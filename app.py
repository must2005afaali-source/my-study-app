import streamlit as st
import google.generativeai as genai
import io

# -----------------------------------------------------------------------------
# 1. إعدادات الصفحة
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="المساعد الدراسي الذكي | AI Study Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. تصميم الواجهة العصرية (Custom Modern CSS)
# -----------------------------------------------------------------------------
custom_css = """
<style>
/* استيراد خط عربي حديث */
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Tajawal', sans-serif !important;
    direction: rtl;
    text-align: right;
}

/* تحسين الهيدر البصري (Hero Banner) */
.hero-header {
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #EC4899 100%);
    color: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 12px 30px -10px rgba(79, 70, 229, 0.5);
    margin-bottom: 2rem;
}

.hero-header h1 {
    color: white !important;
    font-weight: 800;
    margin-bottom: 0.5rem;
    font-size: 2.2rem;
}

.hero-header p {
    font-size: 1.1rem;
    opacity: 0.95;
    margin: 0;
}

/* بطاقات الإحصائيات والمعلومات */
.stat-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 14px;
    padding: 1.2rem;
    text-align: center;
    backdrop-filter: blur(10px);
}

/* تحسين شكل الأزرار */
.stButton > button {
    background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.65rem 1.2rem !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    transition: all 0.3s ease-in-out !important;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3) !important;
    width: 100%;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(79, 70, 229, 0.5) !important;
}

/* شريط التبويبات الحديث */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: rgba(255, 255, 255, 0.03);
    padding: 8px;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.08);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 10px !important;
    padding: 10px 20px !important;
    font-weight: 700 !important;
}

/* تخصيص القائمة الجانبية */
section[data-testid="stSidebar"] {
    border-left: 1px solid rgba(255, 255, 255, 0.08);
}

/* محاذاة حقول النصوص */
.stTextArea textarea, .stTextInput input, div[data-baseweb="select"] {
    direction: rtl !important;
    text-align: right !important;
    border-radius: 10px !important;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. القائمة الجانبية (Sidebar Design)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3429/3429433.png", width=70)
    st.title("⚙️ لوحة التحكم")
    
    api_key = st.text_input("مفتاح Gemini API Key:", type="password", key="user_api_key")
    
    st.markdown("---")
    st.subheader("🤖 إعدادات المحرك")
    
    model_choice = st.selectbox(
        "النموذج الذكي:",
        ["gemini-1.5-flash", "gemini-1.5-pro"],
        help="Flash للمهام السريعة، و Pro للتحليل العميق."
    )
    
    temperature = st.slider("مستوى الإبداع والتحليل:", 0.0, 1.0, 0.3, 0.1)
    
    st.markdown("---")
    if st.button("🗑️ إعادة ضبط الجلسة"):
        st.session_state.chat_history = []
        st.success("تم مسح السجل!")

# -----------------------------------------------------------------------------
# 4. الواجهة الرئيسية (Hero Section)
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-header">
    <h1>🎓 منصة الدراسة الذكية Ultra</h1>
    <p>حلل المحاضرات، ولّد الاختبارات، وراجع دروسك باستخدام أحدث تقنيات الذكاء الاصطناعي</p>
</div>
""", unsafe_allow_html=True)

if not api_key:
    st.info("💡 **للبدء:** يرجى فتح القائمة الجانبية وإدخال مفتاح Gemini API Key الخاص بك.")
    st.stop()

# ربط Gemini
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=model_choice,
        generation_config={"temperature": temperature}
    )
except Exception as e:
    st.error(f"خطأ في الاتصال بالخدمة: {e}")
    st.stop()

# -----------------------------------------------------------------------------
# 5. قسم رفع الملفات الإنسيابي
# -----------------------------------------------------------------------------
with st.container():
    st.subheader("📂 مركز رفع المستندات")
    uploaded_files = st.file_uploader(
        "قم بسحب وإسقاط ملفات الـ PDF، الصور، أو الملاحظات هنا:",
        type=["pdf", "png", "jpg", "jpeg", "txt"],
        accept_multiple_files=True
    )

def process_files(files):
    formatted_parts = []
    for f in files:
        bytes_data = f.getvalue()
        if f.type == "text/plain":
            formatted_parts.append(bytes_data.decode("utf-8"))
        else:
            formatted_parts.append({"mime_type": f.type, "data": bytes_data})
    return formatted_parts

file_parts = process_files(uploaded_files) if uploaded_files else []

# عرض إحصائيات سريعة للملفات المرفوعة
if uploaded_files:
    m1, m2, m3 = st.columns(3)
    m1.metric("عدد الملفات المرفوعة", f"{len(uploaded_files)} ملفات")
    m2.metric("حالة النظام", "جاهز للتحليل 🚀")
    m3.metric("النموذج النشط", model_choice.split('-')[2].upper())

st.markdown("---")

# -----------------------------------------------------------------------------
# 6. التبويبات الرئيسية (Main Interactive Tabs)
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📑 التلخيص والاستخراج", 
    "🧪 صانع الاختبارات", 
    "📇 بطاقات المراجعة", 
    "💬 الشات التفاعلي", 
    "🛠️ أدوات المذاكرة"
])

