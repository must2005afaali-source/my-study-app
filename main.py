import fitz
import json
import os
import logging
from pathlib import Path
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    filters, ContextTypes, ConversationHandler
)
from google import genai
from google.genai import types

# ========== الإعدادات ==========
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
ADMIN_ID = int(os.environ.get("ADMIN_ID", "0"))

# التحقق من المفاتيح
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is required")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is required")

# إنشاء عميل Gemini
ai_client = genai.Client(api_key=GEMINI_API_KEY)

# إعداد السجلات
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("logs/bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# حالات المحادثة
WAITING_PDF, WAITING_PAGES = range(2)
BATCH_SIZE = 5

# ========== الأوامر ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """أمر البدء"""
    await update.message.reply_text(
        "أهلاً بك! 📄🤖\n\n"
        "أرسل لي ملف PDF وسأستخرج منه أسئلة MCQ فوراً!\n\n"
        "الأوامر:\n"
        "/start - بدء البوت\n"
        "/cancel - إلغاء العملية\n"
        "/stats - الإحصائيات (للأدمن)"
    )
    return WAITING_PDF

async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """معالجة ملفات PDF"""
    document = update.message.document
    
    # التحقق من نوع الملف
    if not document.file_name.lower().endswith('.pdf'):
        await update.message.reply_text("⚠️ يرجى إرسال ملف PDF فقط.")
        return WAITING_PDF
    
    # التحقق من حجم الملف (20MB)
    if document.file_size and document.file_size > 20 * 1024 * 1024:
        await update.message.reply_text("⚠️ الحد الأقصى لحجم الملف 20 ميجابايت.")
        return WAITING_PDF
    
    # تحميل الملف
    pdf_file = await document.get_file()
    file_bytes = await pdf_file.download_as_bytearray()
    
    # حفظ الملف في ذاكرة المستخدم
    context.user_data['pdf_bytes'] = file_bytes
    
    # فتح الملف لمعرفة عدد الصفحات
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    total_pages = len(doc)
    
    await update.message.reply_text(
        f"✅ تم استلام الملف بنجاح!\n"
        f"📄 عدد الصفحات: {total_pages}\n\n"
        "أرسل نطاق الصفحات المطلوبة، مثل:\n"
        "• `1-10`\n"
        "• `5`\n"
        "• `all` لكل الملف",
        parse_mode="Markdown"
    )
    return WAITING_PAGES

async def handle_pages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """معالجة نطاق الصفحات"""
    text = update.message.text.strip().lower()
    
    # التحقق من أن الملف موجود
    pdf_bytes = context.user_data.get('pdf_bytes')
    if not pdf_bytes:
        await update.message.reply_text("❌ لا يوجد ملف محفوظ. أرسل /start من جديد.")
        return ConversationHandler.END
    
    # فتح الملف
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    total_pages = len(doc)
    
    # تحديد الصفحات المطلوبة
    if text in ["all", "الكل", "كل"]:
        start_page = 1
        end_page = total_pages
    else:
        # محاولة تحليل النطاق
        import re
        match = re.match(r'^(\d+)\s*[-_–—]\s*(\d+)$', text)
        
        if match:
            start_page = int(match.group(1))
            end_page = int(match.group(2))
        else:
            # صفحة واحدة
            try:
                start_page = int(text)
                end_page = start_page
            except ValueError:
                await update.message.reply_text(
                    "❌ صيغة غير صحيحة!\n"
                    "أرسل مثل: `1-10` أو `5` أو `all`",
                    parse_mode="Markdown"
                )
                return WAITING_PAGES
    
    # التحقق من صحة النطاق
    if start_page < 1 or end_page > total_pages or start_page > end_page:
        await update.message.reply_text(
            f"⚠️ نطاق غير صالح!\n"
            f"الصفحات المتاحة: 1 إلى {total_pages}"
        )
        return WAITING_PAGES
    
    # حد أقصى 50 صفحة
    if end_page - start_page + 1 > 50:
        await update.message.reply_text("⚠️ الحد الأقصى 50 صفحة لكل طلب.")
        return WAITING_PAGES
    
    # رسالة بدء المعالجة
    status_msg = await update.message.reply_text(
        f"⏳ جاري معالجة {end_page - start_page + 1} صفحة...\n"
        f"قد يستغرق هذا عدة دقائق."
    )
    
    # معالجة الصفحات على دفعات
    total_questions = 0
    
    for i in range(start_page - 1, end_page, BATCH_SIZE):
        chunk_end = min(i + BATCH_SIZE, end_page)
        
        # تحديث رسالة الحالة
        await status_msg.edit_text(
            f"⏳ جاري معالجة الصفحات {i+1} إلى {chunk_end}...\n"
            f"إجمالي الأسئلة حتى الآن: {total_questions}"
        )
        
        # تجهيز المحتوى لـ Gemini
        contents = []
        for p in range(i, chunk_end):
            pix = doc[p].get_pixmap(dpi=150)
            contents.append(
                types.Part.from_bytes(
                    data=pix.tobytes("png"),
                    mime_type="image/png"
                )
            )
        
        # الـ Prompt
        prompt = (
            "قم بتحليل هذه الصفحات واستخراج 3 إلى 5 أسئلة MCQ باللغة العربية.\n"
            "لكل سؤال، وفر 4 خيارات، وحدد مؤشر الخيار الصحيح (من 0 إلى 3)، "
            "وشرحاً مختصراً للإجابة.\n"
            "أرجع النتيجة كـ JSON فقط."
        )
        contents.append(prompt)
        
        try:
            # استدعاء Gemini
            response = ai_client.models.generate_content(
                model='gemini-2.0-flash',
                contents=contents,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema={
                        "type": "ARRAY",
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "question": {"type": "STRING"},
                                "options": {
                                    "type": "ARRAY",
                                    "items": {"type": "STRING"}
                                },
                                "correct_option_id": {"type": "INTEGER"},
                                "explanation": {"type": "STRING"}
                            },
                            "required": [
                                "question", "options",
                                "correct_option_id", "explanation"
                            ]
                        }
                    }
                )
            )
            
            # تحليل النتيجة
            questions = json.loads(response.text)
            
            # إرسال الأسئلة كـ Poll
            for q in questions:
                options = [opt[:100] for opt in q['options'][:4]]
                
                await context.bot.send_poll(
                    chat_id=update.effective_chat.id,
                    question=q['question'][:300],
                    options=options,
                    type="quiz",
                    correct_option_id=int(q['correct_option_id']),
                    explanation=q.get('explanation', '')[:200],
                    is_anonymous=False
                )
                
                total_questions += 1
        
        except Exception as e:
            logger.error(f"Error processing pages {i+1}-{chunk_end}: {e}")
            await update.message.reply_text(
                f"⚠️ حدث خطأ في معالجة الصفحات {i+1}-{chunk_end}."
            )
    
    # رسالة النجاح
    await status_msg.edit_text(
        f"✅ اكتملت العملية بنجاح!\n"
        f"📊 تم إنشاء {total_questions} سؤالاً."
    )
    
    # تنظيف الذاكرة
    context.user_data.pop('pdf_bytes', None)
    
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """إلغاء العملية"""
    context.user_data.clear()
    await update.message.reply_text("✅ تم إلغاء العملية.")
    return ConversationHandler.END

async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """إحصائيات للأدمن"""
    if update.effective_user.id != ADMIN_ID:
        return
    
    await update.message.reply_text(
        "📊 *الإحصائيات:*\n\n"
        "• البوت يعمل ✅\n"
        "• المستخدمون: قيد التطوير\n"
        "• الملفات المعالجة: قيد التطوير",
        parse_mode="Markdown"
    )

# ========== التشغيل ==========
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    # Conversation Handler
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            MessageHandler(filters.Document.ALL, handle_pdf)
        ],
        states={
            WAITING_PDF: [MessageHandler(filters.Document.ALL, handle_pdf)],
            WAITING_PAGES: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_pages)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    
    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("stats", admin_stats))
    
    logger.info("🤖 البوت يعمل الآن...")
    app.run_polling()

if __name__ == '__main__':
    main()Add main.py
