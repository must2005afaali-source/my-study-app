import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(
    page_title="الأكاديمية الذكية الشاملة",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# إخفاء واجهة Streamlit الافتراضية وتوحيد الخلفية
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background-color: #030712;}
    section.main > div.block-container {
        max-width: 100% !important;
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# قراءة ملف HTML وتشغيله داخل iframe يدعم JavaScript
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    components.html(html_code, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ ملف index.html غير موجود — تأكد من رفعه في نفس مجلد app.py")