# -----------------------------------------------------------------------------
# التبويب الأول: التلخيص
# -----------------------------------------------------------------------------
with tab1:
    st.markdown("### 🔍 تلخيص واستخراج المفاهيم")
    col1, col2 = st.columns(2)
    with col1:
        summary_type = st.selectbox("نمط التلخيص المطلوب:", ["نقاط رئيسية وهامة", "ملخص تفصيلي شامل", "ملخص تنفيذي سريع"])
    with col2:
        extract_option = st.multiselect("استخراج إضافي تلقائي:", ["المصطلحات والتعاريف", "القوانين والمعادلات", "أهم الأسئلة"])

    if st.button("✨ بدء التلخيص والتحليل"):
        if not file_parts:
            st.error("يرجى رفع ملف واحد على الأقل أولاً!")
        else:
            prompt = f"قم بإنشاء {summary_type} باللغة العربية بأسلوب منظم وواضح."
            if extract_option:
                prompt += f" مع استخراج {', '.join(extract_option)} في أقسام منفصلة."
            
            with st.spinner("جاري قراءة الملفات وتحليل الأفكار..."):
                response = model.generate_content([prompt] + file_parts)
                st.markdown("#### 📝 النتيجة:")
                st.markdown(response.text)
                st.download_button("📥 تحميل الملخص كملف نصي", response.text, file_name="study_summary.txt")

# -----------------------------------------------------------------------------
# التبويب الثاني: توليد الاختبارات
# -----------------------------------------------------------------------------
with tab2:
    st.markdown("### 🧪 إنشاء اختبارات تفاعلية")
    c1, c2, c3 = st.columns(3)
    with c1:
        num_questions = st.number_input("عدد الأسئلة:", 1, 20, 5)
    with c2:
        difficulty = st.selectbox("مستوى الصعوبة:", ["سهل", "متوسط", "صعب"])
    with c3:
        q_type = st.selectbox("نوع الأسئلة:", ["اختيار من متعدد (MCQ)", "صح / خطأ", "أسئلة مقالية قصيرة"])

    if st.button("🚀 توليد الاختبار الآن"):
        if not file_parts:
            st.error("يرجى رفع المحاضرة أو الملفات أولاً!")
        else:
            prompt = f"قم بإنشاء اختبار من {num_questions} أسئلة نوع ({q_type}) وبمستوى ({difficulty}) بناءً على المحتوى المرفق. ضع نموذج الإجابات الشارح في النهاية."
            with st.spinner("جاري صياغة الأسئلة..."):
                response = model.generate_content([prompt] + file_parts)
                st.markdown(response.text)
                st.download_button("📥 تحميل الاختبار", response.text, file_name="quiz.txt")

# -----------------------------------------------------------------------------
# التبويب الثالث: بطاقات المراجعة (Flashcards)
# -----------------------------------------------------------------------------
with tab3:
    st.markdown("### 📇 بطاقات الاستذكار السريعة")
    num_cards = st.slider("عدد البطاقات المطلوبة:", 3, 15, 6)
    
    if st.button("🃏 إنشاء البطاقات"):
        if not file_parts:
            st.error("يرجى رفع ملف أولاً!")
        else:
            prompt = f"قم بإنشاء {num_cards} بطاقات استذكار سريعة (سؤال وجواب) مأخوذة من المادة المرفقة بشكل منسق يسهل الحفظ."
            with st.spinner("جاري تجهيز البطاقات..."):
                response = model.generate_content([prompt] + file_parts)
                st.markdown(response.text)

# -----------------------------------------------------------------------------
# التبويب الرابع: الشات التفاعلي
# -----------------------------------------------------------------------------
with tab4:
    st.markdown("### 💬 ناقش المادة مع الذكاء الاصطناعي")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        st.chat_message(msg["role"]).write(msg["content"])

    user_query = st.chat_input("اسأل عن أي نقطة غير مفهومة في الملف...")
    if user_query:
        if not file_parts:
            st.error("يرجى رفع المستند أولاً لكي يستطيع الإجابة منه.")
        else:
            st.chat_message("user").write(user_query)
            st.session_state.chat_history.append({"role": "user", "content": user_query})
            
            prompt = f"أجب عن السؤال التالي بدقة واختصار استناداً إلى الملفات المرفقة فقط: {user_query}"
            with st.spinner("جاري البحث في المستند..."):
                response = model.generate_content([prompt] + file_parts)
                st.chat_message("assistant").write(response.text)
                st.session_state.chat_history.append({"role": "assistant", "content": response.text})

# -----------------------------------------------------------------------------
# التبويب الخامس: أدوات إضافية
# -----------------------------------------------------------------------------
with tab5:
    st.markdown("### 🛠️ أدوات ودعم إضافي")
    sub1, sub2, sub3 = st.tabs(["🗓️ جدول المذاكرة", "🌐 الترجمة الفورية", "💡 التبسيط للأطفال (ELI5)"])
    
    with sub1:
        days = st.number_input("عدد الأيام المتاحة قبل الامتحان:", 1, 30, 3)
        if st.button("📅 إنشاء جدول المذاكرة"):
            if file_parts:
                res = model.generate_content([f"وزع دراسة هذا الملف على {days} أيام بجدول زمني منظم."] + file_parts)
                st.write(res.text)
            else:
                st.error("ارفع الملف أولاً.")

    with sub2:
        lang = st.radio("ترجمة الملخص إلى:", ["العربية", "English"])
        if st.button("🌐 ترجمة"):
            if file_parts:
                res = model.generate_content([f"ترجم الأفكار الرئيسية في المستند إلى {lang}."] + file_parts)
                st.write(res.text)
            else:
                st.error("ارفع الملف أولاً.")

    with sub3:
        if st.button("👶 اشرح لي بأسلوب بسيط جداً"):
            if file_parts:
                res = model.generate_content(["اشرح المفاهيم المعقدة في هذا الملف بأسلوب مبسط جداً باستخدام أمثلة واقعية."] + file_parts)
                st.write(res.text)
            else:
                st.error("ارفع الملف أولاً.")
