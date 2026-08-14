import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="مساعد الدراسة الذكي", page_icon="📚", layout="centered")

st.title("📚 تطبيق الدراسة الذكي")
st.write("أهلاً بك! ارفع ملفاتك وابدأ في الشات وتوليد الأسئلة بسهولة.")

# القائمة الجانبية لإدخال المفتاح
with st.sidebar:
    st.header("⚙️ الإعدادات")
    api_key = st.text_input("أدخل مفتاح Gemini API Key:", type="password")
    st.markdown("---")
    st.caption("تأكد من إدخال المفتاح لتفعيل الذكاء الاصطناعي.")

# التحقق من وجود المفتاح
if not api_key:
    st.info("👈 الرجاء فتح القائمة الجانبية وكتابة مفتاح Gemini API للبدء.")
else:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        # منطقة رفع الملفات
        uploaded_file = st.file_uploader("ارفع ملف الدرس أو المحاضرة (PDF أو صورة):", type=["pdf", "png", "jpg", "jpeg"])

        # منطقة كتابة السؤال أو الطلب
        user_prompt = st.text_area("ماذا تريد أن تفعل؟", placeholder="مثال: اشرح لي هذه المحاضرة / قم بتوليد 5 أسئلة اختيارات...")

        if st.button("🚀 تنفيذ الطلب"):
            if user_prompt:
                with st.spinner("جاري التحليل والتفكير..."):
                    if uploaded_file:
                        # تحضير الملف للموديل
                        bytes_data = uploaded_file.getvalue()
                        mime_type = uploaded_file.type
                        file_part = [{"mime_type": mime_type, "data": bytes_data}]
                        response = model.generate_content([user_prompt, file_part[0]])
                    else:
                        response = model.generate_content(user_prompt)

                    st.markdown("### 📝 النتيجة:")
                    st.write(response.text)
            else:
                st.warning("يرجى كتابة سؤالك أو طلبك أولاً.")

    except Exception as e:
        st.error(f"حدث خطأ أثناء الاتصال بالخدمة: {e}")
