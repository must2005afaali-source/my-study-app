import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="الأكاديمية الذكية", page_icon="🎓", layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>#MainMenu,footer,header{display:none}.stApp{background:#f0f2f5}.block-container{max-width:100%!important;padding:0!important}</style>", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
*{font-family:'Tajawal',sans-serif;box-sizing:border-box}
body{background:#f0f2f5;color:#050505;margin:0}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-thumb{background:#bcc0c4;border-radius:9px}
.fb-card{background:#fff;border-radius:10px;box-shadow:0 1px 2px rgba(0,0,0,.12)}
.fb-btn{background:#e4e6eb;border-radius:8px;transition:.15s;cursor:pointer}
.fb-btn:hover{background:#d8dadf}
.fb-blue{background:#1877f2;color:#fff;border-radius:8px;transition:.15s;cursor:pointer}
.fb-blue:hover{background:#166fe5}
.tab{position:relative;padding:10px 16px;border-radius:8px;color:#65676b;cursor:pointer;font-size:13px;font-weight:700}
.tab:hover{background:#f2f2f2}
.tab.on{color:#1877f2}
.tab.on:after{content:'';position:absolute;bottom:-4px;right:0;left:0;height:3px;background:#1877f2;border-radius:3px}
.fin{background:#f0f2f5;border-radius:20px;padding:8px 14px;border:none;outline:none;font-size:12px}
.story{width:105px;height:170px;border-radius:12px;position:relative;cursor:pointer;transition:.2s;flex-shrink:0;overflow:hidden}
.story:hover{transform:scale(1.04)}
.view{display:none}.view.on{display:flex;animation:vin .25s}
@keyframes vin{from{opacity:0;transform:translateY(8px)}to{opacity:1}}
.xpf{position:fixed;pointer-events:none;font-weight:900;font-size:22px;color:#f59e0b;text-shadow:0 0 14px rgba(245,158,11,.7);animation:fu 1.3s forwards;z-index:999}
@keyframes fu{to{opacity:0;transform:translateY(-70px) scale(1.4)}}
.toast{animation:ti .3s}@keyframes ti{from{transform:translateX(100%)}to{transform:none}}
.card3d{perspective:900px}.card3d .in{position:relative;width:100%;height:100%;transition:transform .5s;transform-style:preserve-3d}
.card3d.fl .in{transform:rotateY(180deg)}
.card3d .f,.card3d .b{position:absolute;inset:0;backface-visibility:hidden;border-radius:10px;display:flex;align-items:center;justify-content:center;text-align:center;padding:4px}
.card3d .b{transform:rotateY(180deg)}
.tile{width:40px;height:40px;display:flex;align-items:center;justify-content:center;background:#1877f2;border:2px solid #8ab4f8;border-radius:8px;font-weight:900;font-size:16px;cursor:pointer;user-select:none;color:#fff}
.tile.used{opacity:.25;pointer-events:none}
.ok{background:#d1fae5!important;border-color:#10b981!important;color:#065f46!important}
.no{background:#fee2e2!important;border-color:#f43f5e!important;color:#991b1b!important}
.pbar{transition:width .5s}
.gem{background:linear-gradient(135deg,#4285f4,#9b72f0,#f6c177);-webkit-background-clip:text;color:transparent;font-weight:900}
.orb{width:110px;height:110px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#8ab4f8,#4285f4 45%,#7b4ff0 80%);animation:orb 2.5s ease-in-out infinite;box-shadow:0 0 60px rgba(66,133,244,.6)}
@keyframes orb{50%{transform:scale(1.12);box-shadow:0 0 90px rgba(123,79,240,.8)}}
.wave{display:flex;gap:3px;align-items:flex-end;height:24px}
.wave i{width:4px;background:#8ab4f8;border-radius:4px;animation:wv 1s infinite}
.wave i:nth-child(2){animation-delay:.15s}.wave i:nth-child(3){animation-delay:.3s}.wave i:nth-child(4){animation-delay:.45s}.wave i:nth-child(5){animation-delay:.6s}
@keyframes wv{0%,100%{height:5px}50%{height:22px}}
.dot{width:9px;height:9px;background:#31a24c;border-radius:50%;border:2px solid #fff;position:absolute;bottom:0;left:0}
</style>
</head>
<body>
<div id="toasts" class="fixed top-16 right-3 z-50 flex flex-col gap-2"></div>

<div class="h-screen flex flex-col">

<!-- الشريط العلوي بفيسبوك -->
<header class="bg-white shadow px-3 h-14 flex items-center justify-between gap-2 z-20 flex-shrink-0">
  <div class="flex items-center gap-2">
    <div class="w-10 h-10 rounded-full bg-[#1877f2] flex items-center justify-center text-white text-xl font-black">أ</div>
    <div class="hidden sm:block"><b class="text-[15px] text-[#1877f2]">الأكاديمية</b><p class="text-[9px] text-gray-500">تعلّم • تحدَّ • تحدث</p></div>
    <input id="search" class="fin w-32 md:w-52 mr-2" placeholder="🔍 ابحث عن لعبة…">
  </div>
  <nav class="flex items-center gap-1">
    <div data-v="home" class="tab on">🏠<span class="hidden lg:inline"> الرئيسية</span></div>
    <div data-v="games" class="tab">🎮<span class="hidden lg:inline"> الألعاب</span></div>
    <div data-v="study" class="tab">📚<span class="hidden lg:inline"> الدراسة</span></div>
    <div data-v="ai" class="tab">✨<span class="hidden lg:inline"> المساعد</span></div>
    <div data-v="board" class="tab">🏆<span class="hidden lg:inline"> التصنيف</span></div>
  </nav>
  <div class="flex items-center gap-1.5">
    <span class="bg-amber-100 text-amber-700 px-2 py-1 rounded-full text-[10px] font-bold">🔥 <b id="stV">1</b></span>
    <span class="bg-purple-100 text-purple-700 px-2 py-1 rounded-full text-[10px] font-bold">⚡x<b id="cbV">0</b></span>
    <span class="bg-blue-100 text-blue-700 px-2 py-1 rounded-full text-[10px] font-bold">🏆 <b id="xpV">0</b></span>
    <button onclick="switchView('badges')" class="fb-btn w-9 h-9 relative text-base">🔔<span id="bellN" class="absolute -top-1 -left-1 bg-red-500 text-white text-[8px] w-4 h-4 rounded-full flex items-center justify-center font-bold">0</span></button>
    <a href="https://t.me/m3v30" target="_blank" class="fb-blue w-9 h-9 flex items-center justify-center text-base" title="الدعم الفني @m3v30">📨</a>
  </div>
</header>

<div class="flex-1 flex overflow-hidden max-w-[1400px] w-full mx-auto">

<!-- الشريط الأيمن (اختصارات) -->
<aside class="w-64 hidden xl:flex flex-col gap-1 p-3 overflow-y-auto">
  <div data-v="home" class="sv flex items-center gap-2 p-2 rounded-lg hover:bg-[#e4e6eb] cursor-pointer text-[12px] font-bold">🏠 الرئيسية</div>
  <div data-v="games" class="sv flex items-center gap-2 p-2 rounded-lg hover:bg-[#e4e6eb] cursor-pointer text-[12px] font-bold">🎮 الألعاب الذهنية</div>
  <div data-v="study" class="sv flex items-center gap-2 p-2 rounded-lg hover:bg-[#e4e6eb] cursor-pointer text-[12px] font-bold">📚 قسم الدراسة والملفات</div>
  <div data-v="ai" class="sv flex items-center gap-2 p-2 rounded-lg hover:bg-[#e4e6eb] cursor-pointer text-[12px] font-bold">✨ المساعد الصوتي</div>
  <div data-v="badges" class="sv flex items-center gap-2 p-2 rounded-lg hover:bg-[#e4e6eb] cursor-pointer text-[12px] font-bold">🏅 الإنجازات</div>
  <div data-v="board" class="sv flex items-center gap-2 p-2 rounded-lg hover:bg-[#e4e6eb] cursor-pointer text-[12px] font-bold">🏆 المتصدرين والخصوصية</div>
  <a href="https://t.me/m3v30" target="_blank" class="flex items-center gap-2 p-2 rounded-lg hover:bg-[#e4e6eb] text-[12px] font-bold text-[#1877f2]">📨 الدعم الفني 24/7</a>
  <div class="fb-card p-3 mt-2 text-[11px]">
    <b>📊 إحصائياتك</b>
    <div class="grid grid-cols-2 gap-1 mt-2 text-center">
      <div class="bg-[#f0f2f5] rounded p-1.5"><p class="text-[9px] text-gray-500">مستوى</p><b id="lvV" class="text-[#1877f2]">1</b></div>
      <div class="bg-[#f0f2f5] rounded p-1.5"><p class="text-[9px] text-gray-500">دقة</p><b id="hAcc" class="text-emerald-600">0%</b></div>
      <div class="bg-[#f0f2f5] rounded p-1.5"><p class="text-[9px] text-gray-500">صحيحة</p><b id="hCor" class="text-amber-600">0</b></div>
      <div class="bg-[#f0f2f5] rounded p-1.5"><p class="text-[9px] text-gray-500">إنجازات</p><b id="hBdg" class="text-purple-600">0</b></div>
    </div>
  </div>
</aside>

<!-- العمود الأوسط -->
<main class="flex-1 overflow-y-auto p-3">

<!-- الرئيسية (فيد) -->
<section id="v-home" class="view on flex-col gap-3 max-w-xl mx-auto">
  <div class="flex gap-2 overflow-x-auto pb-1">
    <div class="story bg-gradient-to-b from-blue-500 to-blue-700" onclick="goGame(1)"><div class="absolute inset-0 flex flex-col items-center justify-center text-white"><span class="text-3xl">🧮</span><b class="text-[10px] mt-1">حساب سريع</b></div></div>
    <div class="story bg-gradient-to-b from-purple-500 to-purple-800" onclick="goGame(2)"><div class="absolute inset-0 flex flex-col items-center justify-center text-white"><span class="text-3xl">📜</span><b class="text-[10px] mt-1">تاريخ</b></div></div>
    <div class="story bg-gradient-to-b from-cyan-500 to-cyan-700" onclick="goGame(3)"><div class="absolute inset-0 flex flex-col items-center justify-center text-white"><span class="text-3xl">⚛️</span><b class="text-[10px] mt-1">فيزياء</b></div></div>
    <div class="story bg-gradient-to-b from-pink-500 to-rose-700" onclick="goGame(4)"><div class="absolute inset-0 flex flex-col items-center justify-center text-white"><span class="text-3xl">🧠</span><b class="text-[10px] mt-1">ذاكرة</b></div></div>
    <div class="story bg-gradient-to-b from-amber-500 to-orange-700" onclick="goGame(5)"><div class="absolute inset-0 flex flex-col items-center justify-center text-white"><span class="text-3xl">🔠</span><b class="text-[10px] mt-1">كلمات</b></div></div>
    <div class="story bg-[#e4e6eb]" onclick="switchView('study')"><div class="absolute inset-0 flex flex-col items-center justify-center text-gray-700"><span class="text-3xl">📚</span><b class="text-[10px] mt-1">ذاكر ملف</b></div></div>
  </div>

  <div class="fb-card p-3">
    <div class="flex items-center gap-2">
      <div class="w-10 h-10 rounded-full bg-[#1877f2] flex items-center justify-center text-white font-black">أ</div>
      <button onclick="switchView('study')" class="fin flex-1 text-right text-gray-500 hover:bg-[#e4e6eb]">ماذا تدرس اليوم؟ 📚</button>
    </div>
    <div class="border-t mt-3 pt-2 grid grid-cols-3 gap-1 text-center text-[11px] font-bold text-gray-600">
      <button onclick="goGame(1)" class="fb-btn p-1.5">🎮 لعبة</button>
      <button onclick="switchView('ai')" class="fb-btn p-1.5">✨ مساعد</button>
      <button onclick="startCall()" class="fb-btn p-1.5 text-emerald-700">📞 اتصال</button>
    </div>
  </div>

  <div class="fb-card p-3">
    <div class="flex items-center justify-between mb-2"><b class="text-[13px]">☀️ تحدي اليوم</b><span class="text-[10px] text-gray-500">+200 XP</span></div>
    <p class="text-[11px] text-gray-600 mb-2">أكمل 3 جولات حقيقية لتربح المكافأة</p>
    <div class="flex items-center gap-2"><div class="flex-1 h-2 bg-[#f0f2f5] rounded-full"><div id="dBar" class="pbar h-full bg-[#1877f2] rounded-full" style="width:0%"></div></div><span id="dTxt" class="text-[10px] text-gray-500">0/3</span></div>
  </div>

  <div class="fb-card p-3">
    <b class="text-[13px]">📰 آخر نشاطاتك</b>
    <div id="feed" class="mt-2 space-y-2 text-[11px]"><p class="text-gray-400">لا نشاطات بعد… العب وتعلم!</p></div>
  </div>
</section>

<!-- الألعاب -->
<section id="v-games" class="view flex-col gap-3 max-w-xl mx-auto w-full">
  <div id="gList" class="flex flex-col gap-3">
    <div class="fb-card p-3"><b class="text-[13px] text-[#1877f2]">🎮 ساحة التحديات — النقاط للصحيح فقط ✅</b>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-2" id="gGrid"></div>
    </div>
  </div>
  <div id="gScreen" class="hidden flex-col gap-2">
    <div class="fb-card p-2 flex items-center justify-between">
      <button onclick="backToGames()" class="fb-btn px-3 py-1.5 text-[11px] font-bold">→ رجوع</button>
      <b id="gsTitle" class="text-[12px] text-[#1877f2]"></b>
      <span class="text-[11px]">النقاط: <b id="gsScore" class="text-amber-600">0</b></span>
    </div>
    <div id="gsBody" class="fb-card p-4 min-h-[300px] flex flex-col items-center justify-center gap-3 text-center"></div>
  </div>
</section>

<!-- الدراسة -->
<section id="v-study" class="view flex-col gap-3 max-w-xl mx-auto w-full">
  <div class="fb-card p-3">
    <b class="text-[13px] text-[#1877f2]">📚 قسم الدراسة — ارفع ملفك وذاكر بذكاء</b>
    <label class="mt-2 flex flex-col items-center gap-1 border-2 border-dashed border-[#bcc0c4] rounded-xl p-5 cursor-pointer hover:bg-blue-50">
      <span class="text-3xl">📤</span><b class="text-[11px]">ارفع PDF أو TXT أو MD</b>
      <input type="file" id="fileIn" accept=".pdf,.txt,.md" class="hidden">
    </label>
  </div>
  <div id="studyOut" class="hidden flex flex-col gap-3">
    <div class="fb-card p-3 grid grid-cols-3 gap-2 text-center text-[10px]">
      <div class="bg-[#f0f2f5] rounded p-2"><p class="text-gray-500">الملف</p><b id="stName" class="text-[#1877f2]">-</b></div>
      <div class="bg-[#f0f2f5] rounded p-2"><p class="text-gray-500">الكلمات</p><b id="stWords">-</b></div>
      <div class="bg-[#f0f2f5] rounded p-2"><p class="text-gray-500">صفحات</p><b id="stPages">-</b></div>
    </div>
    <div class="fb-card p-3"><b class="text-[12px] text-emerald-700">✨ الملخص</b><p id="stSum" class="text-[11px] text-gray-700 mt-1 leading-relaxed">-</p></div>
    <div class="fb-card p-3"><b class="text-[12px] text-purple-700">🔑 كلمات مفتاحية</b><div id="stKeys" class="flex flex-wrap gap-1 mt-1"></div></div>
    <div class="grid grid-cols-2 gap-2">
      <button onclick="genCards()" class="fb-blue p-2 text-[11px] font-bold">🎴 بطاقات تعليمية</button>
      <button onclick="genQuiz()" class="fb-blue p-2 text-[11px] font-bold">📝 اختبار من الملف</button>
    </div>
    <div id="studyTools" class="flex flex-col gap-2"></div>
    <div class="fb-card p-3"><b class="text-[12px] text-gray-600">📄 النص</b><div id="stText" class="text-[10px] text-gray-500 max-h-32 overflow-y-auto mt-1"></div></div>
  </div>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
    <div class="fb-card p-3 text-center">
      <b class="text-[12px]">🍅 مؤقت بومودورو</b>
      <div id="pomoTime" class="text-3xl font-black text-[#1877f2] my-2">25:00</div>
      <div class="flex gap-1 justify-center">
        <button onclick="pomoStart()" class="fb-blue px-3 py-1.5 text-[10px] font-bold">بدء</button>
        <button onclick="pomoPause()" class="fb-btn px-3 py-1.5 text-[10px] font-bold">إيقاف</button>
        <button onclick="pomoReset()" class="fb-btn px-3 py-1.5 text-[10px] font-bold">تصفير</button>
      </div>
      <p class="text-[9px] text-gray-500 mt-1">جلسة كاملة = +50 XP</p>
    </div>
    <div class="fb-card p-3">
      <b class="text-[12px]">📝 ملاحظاتي</b>
      <div class="flex gap-1 mt-2"><input id="noteIn" class="fin flex-1" placeholder="اكتب ملاحظة…"><button onclick="addNote()" class="fb-blue px-3 text-[10px] font-bold">+</button></div>
      <div id="noteList" class="mt-2 space-y-1 max-h-28 overflow-y-auto"></div>
    </div>
  </div>
</section>

<!-- المساعد (Gemini) -->
<section id="v-ai" class="view flex-col gap-2 max-w-xl mx-auto w-full h-full">
  <div class="fb-card p-4 text-center">
    <div class="text-3xl gem inline-block">✦</div>
    <h2 class="gem text-lg">مرحباً بيك! شلونك؟</h2>
    <p class="text-[11px] text-gray-500">أني مساعدك الذكي — اسألني نصياً أو صوتياً وأجاوبك بسرعة</p>
  </div>
  <div id="log" class="flex-1 overflow-y-auto space-y-2 p-1 min-h-[200px]"></div>
  <div class="flex gap-1.5 overflow-x-auto pb-1">
    <button onclick="askChip(this)" class="fb-btn px-3 py-1.5 rounded-full text-[10px] whitespace-nowrap">شرحلي النسبية ببساطة</button>
    <button onclick="askChip(this)" class="fb-btn px-3 py-1.5 rounded-full text-[10px] whitespace-nowrap">أريد خطة مذاكرة</button>
    <button onclick="askChip(this)" class="fb-btn px-3 py-1.5 rounded-full text-[10px] whitespace-nowrap">شلون أحسب المشتقة؟</button>
    <button onclick="askChip(this)" class="fb-btn px-3 py-1.5 rounded-full text-[10px] whitespace-nowrap">احكيلي عن بغداد</button>
  </div>
  <div class="fb-card flex items-center gap-1 p-1.5 rounded-full shadow">
    <button onclick="micOnce()" class="w-9 h-9 rounded-full hover:bg-[#f0f2f5] text-base">🎙️</button>
    <input id="inp" class="flex-1 bg-transparent text-[12px] outline-none" placeholder="اكتب سؤالك هنا…">
    <button onclick="sendMsg()" class="w-9 h-9 rounded-full bg-[#1877f2] text-white">➤</button>
    <button onclick="startCall()" class="w-9 h-9 rounded-full hover:bg-[#f0f2f5] text-base" title="اتصال صوتي">📞</button>
  </div>
</section>

<!-- التصنيف -->
<section id="v-board" class="view flex-col gap-3 max-w-xl mx-auto w-full">
  <div class="fb-card p-3 flex items-center justify-between flex-wrap gap-2">
    <b class="text-[12px]">🕶️ الخصوصية والهوية الرمزية</b>
    <div class="flex items-center gap-2">
      <label class="text-[10px] font-bold">الظهور <input type="checkbox" id="tgLb" checked class="accent-[#1877f2]"></label>
      <select id="avSel" class="fin text-[10px] font-bold">
        <option>الفيزيائي المجهول ⚛️</option><option>المحقق التاريخي 📜</option><option>عبقري الخوارزميات 💻</option><option>مكتشف المجرات 🌌</option>
      </select>
    </div>
  </div>
  <div class="fb-card p-2 flex justify-between text-[11px] bg-amber-50"><span>🥇 الراحل عبر الزمن ⏳</span><b class="text-amber-600">3,450 XP</b></div>
  <div class="fb-card p-2 flex justify-between text-[11px]"><span>🥈 صانع المعادلات 🧮</span><b>2,980 XP</b></div>
  <div id="uCard" class="fb-card p-2 flex justify-between text-[11px] border-2 border-[#1877f2] bg-blue-50"><span id="uName">الفيزيائي المجهول ⚛️ (أنت)</span><b id="uXP" class="text-[#1877f2]">0 XP</b></div>
  <div id="hidB" class="hidden fb-card p-4 text-center text-[10px] text-gray-500">🕶️ وضع الخصوصية — نقاطك محلية فقط</div>
  <div class="fb-card p-2 flex justify-between text-[11px]"><span>#4 فارس المنطق 🛡️</span><b class="text-gray-500">950 XP</b></div>
</section>

<!-- الإنجازات -->
<section id="v-badges" class="view flex-col gap-3 max-w-xl mx-auto w-full">
  <div class="fb-card p-3"><b class="text-[13px] text-amber-600">🏅 الإنجازات — تُفتح بالأداء الحقيقي فقط</b></div>
  <div id="bGrid" class="grid grid-cols-2 sm:grid-cols-3 gap-2"></div>
</section>

</main>

<!-- جهات الاتصال -->
<aside class="w-64 hidden xl:flex flex-col gap-1 p-3 overflow-y-auto">
  <b class="text-[11px] text-gray-500 mb-1">جهات الاتصال</b>
  <div class="flex items-center gap-2 p-1.5 rounded-lg hover:bg-[#e4e6eb] cursor-pointer relative"><div class="relative w-9 h-9 rounded-full bg-purple-200 flex items-center justify-center">⏳<span class="dot"></span></div><div><b class="text-[11px]">الراحل عبر الزمن</b><p class="text-[9px] text-emerald-600">متصل الآن</p></div></div>
  <div class="flex items-center gap-2 p-1.5 rounded-lg hover:bg-[#e4e6eb] cursor-pointer relative"><div class="relative w-9 h-9 rounded-full bg-blue-200 flex items-center justify-center">🧮<span class="dot"></span></div><div><b class="text-[11px]">صانع المعادلات</b><p class="text-[9px] text-emerald-600">متصل الآن</p></div></div>
  <div class="flex items-center gap-2 p-1.5 rounded-lg hover:bg-[#e4e6eb] cursor-pointer relative"><div class="relative w-9 h-9 rounded-full bg-emerald-200 flex items-center justify-center">🛡️<span class="dot" style="background:#bcc0c4"></span></div><div><b class="text-[11px]">فارس المنطق</b><p class="text-[9px] text-gray-400">قبل ساعة</p></div></div>
  <div class="fb-card p-3 mt-3 text-center">
    <b class="text-[11px] text-[#1877f2]">تحتاج مساعدة؟</b>
    <p class="text-[9px] text-gray-500 my-1">فريق الدعم متواجد 24/7</p>
    <a href="https://t.me/m3v30" target="_blank" class="fb-blue block p-2 text-[10px] font-bold">📨 راسلنا تلغرام</a>
  </div>
</aside>
</div>
</div>

<!-- شاشة الاتصال -->
<div id="ov" class="hidden fixed inset-0 bg-black/95 z-50 flex flex-col items-center justify-center gap-4">
  <div id="ovOrb" class="orb"></div>
  <b class="text-white text-lg">المساعد الذكي</b>
  <p id="ovSt" class="text-xs text-[#8ab4f8]">جارٍ الاتصال…</p>
  <div id="ovW" class="wave hidden"><i></i><i></i><i></i><i></i><i></i></div>
  <p id="ovT" class="text-xs text-gray-300 max-w-xs text-center min-h-5 px-4"></p>
  <button onclick="endCall()" class="bg-red-600 hover:bg-red-700 px-8 py-2.5 rounded-full text-sm font-bold text-white">📴 إنهاء المكالمة</button>
</div>

<a href="https://t.me/m3v30" target="_blank" class="fixed bottom-4 left-4 z-40 w-12 h-12 rounded-full bg-[#1877f2] shadow-xl flex items-center justify-center text-xl hover:scale-110 transition">📨</a>

<script>
var $=function(id){return document.getElementById(id)};
function shuffle(a){return a.slice().sort(function(){return Math.random()-.5})}
function norm(s){return (s||'').replace(/[أإآ]/g,'ا').replace(/ة/g,'ه').replace(/ى/g,'ي').trim()}
var S={xp:0,correct:0,total:0,combo:0,best:0,streak:1,daily:0,badges:[],perfect:0,voice:0,file:0,pomo:0,notes:[]};
try{var d=localStorage.getItem('acad6');if(d)S=Object.assign(S,JSON.parse(d));}catch(e){}
function save(){try{localStorage.setItem('acad6',JSON.stringify(S))}catch(e){}}
function toast(m,t){var c=t==='ok'?'border-emerald-500':(t==='no'?'border-red-500':'border-[#1877f2]');
var d=document.createElement('div');d.className='toast bg-white px-3 py-2 rounded-lg shadow-lg border-r-4 text-[11px] font-bold '+c;d.textContent=m;
$('toasts').appendChild(d);setTimeout(function(){d.remove()},2600);}
function sound(t){try{var c=new (window.AudioContext||window.webkitAudioContext)();var o=c.createOscillator();var g=c.createGain();
o.connect(g);g.connect(c.destination);g.gain.setValueAtTime(.07,c.currentTime);
var f=t==='ok'?[880,1100]:(t==='no'?[300,200]:[523,659,784]);
f.forEach(function(x,i){o.frequency.setValueAtTime(x,c.currentTime+i*.08)});
g.gain.exponentialRampToValueAtTime(.01,c.currentTime+.3);o.start();o.stop(c.currentTime+.3);}catch(e){}}
function floatXP(n,ev){if(!ev)return;var d=document.createElement('div');d.className='xpf';d.textContent='+'+n;d.style.left=ev.clientX+'px';d.style.top=ev.clientY+'px';document.body.appendChild(d);setTimeout(function(){d.remove()},1300);}
function record(ok){S.total++;if(ok){S.correct++;S.combo++;if(S.combo>S.best)S.best=S.combo;}else S.combo=0;}
function addXP(n,ev){S.xp+=n;floatXP(n,ev);S.daily++;
if(S.daily===3){S.xp+=200;toast('☀️ تحدي اليوم اكتمل! +200 XP','ok');sound('up');}
act('+'+n+' XP');updateUI();}
function act(t){var f=$('feed');if(f.querySelector('p'))f.innerHTML='';
var d=document.createElement('div');d.className='flex justify-between bg-[#f0f2f5] p-2 rounded-lg';
d.innerHTML='<span>'+t+'</span><span class="text-gray-400">'+new Date().toLocaleTimeString('ar-IQ',{hour:'2-digit',minute:'2-digit'})+'</span>';
f.prepend(d);while(f.children.length>5)f.lastChild.remove();}
function updateUI(){$('xpV').textContent=S.xp;$('stV').textContent=S.streak;$('cbV').textContent=S.combo;
$('lvV').textContent=Math.floor(S.xp/500)+1;
$('hAcc').textContent=(S.total?Math.round(S.correct/S.total*100):0)+'%';
$('hCor').textContent=S.correct;$('hBdg').textContent=S.badges.length;$('bellN').textContent=S.badges.length;
$('dBar').style.width=Math.min(100,S.daily/3*100)+'%';$('dTxt').textContent=Math.min(3,S.daily)+'/3';
$('uXP').textContent=S.xp+' XP';save();checkBadges();}
var BADGES=[
{id:'b1',i:'🎯',t:'أول إصابة',d:'إجابة صحيحة',c:function(){return S.correct>=1}},
{id:'b2',i:'🧠',t:'عقل حاد',d:'25 صحيحة',c:function(){return S.correct>=25}},
{id:'b3',i:'🔥',t:'سلسلة x5',d:'كومبو 5',c:function(){return S.best>=5}},
{id:'b4',i:'💎',t:'جامع النقاط',d:'1000 XP',c:function(){return S.xp>=1000}},
{id:'b5',i:'🏅',t:'علامة كاملة',d:'جولة مثالية',c:function(){return S.perfect>=1}},
{id:'b6',i:'🎙️',t:'متحدث بارع',d:'تحدث صوتياً',c:function(){return S.voice>=1}},
{id:'b7',i:'📚',t:'طالب مجتهد',d:'حلل ملف دراسة',c:function(){return S.file>=1}},
{id:'b8',i:'🍅',t:'بومودورو',d:'جلسة دراسة كاملة',c:function(){return S.pomo>=1}}];
function checkBadges(){BADGES.forEach(function(b){if(S.badges.indexOf(b.id)<0&&b.c()){S.badges.push(b.id);toast('🏅 إنجاز جديد: '+b.t,'ok');sound('up');}});
$('bGrid').innerHTML=BADGES.map(function(b){var u=S.badges.indexOf(b.id)>=0;
return '<div class="fb-card p-3 text-center '+(u?'border-2 border-amber-400':'opacity-50')+'"><div class="text-2xl">'+(u?b.i:'🔒')+'</div><b class="text-[10px]">'+b.t+'</b><p class="text-[9px] text-gray-500">'+b.d+'</p></div>';}).join('');}
function switchView(v){document.querySelectorAll('.view').forEach(function(x){x.classList.remove('on')});
$('v-'+v).classList.add('on');
document.querySelectorAll('.tab,.sv').forEach(function(n){n.classList.toggle('on',n.getAttribute('data-v')===v)});
if(v!=='games')backToGames();}
document.querySelectorAll('[data-v]').forEach(function(n){n.onclick=function(){switchView(n.getAttribute('data-v'))}});
$('tgLb').onchange=function(e){$('uCard').classList.toggle('hidden',!e.target.checked);$('hidB').classList.toggle('hidden',e.target.checked);};
$('avSel').onchange=function(e){$('uName').textContent=e.target.value+' (أنت)';};
$('search').oninput=function(e){var q=norm(e.target.value);$('gGrid').querySelectorAll('[data-g]').forEach(function(c){c.style.display=norm(c.textContent).indexOf(q)>=0?'':'none';});};

var GS={s:0,t:0,x:0};
var GD=[{id:1,e:'🧮',n:'الحساب الذهني',xp:20},{id:2,e:'📜',n:'الآلة الزمنية',xp:25},{id:3,e:'⚛️',n:'تحدي الفيزياء',xp:20},{id:4,e:'🧠',n:'الذاكرة العلمية',xp:10},{id:5,e:'🔠',n:'فك المصطلحات',xp:20}];
$('gGrid').innerHTML=GD.map(function(g){return '<div data-g="'+g.id+'" class="fb-card p-3 cursor-pointer hover:shadow-md"><b class="text-[12px]">'+g.e+' '+g.n+'</b><p class="text-[9px] text-gray-500 mt-1">+'+g.xp+' XP لكل إجابة صحيحة ✅</p></div>';}).join('');
$('gGrid').onclick=function(e){var c=e.target.closest('[data-g]');if(c)goGame(+c.getAttribute('data-g'));};
function goGame(id){switchView('games');openGame(id);}
function backToGames(){$('gScreen').classList.add('hidden');$('gList').classList.remove('hidden');}
function openScreen(t){$('gList').classList.add('hidden');$('gScreen').classList.remove('hidden');$('gScreen').classList.add('flex');$('gsTitle').textContent=t;GS={s:0,t:0,x:0};$('gsScore').textContent='0';}
function win(n,ev){GS.s++;GS.x+=n;record(true);addXP(n,ev);sound('ok');$('gsScore').textContent=GS.s;}
function lose(){record(false);sound('no');updateUI();}
function end(){if(GS.t>1&&GS.s===GS.t){S.perfect++;toast('🏆 جولة مثالية!','ok');}
$('gsBody').innerHTML='<div class="text-5xl">'+(GS.s===GS.t?'🏆':(GS.s>=GS.t/2?'🎉':'💪'))+'</div><h3 class="font-black text-xl text-[#1877f2]">'+GS.s+'/'+GS.t+'</h3><p class="text-xs text-amber-600 font-bold mt-1">ربحت '+GS.x+' XP حقيقية</p><button onclick="backToGames()" class="fb-blue px-5 py-2 text-xs font-bold mt-2">العودة</button>';
act('🎮 جولة: '+GS.s+'/'+GS.t);updateUI();}
function optsHTML(o){return shuffle(o).map(function(x){return '<button data-o="'+x+'" class="obtn bg-[#f0f2f5] hover:bg-[#e4e6eb] p-2 rounded-lg text-[11px] font-bold">'+x+'</button>';}).join('');}
function bindOpts(box,fn){box.querySelectorAll('.obtn').forEach(function(b){b.onclick=function(ev){if(b.getAttribute('data-done'))return;fn(b,ev);};});}
function g1(){openScreen('🧮 الحساب الذهني');GS.t=8;var r=0;
function next(){if(r>=8)return end();r++;
var a=3+Math.floor(Math.random()*12),b=3+Math.floor(Math.random()*12),ans=a*b;
$('gsBody').innerHTML='<p class="text-[10px] text-gray-500">سؤال '+r+'/8</p><div class="text-3xl font-black text-[#1877f2] my-2">'+a+' × '+b+' = ؟</div><div class="flex gap-2 w-full max-w-xs"><input id="ans" type="number" class="fin flex-1 text-center"><button id="go" class="fb-blue px-4 text-xs font-bold">✓</button></div>';
$('ans').focus();
var go=function(ev){var v=parseInt($('ans').value);if(v===ans)win(20,ev);else lose();next();};
$('go').onclick=go;$('ans').onkeypress=function(e){if(e.key==='Enter')go(e)};}
next();}
var HIST=[{q:'عاصمة على الدجلة، مركز دار الحكمة',a:'بغداد',o:['بغداد','دمشق','القاهرة','قرطبة']},{q:'فتح الأندلس 711م',a:'طارق بن زياد',o:['طارق بن زياد','خالد بن الوليد','صلاح الدين','عمرو بن العاص']},{q:'أب الجبر',a:'الخوارزمي',o:['الخوارزمي','ابن سينا','الرازي','ابن الهيثم']},{q:'سقطت الأندلس عام',a:'1492',o:['1492','1453','1258','1187']},{q:'حضارة الأهرام',a:'المصريون القدماء',o:['المصريون القدماء','الرومان','الإغريق','الفرس']}];
var PHYS=[{q:'تسارع الجاذبية تقريباً؟',a:'9.8',o:['9.8','8.9','10.5','7.8']},{q:'وحدة الطاقة؟',a:'الجول',o:['الجول','النيوتن','الواط','الفولت']},{q:'F = ؟',a:'m×a',o:['m×a','m/a','m+a','a/m']},{q:'لكل فعل رد فعل مساوٍ ومعاكس؟',a:'الثالث',o:['الثالث','الأول','الثاني','الرابع']},{q:'سرعة الضوء تقريباً km/s؟',a:'300000',o:['300000','300','3000','150000']}];
function mcq(title,qs,xp){openScreen(title);GS.t=qs.length;var i=0;
function next(){if(i>=qs.length)return end();var q=qs[i++];
$('gsBody').innerHTML='<p class="text-[10px] text-gray-500">سؤال '+i+'/'+qs.length+'</p><p class="text-sm font-bold my-2">'+q.q+'</p><div class="grid grid-cols-2 gap-2 w-full max-w-sm">'+optsHTML(q.o)+'</div>';
bindOpts($('gsBody'),function(b,ev){if(b.getAttribute('data-o')===q.a){b.classList.add('ok');win(xp,ev);}else{b.classList.add('no');lose();}setTimeout(next,450);});}
next();}
var MEM=[['E=mc²','نسبية'],['F=ma','نيوتن'],['π≈3.14','دائرة'],['H₂O','ماء'],['NaCl','ملح'],['c=3×10⁸','ضوء']];
function g4(){openScreen('🧠 الذاكرة العلمية');GS.t=MEM.length;
var cards=shuffle(MEM.flatMap(function(p,i){return [{id:i,t:p[0]},{id:i,t:p[1]}]}));
var fl=[],done=0;
$('gsBody').innerHTML='<div class="grid grid-cols-4 gap-1.5 w-full max-w-md">'+cards.map(function(c){return '<div data-id="'+c.id+'" class="card3d h-16 cursor-pointer"><div class="in"><div class="f bg-[#1877f2] text-white font-black">؟</div><div class="b bg-white border-2 border-[#1877f2] text-[9px] font-bold">'+c.t+'</div></div></div>';}).join('')+'</div>';
$('gsBody').querySelectorAll('.card3d').forEach(function(cd){cd.onclick=function(ev){
if(cd.classList.contains('fl')||fl.length===2)return;
cd.classList.add('fl');fl.push(cd);
if(fl.length===2){var a=fl[0],b=fl[1];
if(a.getAttribute('data-id')===b.getAttribute('data-id')&&a!==b){a.style.opacity=.5;b.style.opacity=.5;fl=[];done++;win(10,ev);if(done===MEM.length){addXP(30,ev);setTimeout(end,500);}}
else setTimeout(function(){a.classList.remove('fl');b.classList.remove('fl');fl=[];lose();},650);}};});}
var WORDS=[{w:'جاذبية',h:'قوة تجذب الأجسام للأرض'},{w:'الكترون',h:'جسيم سالب بالذرة'},{w:'مجرة',h:'تجمع هائل من النجوم'}];
function g5(){openScreen('🔠 فك المصطلحات');GS.t=WORDS.length;var i=0;
function next(){if(i>=WORDS.length)return end();var p=WORDS[i++];var ans=[];var used=[];
$('gsBody').innerHTML='<p class="text-[10px] text-gray-500">تلميح: <span class="text-[#1877f2] font-bold">'+p.h+'</span></p><div id="slots" class="flex gap-1 justify-center min-h-10 my-2 flex-wrap"></div><div id="tls" class="flex gap-1 justify-center flex-wrap">'+shuffle(p.w.split('')).map(function(l){return '<div class="tile">'+l+'</div>';}).join('')+'</div><div class="flex gap-2 mt-2"><button id="und" class="fb-btn px-3 py-1.5 text-[10px] font-bold">تراجع</button><button id="chk" class="fb-blue px-4 py-1.5 text-[10px] font-bold">تحقق</button></div>';
function draw(){$('slots').innerHTML=ans.map(function(l){return '<div class="tile" style="background:#31a24c;border-color:#86efac">'+l+'</div>';}).join('');}
$('tls').querySelectorAll('.tile').forEach(function(t){t.onclick=function(){t.classList.add('used');used.push(t);ans.push(t.textContent);draw();};});
$('und').onclick=function(){if(used.length){used.pop().classList.remove('used');ans.pop();draw();}};
$('chk').onclick=function(ev){if(ans.join('')===p.w)win(20,ev);else lose();setTimeout(next,450);};}
next();}
function openGame(id){if(id===1)g1();else if(id===2)mcq('📜 الآلة الزمنية',HIST,25);else if(id===3)mcq('⚛️ الفيزياء',PHYS,20);else if(id===4)g4();else g5();}

/* ======= الدراسة ======= */
var studyData=null;
$('fileIn').onchange=async function(e){var f=e.target.files[0];if(!f)return;toast('📄 جارٍ تحليل الملف…');
var txt='',pages=1;
try{
if(f.name.indexOf('.pdf')>=0){var pdf=await pdfjsLib.getDocument({data:await f.arrayBuffer()}).promise;pages=pdf.numPages;
for(var i=1;i<=pages;i++){var pg=await pdf.getPage(i);var c=await pg.getTextContent();txt+=c.items.map(function(x){return x.str}).join(' ')+'\n';}}
else{txt=await f.text();}
buildStudy(txt,f.name,pages);S.file=1;addXP(30);toast('✅ تم التحليل! +30 XP','ok');
}catch(err){toast('⚠️ فشل قراءة الملف','no');}};
function buildStudy(txt,name,pages){var words=txt.split(/\s+/).filter(function(w){return w.length>2});
$('stName').textContent=name;$('stWords').textContent=words.length;$('stPages').textContent=pages;
var sents=txt.split(/[.!?؟\n]/).filter(function(s){return s.trim().length>20});
$('stSum').textContent=sents.slice(0,3).join('. ')||'النص قصير.';
var stop=['في','من','على','الى','عن','ان','هو','هي','و','ثم','او','لا','ما','لم','قد','مع','هذا','هذه','التي','الذي','كان','كانت','بعد','قبل','بين','حتى','اذا','كل','بعض','تم','يتم','حيث','عند','منذ','خلال','كما','ايضا','فقط','جدا'];
var freq={};words.forEach(function(w){var n=norm(w).replace(/[^\u0600-\u06FFa-zA-Z0-9]/g,'');if(n.length>3&&stop.indexOf(n)<0)freq[n]=(freq[n]||0)+1;});
var keys=Object.keys(freq).sort(function(a,b){return freq[b]-freq[a]}).slice(0,8);
$('stKeys').innerHTML=keys.map(function(k){return '<span class="bg-purple-100 text-purple-700 px-2 py-0.5 rounded-full text-[9px] font-bold">'+k+'</span>';}).join('')||'-';
$('stText').textContent=txt.substring(0,1500);
studyData={sents:sents,keys:keys};$('studyOut').classList.remove('hidden');}
function genQuiz(){if(!studyData||studyData.keys.length<4)return toast('حلل ملفاً أولاً','no');
var qs=studyData.sents.filter(function(s){return studyData.keys.some(function(k){return s.indexOf(k)>=0})}).slice(0,3);
$('studyTools').innerHTML=qs.map(function(s){var k=studyData.keys.find(function(x){return s.indexOf(x)>=0});
var others=shuffle(studyData.keys.filter(function(x){return x!==k})).slice(0,3);
return '<div class="fb-card p-3"><p class="text-[10px] font-bold mb-2">'+s.replace(k,'____')+'</p><div class="flex gap-1.5 flex-wrap">'+shuffle([k].concat(others)).map(function(o){return '<button data-o="'+o+'" data-a="'+k+'" class="obtn fb-btn px-3 py-1.5 text-[10px] font-bold">'+o+'</button>';}).join('')+'</div></div>';}).join('');
$('studyTools').querySelectorAll('.obtn').forEach(function(b){b.onclick=function(ev){if(b.getAttribute('data-done'))return;
b.parentElement.querySelectorAll('.obtn').forEach(function(x){x.setAttribute('data-done',1)});
if(b.getAttribute('data-o')===b.getAttribute('data-a')){b.classList.add('ok');record(true);addXP(15,ev);sound('ok');}else{b.classList.add('no');record(false);sound('no');updateUI();}};});
toast('📝 جاهز! أجب لتحصل النقاط','ok');}
function genCards(){if(!studyData)return toast('حلل ملفاً أولاً','no');
$('studyTools').innerHTML=studyData.sents.slice(0,4).map(function(s,i){var k=studyData.keys.find(function(x){return s.indexOf(x)>=0})||'؟';
return '<div class="card3d h-20 cursor-pointer"><div class="in"><div class="f bg-[#1877f2] text-white p-2 text-[10px] font-bold">'+s.substring(0,80)+'</div><div class="b bg-white border-2 border-amber-400 text-amber-600 font-black text-sm">'+k+'</div></div></div>';}).join('');
$('studyTools').querySelectorAll('.card3d').forEach(function(c){c.onclick=function(){c.classList.toggle('fl')};});}
var pomoT=null,pomoLeft=1500;
function pomoDraw(){var m=Math.floor(pomoLeft/60),s=pomoLeft%60;$('pomoTime').textContent=(m<10?'0':'')+m+':'+(s<10?'0':'')+s;}
function pomoStart(){if(pomoT)return;pomoT=setInterval(function(){pomoLeft--;pomoDraw();
if(pomoLeft<=0){pomoPause();S.pomo++;addXP(50);toast('🍅 جلسة كاملة! +50 XP','ok');sound('up');pomoLeft=1500;pomoDraw();}},1000);}
function pomoPause(){clearInterval(pomoT);pomoT=null;}
function pomoReset(){pomoPause();pomoLeft=1500;pomoDraw();}
function renderNotes(){$('noteList').innerHTML=S.notes.map(function(n,i){return '<div class="flex justify-between items-center bg-[#f0f2f5] p-1.5 rounded text-[10px]"><span>'+n+'</span><button onclick="delNote('+i+')" class="text-red-500 font-bold">✕</button></div>';}).join('');}
function addNote(){var v=$('noteIn').value.trim();if(!v)return;S.notes.unshift(v);$('noteIn').value='';renderNotes();save();}
function delNote(i){S.notes.splice(i,1);renderNotes();save();}

/* ======= المساعد العراقي ======= */
var KB=[
{k:['مرحبا','سلام','هلا','اهلا','هاي'],a:'هلا بيك يا غالي! شلونك؟ أني هسة بخدمتك، اسألني أي شيء وبجاوبك بسرعة البرق.'},
{k:['شلونك','كيفك','اخبارك'],a:'أني تمام الحمدلله، جاهز أجاوبك أربع وعشرين ساعة! شتريد تسأل اليوم؟'},
{k:['من انت','اسمك','من تكون'],a:'أني مساعدك الذكي، مثل صديقك اللي يفهم بكل شيء. أكدر أشرحلك دروس، أحاجيك، وأساعدك بدراستك.'},
{k:['نسبي'],a:'شوف، النسبية ببساطة: الوقت والمكان مرتبطين ببعض، والجاذبية مو قوة، هي انحناء بالزمان والمكان. ومعادلة أينشتاين الشهيرة: الطاقة تساوي الكتلة ضرب مربع سرعة الضوء.'},
{k:['نيوتن'],a:'قوانين نيوتن ثلاثة يا صديقي: الأول الجسم يبقى على حاله ما لم تؤثر عليه قوة، الثاني القوة تساوي الكتلة بالضرب التسارع، والثالث لكل فعل رد فعل مساويه بالاتجاه المعاكس.'},
{k:['مذاكر','خطة','ادرس','ذاكر'],a:'خليني أعطيك خطة زين: ذاكر خمس وعشرين دقيقة وارتاح خمس، وابتعد عن الهاتف، وراجع قبل النوم. جرب مؤقت بومودورو الموجود بقسم الدراسة، والله بتشوف الفرق!'},
{k:['مشتق','تفاضل'],a:'المشتقة يعني معدل التغيير. قاعدة سهلة بعد: أنزل الأس واضربه بالعدد، وبعدين طرح واحد من الأس. مثلا مشتقة أس ثلاثة تصير ثلاثة أس اثنين. جربها وشوف!'},
{k:['برمج','بايثون','كود'],a:'البرمجة هاي لغة نتحدث بيها مع الكمبيوتر. أبدأ ببايثون، سهلة مثل الكلام العادي، وبعدها تكدر تتعلم جافاسكريبت للويب. مستقبلها مضمون والله!'},
{k:['بغداد'],a:'بغداد الحبيبة! بنيت بعصر العباسيين وفيها بيت الحكمة، كانت أعظم مدينة علم بالعالم كله. عاصمة التاريخ والحضارة، الله يحفظها.'},
{k:['ضوئي','نبات'],a:'النباتات تسوي أكلها من الضوء والماء وثاني أوكسيد الكربون، وبنفس الوقت تعطيك أوكسيد تتنفسه. يعني مصنع مجاني يشتغل بضوء الشمس!'},
{k:['ثقب'],a:'الثقب الأسود منطقة بالفضاء جاذبيتها قوية مرة، حتى الضوء ما يكدر يطلع منها. شي مرعب بس مذهل بنفس الوقت!'},
{k:['نقط','اكس'],a:'النقاط ما تنعط ببلاش عندنا! لازم تجاوب صحيح بالألعاب والاختبارات حتى تجمعها، والكومبو يخليها تزيد أسرع.'},
{k:['شكر','يعطيك'],a:'العفو يا غالي! أي وقت تحتاجني أني هنا، لا تتأخر عني.'}];
function aiReply(t){var n=norm(t);for(var i=0;i<KB.length;i++){for(var j=0;j<KB[i].k.length;j++){if(n.indexOf(norm(KB[i].k[j]))>=0)return KB[i].a;}}
return 'سؤال حلو والله! جرب تسألني عن النسبية، نيوتن، البرمجة، بغداد، أو قلّي أريد خطة مذاكرة وأنطيها الك.';}
function cleanSpeak(s){return s.replace(/[^\u0600-\u06FF a-zA-Z0-9.,!?؟،]/g,' ');}
function speak(txt,cb){if(!('speechSynthesis' in window)){cb&&cb();return;}
speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(cleanSpeak(txt));u.lang='ar';u.rate=1.05;u.pitch=1.1;
var vs=speechSynthesis.getVoices();for(var i=0;i<vs.length;i++){if(vs[i].lang.indexOf('ar')===0){u.voice=vs[i];break;}}
u.onend=function(){cb&&cb();};speechSynthesis.speak(u);}
if('speechSynthesis' in window)speechSynthesis.getVoices();
function pushMsg(who,txt){var log=$('log');var d=document.createElement('div');
if(who==='u'){d.className='flex justify-end';d.innerHTML='<div class="bg-[#1877f2] text-white rounded-2xl rounded-bl-sm p-2.5 max-w-[80%] text-[11px]">'+txt+'</div>';}
else{d.innerHTML='<div class="flex gap-1.5 items-start"><span class="gem text-xl">✦</span><div class="fb-card p-2.5 max-w-[80%] text-[11px] leading-relaxed">'+txt+'</div></div>';}
log.appendChild(d);log.scrollTop=log.scrollHeight;return d;}
function aiThink(txt,then){pushMsg('u',txt);
var d=pushMsg('ai','<span class="text-gray-400">…</span>');
setTimeout(function(){var r=aiReply(txt);d.querySelector('div:last-child').textContent=r;
if(then)speak(r,then);},200);}
function sendMsg(){var v=$('inp').value.trim();if(!v)return;$('inp').value='';aiThink(v);}
$('inp').onkeypress=function(e){if(e.key==='Enter')sendMsg();};
function askChip(b){aiThink(b.textContent);}
var SR=window.SpeechRecognition||window.webkitSpeechRecognition;
var rec=null,inCall=false,listening=false;
if(SR){rec=new SR();rec.lang='ar';
rec.onresult=function(e){listening=false;var t=e.results[0][0].transcript;S.voice++;updateUI();
if(inCall){$('ovT').textContent='قلت: '+t;$('ovSt').textContent='الروبوت يحكي…';$('ovW').classList.add('hidden');
pushMsg('u','🎙️ '+t);var r=aiReply(t);setTimeout(function(){pushMsg('ai',r);speak(r,function(){if(inCall)listen();});},150);}
else{$('inp').value=t;sendMsg();}};
rec.onerror=function(){listening=false;if(inCall){$('ovSt').textContent='ما سمعتك زين، تكلم مرة ثانية';listen();}else toast('⚠️ اسمح بالمايكروفون','no');};}
function listen(){if(!rec||listening)return;try{listening=true;rec.start();
if(inCall){$('ovSt').textContent='اسمعك الآن… تكلم 🎙️';$('ovW').classList.remove('hidden');}}catch(e){}}
function micOnce(){if(!SR)return toast('⚠️ استخدم متصفح كروم','no');toast('🎙️ تكلم الآن');listen();}
function startCall(){if(!SR)return toast('⚠️ استخدم متصفح كروم','no');
inCall=true;$('ov').classList.remove('hidden');$('ovT').textContent='';sound('ok');
setTimeout(function(){speak('هلا بيك! أني مساعدك الذكي، تكلم الآن وأنی أسمعك.',function(){if(inCall)listen();});},300);}
function endCall(){inCall=false;listening=false;if(rec)try{rec.stop()}catch(e){}
if('speechSynthesis' in window)speechSynthesis.cancel();
$('ov').classList.add('hidden');toast('📴 انتهت المكالمة');}

pomoDraw();renderNotes();updateUI();
pushMsg('ai','هلا وسهلين! 🤖 أني مساعدك الذكي بلهجتنا العراقية. اضغط 📞 وخلينا نحجي مثل الأصحاب، أو اكتب سؤالك تحت.');
</script>
</body>
</html>
"""

components.html(HTML, height=950, scrolling=True)
