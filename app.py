import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="الأكاديمية الذكية", page_icon="🎓", layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>#MainMenu,footer,header{display:none}.stApp{background:#030712}.block-container{max-width:100%!important;padding:0!important}</style>", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://cdn.tailwindcss.com"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
*{font-family:'Tajawal',sans-serif;box-sizing:border-box}
body{background:#030712;color:#f9fafb;margin:0}
.view{display:none}.view.on{display:flex;animation:vin .3s}
@keyframes vin{from{opacity:0;transform:translateY(10px)}to{opacity:1}}
.card{background:rgba(31,41,55,.6);border:1px solid rgba(255,255,255,.07);transition:.2s}
.card:hover{border-color:rgba(59,130,246,.5)}
.btn{background:rgba(59,130,246,.15);border:1px solid rgba(59,130,246,.35);cursor:pointer;transition:.15s}
.btn:hover{background:rgba(59,130,246,.35)}.btn:active{transform:scale(.95)}
.navb{cursor:pointer;border:1px solid transparent;transition:.15s}
.navb.on{background:rgba(59,130,246,.2);border-color:rgba(59,130,246,.4)}
.grad{background:linear-gradient(90deg,#3b82f6,#a855f7,#ec4899);-webkit-background-clip:text;color:transparent}
.xpf{position:fixed;pointer-events:none;font-weight:900;font-size:22px;color:#fbbf24;text-shadow:0 0 16px rgba(251,191,36,.8);animation:fu 1.3s forwards;z-index:999}
@keyframes fu{to{opacity:0;transform:translateY(-70px) scale(1.4)}}
.toast{animation:ti .3s}@keyframes ti{from{transform:translateX(100%)}to{transform:none}}
.card3d{perspective:900px}.card3d .in{position:relative;width:100%;height:100%;transition:transform .5s;transform-style:preserve-3d}
.card3d.fl .in{transform:rotateY(180deg)}
.card3d .f,.card3d .b{position:absolute;inset:0;backface-visibility:hidden;border-radius:10px;display:flex;align-items:center;justify-content:center;text-align:center;padding:4px}
.card3d .b{transform:rotateY(180deg)}
.tile{width:42px;height:42px;display:flex;align-items:center;justify-content:center;background:#1e40af;border:2px solid #60a5fa;border-radius:8px;font-weight:900;font-size:17px;cursor:pointer;user-select:none}
.tile.used{opacity:.25;pointer-events:none}
.ok{background:rgba(16,185,129,.3)!important;border-color:#10b981!important}
.no{background:rgba(244,63,94,.3)!important;border-color:#f43f5e!important}
.pbar{transition:width .5s}
.callav{animation:av 2s infinite}@keyframes av{0%{box-shadow:0 0 0 0 rgba(34,197,94,.6)}70%{box-shadow:0 0 0 28px rgba(34,197,94,0)}100%{box-shadow:0 0 0 0 rgba(34,197,94,0)}}
.wave{display:flex;gap:3px;align-items:flex-end;height:24px}
.wave i{width:4px;background:#22c55e;border-radius:4px;animation:wv 1s infinite}
.wave i:nth-child(2){animation-delay:.15s}.wave i:nth-child(3){animation-delay:.3s}.wave i:nth-child(4){animation-delay:.45s}.wave i:nth-child(5){animation-delay:.6s}
@keyframes wv{0%,100%{height:5px}50%{height:22px}}
.tg{background:linear-gradient(135deg,rgba(0,136,204,.3),rgba(36,169,220,.35));border:1px solid rgba(36,169,220,.5)}
.tg:hover{box-shadow:0 0 18px rgba(36,169,220,.6)}
</style>
</head>
<body>
<div id="toasts" class="fixed top-3 right-3 z-50 flex flex-col gap-2"></div>

<div class="h-screen flex flex-col max-w-6xl mx-auto p-2 gap-2">

<header class="card rounded-xl p-2.5 flex items-center justify-between flex-wrap gap-2">
  <div class="flex items-center gap-2"><span class="text-2xl">🎓</span><div><h1 class="font-black text-sm grad">الأكاديمية الذكية الشاملة</h1><p class="text-[10px] text-gray-400">تعلّم • تحدَّ • تحدث مع الذكاء</p></div></div>
  <div class="flex items-center gap-1.5 flex-wrap text-[10px] font-bold">
    <span class="bg-amber-500/10 border border-amber-500/30 px-2 py-1 rounded">🔥 <b id="stV">1</b></span>
    <span class="bg-purple-500/10 border border-purple-500/30 px-2 py-1 rounded">⚡ x<b id="cbV">0</b></span>
    <span class="bg-amber-500/10 border border-amber-500/30 px-2 py-1 rounded">🏆 <b id="xpV">0</b></span>
    <span class="bg-blue-500/10 border border-blue-500/30 px-2 py-1 rounded">مستوى <b id="lvV">1</b></span>
    <a href="https://t.me/m3v30" target="_blank" class="tg px-2.5 py-1 rounded text-cyan-100">📨 الدعم @m3v30</a>
  </div>
</header>

<div class="flex-1 flex gap-2 overflow-hidden">

<nav class="w-14 md:w-40 card rounded-xl p-1.5 flex flex-col gap-1">
  <div data-v="home" class="navb on p-2 rounded-lg text-center md:text-right text-[11px] font-bold">🏠<span class="hidden md:inline"> الرئيسية</span></div>
  <div data-v="games" class="navb p-2 rounded-lg text-center md:text-right text-[11px] font-bold">🎮<span class="hidden md:inline"> الألعاب</span></div>
  <div data-v="ai" class="navb p-2 rounded-lg text-center md:text-right text-[11px] font-bold">🤖<span class="hidden md:inline"> المساعد الصوتي</span></div>
  <div data-v="badges" class="navb p-2 rounded-lg text-center md:text-right text-[11px] font-bold">🏅<span class="hidden md:inline"> الإنجازات</span></div>
  <div data-v="board" class="navb p-2 rounded-lg text-center md:text-right text-[11px] font-bold">🏆<span class="hidden md:inline"> التصنيف</span></div>
</nav>

<main class="flex-1 card rounded-xl p-3 overflow-hidden">

<section id="v-home" class="view on flex-col gap-2 h-full overflow-y-auto">
  <div class="grid grid-cols-2 lg:grid-cols-4 gap-2">
    <div class="card p-2.5 rounded-lg"><p class="text-[9px] text-gray-400">النقاط</p><b id="hXP" class="text-blue-400">0</b></div>
    <div class="card p-2.5 rounded-lg"><p class="text-[9px] text-gray-400">إجابات صحيحة</p><b id="hCor" class="text-emerald-400">0</b></div>
    <div class="card p-2.5 rounded-lg"><p class="text-[9px] text-gray-400">الدقة</p><b id="hAcc" class="text-amber-400">0%</b></div>
    <div class="card p-2.5 rounded-lg"><p class="text-[9px] text-gray-400">الإنجازات</p><b id="hBdg" class="text-yellow-400">0</b></div>
  </div>
  <div class="card p-3 rounded-xl border border-purple-500/30">
    <h3 class="font-black text-xs text-amber-200 mb-1">☀️ تحدي اليوم</h3>
    <p class="text-[10px] text-gray-300 mb-2">أكمل 3 جولات حقيقية = 200 XP</p>
    <div class="flex items-center gap-2"><div class="flex-1 h-1.5 bg-gray-800 rounded-full"><div id="dBar" class="pbar h-full bg-gradient-to-r from-amber-500 to-pink-500" style="width:0%"></div></div><span id="dTxt" class="text-[9px] text-gray-400">0/3</span></div>
  </div>
  <div class="grid grid-cols-2 gap-2">
    <button onclick="switchView('ai')" class="btn p-3 rounded-xl text-[11px] font-bold text-emerald-300">🤖 تحدث مع الروبوت الصوتي</button>
    <button onclick="switchView('games')" class="btn p-3 rounded-xl text-[11px] font-bold text-amber-300">🎮 العب واكسب نقاطاً</button>
  </div>
</section>

<section id="v-games" class="view flex-col gap-2 h-full">
  <div id="gList" class="flex-1 overflow-y-auto">
    <h2 class="font-black text-sm text-amber-300 mb-2">🎮 ساحة التحديات — نقاط فقط للإجابات الصحيحة</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2" id="gGrid"></div>
  </div>
  <div id="gScreen" class="hidden flex-1 flex-col overflow-y-auto">
    <div class="flex items-center justify-between bg-gray-900 p-2 rounded-lg mb-2">
      <button onclick="backToGames()" class="bg-gray-800 px-2 py-1 rounded text-[10px]">→ رجوع</button>
      <b id="gsTitle" class="text-xs text-amber-400"></b>
      <span class="text-[10px]">النقاط: <b id="gsScore" class="text-amber-400">0</b></span>
    </div>
    <div id="gsBody" class="flex-1 flex flex-col items-center justify-center gap-3 text-center p-2"></div>
  </div>
</section>

<section id="v-ai" class="view flex-col gap-2 h-full">
  <div class="bg-gray-900 p-2 rounded-lg flex items-center justify-between">
    <div class="flex items-center gap-2"><span class="text-xl">🤖</span><div><b class="text-xs text-emerald-300">الروبوت الذكي</b><p id="aiSt" class="text-[9px] text-gray-400">جاهز نصياً وصوتياً</p></div></div>
    <button id="callB" class="btn px-3 py-1.5 rounded-lg text-[10px] font-bold text-emerald-300">📞 اتصال صوتي</button>
  </div>
  <div id="log" class="flex-1 overflow-y-auto space-y-2 p-2 bg-gray-950 rounded-xl"></div>
  <div class="flex gap-1.5 bg-gray-900 p-1.5 rounded-xl">
    <button id="micB" class="btn p-2 rounded-lg">🎙️</button>
    <input id="inp" class="flex-1 bg-transparent px-2 text-xs focus:outline-none" placeholder="اكتب أو اضغط المايك وتحدث…">
    <button id="sendB" class="btn px-4 py-2 rounded-lg text-[10px] font-bold bg-blue-600 text-white">إرسال</button>
  </div>
</section>

<section id="v-badges" class="view flex-col gap-2 h-full overflow-y-auto">
  <h2 class="font-black text-sm text-yellow-300">🏅 إنجازات تُفتح بالأداء الحقيقي فقط</h2>
  <div id="bGrid" class="grid grid-cols-2 sm:grid-cols-3 gap-2"></div>
</section>

<section id="v-board" class="view flex-col gap-2 h-full overflow-y-auto">
  <div class="card p-2.5 rounded-xl flex items-center justify-between flex-wrap gap-2">
    <b class="text-xs text-purple-200">️ الخصوصية والهوية</b>
    <div class="flex items-center gap-2">
      <label class="text-[9px]">الظهور <input type="checkbox" id="tgLb" checked class="accent-purple-500"></label>
      <select id="avSel" class="bg-gray-800 text-[9px] p-1 rounded border border-purple-500/40">
        <option>الفيزيائي المجهول ⚛️</option><option>المحقق التاريخي 📜</option><option>عبقري الخوارزميات 💻</option><option>مكتشف المجرات 🌌</option>
      </select>
    </div>
  </div>
  <div class="flex justify-between bg-amber-500/10 border border-amber-500/30 p-2 rounded-lg text-[10px]"><span>🥇 الراحل عبر الزمن ⏳</span><b class="text-amber-300">3,450 XP</b></div>
  <div class="flex justify-between bg-gray-800 p-2 rounded-lg text-[10px]"><span>🥈 صانع المعادلات 🧮</span><b>2,980 XP</b></div>
  <div id="uCard" class="flex justify-between bg-blue-600/20 border border-blue-500/50 p-2 rounded-lg text-[10px]"><span id="uName">الفيزيائي المجهول ⚛️ (أنت)</span><b id="uXP" class="text-blue-300">0 XP</b></div>
  <div id="hidB" class="hidden p-4 text-center bg-gray-950 rounded-lg border border-dashed border-gray-800 text-[10px] text-gray-400">️ وضع الخصوصية — نقاطك محلية فقط</div>
</section>

</main>
</div>
</div>

<a href="https://t.me/m3v30" target="_blank" class="fixed bottom-4 left-4 z-40 w-12 h-12 rounded-full tg flex items-center justify-center text-xl callav">📨</a>

<div id="ov" class="hidden fixed inset-0 bg-black/90 z-50 flex flex-col items-center justify-center gap-3">
  <div class="w-24 h-24 rounded-full bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center text-4xl callav">🤖</div>
  <b class="text-white">الروبوت الذكي</b>
  <p id="ovSt" class="text-xs text-emerald-300">جارٍ الاتصال…</p>
  <div id="ovW" class="wave hidden"><i></i><i></i><i></i><i></i><i></i></div>
  <p id="ovT" class="text-xs text-gray-300 max-w-xs text-center min-h-5 px-4"></p>
  <button id="endB" class="bg-rose-600 px-6 py-2 rounded-full text-sm font-bold text-white">📴 إنهاء</button>
</div>

<script>
var $=function(id){return document.getElementById(id)};
function shuffle(a){return a.slice().sort(function(){return Math.random()-.5})}
function pick(a){return a[Math.floor(Math.random()*a.length)]}
function norm(s){return (s||'').replace(/[أإآ]/g,'ا').replace(/ة/g,'ه').replace(/ى/g,'ي').trim()}
var S={xp:0,correct:0,total:0,combo:0,best:0,streak:1,daily:0,badges:[],sound:true,perfect:0,voice:0};
try{var d=localStorage.getItem('acad5');if(d)S=Object.assign(S,JSON.parse(d));}catch(e){}
function save(){try{localStorage.setItem('acad5',JSON.stringify(S))}catch(e){}}
function toast(m,t){var c=t==='ok'?'border-emerald-500':(t==='no'?'border-rose-500':'border-blue-500');
var d=document.createElement('div');d.className='toast px-3 py-2 rounded-lg border-2 bg-gray-900/95 text-[11px] font-bold '+c;d.textContent=m;
$('toasts').appendChild(d);setTimeout(function(){d.remove()},2600);}
function sound(t){if(!S.sound)return;try{var c=new (window.AudioContext||window.webkitAudioContext)();var o=c.createOscillator();var g=c.createGain();
o.connect(g);g.connect(c.destination);g.gain.setValueAtTime(.08,c.currentTime);
var f=t==='ok'?[880,1100]:(t==='no'?[300,200]:[523,659,784]);
f.forEach(function(x,i){o.frequency.setValueAtTime(x,c.currentTime+i*.08)});
g.gain.exponentialRampToValueAtTime(.01,c.currentTime+.3);o.start();o.stop(c.currentTime+.3);}catch(e){}}
function floatXP(n,ev){if(!ev)return;var d=document.createElement('div');d.className='xpf';d.textContent='+'+n;d.style.left=ev.clientX+'px';d.style.top=ev.clientY+'px';document.body.appendChild(d);setTimeout(function(){d.remove()},1300);}
function record(ok){S.total++;if(ok){S.correct++;S.combo++;if(S.combo>S.best)S.best=S.combo;}else S.combo=0;}
function addXP(n,ev){S.xp+=n;floatXP(n,ev);S.daily++;
if(S.daily===3){S.xp+=200;toast('☀️ تحدي اليوم اكتمل! +200','ok');sound('up');}
updateUI();}
function updateUI(){$('xpV').textContent=S.xp;$('stV').textContent=S.streak;$('cbV').textContent=S.combo;
$('lvV').textContent=Math.floor(S.xp/500)+1;
$('hXP').textContent=S.xp;$('hCor').textContent=S.correct;
$('hAcc').textContent=(S.total?Math.round(S.correct/S.total*100):0)+'%';
$('hBdg').textContent=S.badges.length;
$('dBar').style.width=Math.min(100,S.daily/3*100)+'%';$('dTxt').textContent=Math.min(3,S.daily)+'/3';
$('uXP').textContent=S.xp+' XP';
save();checkBadges();}
var BADGES=[
{id:'b1',i:'🎯',t:'أول إصابة',d:'إجابة صحيحة',c:function(){return S.correct>=1}},
{id:'b2',i:'🧠',t:'عقل حاد',d:'25 صحيحة',c:function(){return S.correct>=25}},
{id:'b3',i:'🔥',t:'سلسلة x5',d:'كومبو 5',c:function(){return S.best>=5}},
{id:'b4',i:'💎',t:'جامع النقاط',d:'1000 XP',c:function(){return S.xp>=1000}},
{id:'b5',i:'🏅',t:'علامة كاملة',d:'جولة مثالية',c:function(){return S.perfect>=1}},
{id:'b6',i:'🎙️',t:'متحدث بارع',d:'تحدث صوتياً',c:function(){return S.voice>=1}}];
function checkBadges(){BADGES.forEach(function(b){if(S.badges.indexOf(b.id)<0&&b.c()){S.badges.push(b.id);toast('🏅 إنجاز: '+b.t,'ok');sound('up');}});renderBadges();}
function renderBadges(){$('bGrid').innerHTML=BADGES.map(function(b){var u=S.badges.indexOf(b.id)>=0;
return '<div class="card p-3 rounded-xl '+(u?'border-yellow-500/50':'opacity-50')+'"><div class="text-2xl">'+(u?b.i:'🔒')+'</div><b class="text-[10px]">'+b.t+'</b><p class="text-[9px] text-gray-400">'+b.d+'</p></div>';}).join('');}
function switchView(v){document.querySelectorAll('.view').forEach(function(x){x.classList.remove('on')});
$('v-'+v).classList.add('on');
document.querySelectorAll('.navb').forEach(function(n){n.classList.toggle('on',n.getAttribute('data-v')===v)});
if(v!=='games')backToGames();}
document.querySelectorAll('.navb').forEach(function(n){n.onclick=function(){switchView(n.getAttribute('data-v'))}});
$('tgLb').onchange=function(e){$('uCard').classList.toggle('hidden',!e.target.checked);$('hidB').classList.toggle('hidden',e.target.checked);};
$('avSel').onchange=function(e){$('uName').textContent=e.target.value+' (أنت)';};

var GS={s:0,t:0,x:0};
var GD=[{id:1,e:'🧮',n:'الحساب الذهني',xp:20},{id:2,e:'📜',n:'الآلة الزمنية',xp:25},{id:3,e:'⚛️',n:'تحدي الفيزياء',xp:20},{id:4,e:'🧠',n:'الذاكرة العلمية',xp:10},{id:5,e:'🔠',n:'فك المصطلحات',xp:20}];
$('gGrid').innerHTML=GD.map(function(g){return '<div data-g="'+g.id+'" class="card p-3 rounded-xl cursor-pointer"><b class="text-[11px]">'+g.e+' '+g.n+'</b><p class="text-[9px] text-gray-400 mt-1">+'+g.xp+' XP لكل إجابة صحيحة</p></div>';}).join('');
$('gGrid').onclick=function(e){var c=e.target.closest('[data-g]');if(c)openGame(+c.getAttribute('data-g'));};
function backToGames(){$('gScreen').classList.add('hidden');$('gList').classList.remove('hidden');}
function openScreen(t){$('gList').classList.add('hidden');$('gScreen').classList.remove('hidden');$('gScreen').classList.add('flex');$('gsTitle').textContent=t;GS={s:0,t:0,x:0};$('gsScore').textContent='0';}
function win(n,ev){GS.s++;GS.x+=n;record(true);addXP(n,ev);sound('ok');$('gsScore').textContent=GS.s;}
function lose(){record(false);sound('no');updateUI();}
function end(){if(GS.t>1&&GS.s===GS.t){S.perfect++;toast('🏆 جولة مثالية!','ok');}
$('gsBody').innerHTML='<div class="text-5xl">'+(GS.s===GS.t?'🏆':(GS.s>=GS.t/2?'🎉':'💪'))+'</div><h3 class="font-black text-lg grad">'+GS.s+'/'+GS.t+'</h3><p class="text-xs text-amber-400 font-bold mt-1">ربحت '+GS.x+' XP حقيقية</p><button onclick="backToGames()" class="btn px-4 py-2 rounded-lg text-xs font-bold mt-2">العودة</button>';
updateUI();}
function optsHTML(o){return shuffle(o).map(function(x){return '<button data-o="'+x+'" class="obtn bg-gray-900 border border-gray-700 p-2 rounded-lg text-[11px]">'+x+'</button>';}).join('');}
function bindOpts(box,fn){box.querySelectorAll('.obtn').forEach(function(b){b.onclick=function(ev){if(b.getAttribute('data-done'))return;fn(b,ev);};});}

function g1(){openScreen('🧮 الحساب الذهني');GS.t=8;var r=0;
function next(){if(r>=8)return end();r++;
var a=3+Math.floor(Math.random()*12),b=3+Math.floor(Math.random()*12),ans=a*b;
$('gsBody').innerHTML='<p class="text-[10px] text-gray-400">سؤال '+r+'/8</p><div class="text-3xl font-black text-amber-300 my-2">'+a+' × '+b+' = ؟</div><div class="flex gap-2 w-full max-w-xs"><input id="ans" type="number" class="flex-1 bg-gray-900 border border-gray-700 rounded-lg p-2 text-center text-sm"><button id="go" class="btn px-4 rounded-lg text-xs font-bold bg-amber-600 text-white">✓</button></div>';
$('ans').focus();
var go=function(ev){var v=parseInt($('ans').value);if(v===ans)win(20,ev);else lose();next();};
$('go').onclick=go;$('ans').onkeypress=function(e){if(e.key==='Enter')go(e)};}
next();}

var HIST=[{q:'عاصمة على الدجلة، مركز دار الحكمة',a:'بغداد',o:['بغداد','دمشق','القاهرة','قرطبة']},{q:'فتح الأندلس 711م',a:'طارق بن زياد',o:['طارق بن زياد','خالد بن الوليد','صلاح الدين','عمرو بن العاص']},{q:'أب الجبر',a:'الخوارزمي',o:['الخوارزمي','ابن سينا','الرازي','ابن الهيثم']},{q:'سقطت الأندلس عام',a:'1492',o:['1492','1453','1258','1187']},{q:'حضارة الأهرام',a:'المصريون القدماء',o:['المصريون القدماء','الرومان','الإغريق','الفرس']}];
var PHYS=[{q:'تسارع الجاذبية تقريباً؟',a:'9.8',o:['9.8','8.9','10.5','7.8']},{q:'وحدة الطاقة؟',a:'الجول',o:['الجول','النيوتن','الواط','الفولت']},{q:'F = ؟',a:'m×a',o:['m×a','m/a','m+a','a/m']},{q:'لكل فعل رد فعل مساوٍ ومعاكس؟',a:'الثالث',o:['الثالث','الأول','الثاني','الرابع']},{q:'سرعة الضوء تقريباً (km/s)؟',a:'300000',o:['300000','300','3000','150000']}];
function mcq(title,qs,xp){openScreen(title);GS.t=qs.length;var i=0;
function next(){if(i>=qs.length)return end();var q=qs[i++];
$('gsBody').innerHTML='<p class="text-[10px] text-gray-400">سؤال '+i+'/'+qs.length+'</p><p class="text-sm my-2">'+q.q+'</p><div class="grid grid-cols-2 gap-2 w-full max-w-sm">'+optsHTML(q.o)+'</div>';
bindOpts($('gsBody'),function(b,ev){if(b.getAttribute('data-o')===q.a){b.classList.add('ok');win(xp,ev);}else{b.classList.add('no');lose();}setTimeout(next,500);});}
next();}

var MEM=[['E=mc²','نسبية'],['F=ma','نيوتن'],['π≈3.14','دائرة'],['H₂O','ماء'],['NaCl','ملح'],['c=3×10⁸','ضوء']];
function g4(){openScreen('🧠 الذاكرة العلمية');GS.t=MEM.length;
var cards=shuffle(MEM.flatMap(function(p,i){return [{id:i,t:p[0]},{id:i,t:p[1]}]}));
var fl=[],done=0;
$('gsBody').innerHTML='<div class="grid grid-cols-4 gap-1.5 w-full max-w-md">'+cards.map(function(c,i){return '<div data-i="'+i+'" data-id="'+c.id+'" class="card3d h-16 cursor-pointer"><div class="in"><div class="f bg-gradient-to-br from-pink-600 to-purple-600 font-black">؟</div><div class="b bg-gray-800 border-2 border-pink-500 text-[9px]">'+c.t+'</div></div></div>';}).join('')+'</div>';
$('gsBody').querySelectorAll('.card3d').forEach(function(cd){cd.onclick=function(ev){
if(cd.classList.contains('fl')||fl.length===2)return;
cd.classList.add('fl');fl.push(cd);
if(fl.length===2){var a=fl[0],b=fl[1];
if(a.getAttribute('data-id')===b.getAttribute('data-id')&&a!==b){a.style.opacity=.5;b.style.opacity=.5;fl=[];done++;win(10,ev);if(done===MEM.length){addXP(30,ev);setTimeout(end,500);}}
else setTimeout(function(){a.classList.remove('fl');b.classList.remove('fl');fl=[];lose();},700);}};});}

var WORDS=[{w:'جاذبية',h:'قوة تجذب الأجسام للأرض'},{w:'الكترون',h:'جسيم سالب في الذرة'},{w:'مجرة',h:'تجمع هائل من النجوم'}];
function g5(){openScreen('🔠 فك المصطلحات');GS.t=WORDS.length;var i=0;
function next(){if(i>=WORDS.length)return end();var p=WORDS[i++];var ans=[];var used=[];
$('gsBody').innerHTML='<p class="text-[10px] text-gray-400">تلميح: <span class="text-amber-300">'+p.h+'</span></p><div id="slots" class="flex gap-1 justify-center min-h-10 my-2 flex-wrap"></div><div id="tls" class="flex gap-1 justify-center flex-wrap">'+shuffle(p.w.split('')).map(function(l){return '<div class="tile">'+l+'</div>';}).join('')+'</div><div class="flex gap-2 mt-2"><button id="und" class="btn px-3 py-1.5 rounded-lg text-[10px]">تراجع</button><button id="chk" class="btn px-4 py-1.5 rounded-lg text-[10px] font-bold bg-rose-600 text-white">تحقق</button></div>';
function draw(){$('slots').innerHTML=ans.map(function(l){return '<div class="tile" style="background:#047857">'+l+'</div>';}).join('');}
$('tls').querySelectorAll('.tile').forEach(function(t){t.onclick=function(){t.classList.add('used');used.push(t);ans.push(t.textContent);draw();};});
$('und').onclick=function(){if(used.length){used.pop().classList.remove('used');ans.pop();draw();}};
$('chk').onclick=function(ev){if(ans.join('')===p.w)win(20,ev);else lose();setTimeout(next,500);};}
next();}

function openGame(id){if(id===1)g1();else if(id===2)mcq('📜 الآلة الزمنية',HIST,25);else if(id===3)mcq('⚛️ الفيزياء',PHYS,20);else if(id===4)g4();else g5();}

var KB=[
{k:['مرحبا','سلام','اهلا','هلا'],a:'أهلاً بك! أنا روبوتك الذكي، تحدث معي بالمايك وسأجيبك صوتياً.'},
{k:['من انت','اسمك'],a:'أنا مساعد الأكاديمية الذكي، أجيبك نصياً وصوتياً مثل مكالمة حقيقية.'},
{k:['نسبي'],a:'نظرية أينشتاين تقول إن الزمان والمكان مرتبطان، والجاذبية انحناء في الزمكان.'},
{k:['نيوتن'],a:'قوانين نيوتن ثلاثة، أشهرها القوة تساوي الكتلة في التسارع.'},
{k:['ذكاء اصطناعي','الذكاء'],a:'الذكاء الاصطناعي هو جعل الآلات تتعلم وتفكر، كالمساعدات الصوتية.'},
{k:['برمج','بايثون','كود'],a:'البرمجة كتابة أوامر للحاسوب، وأنصحك بالبدء ببايثون لسهولتها.'},
{k:['ضوئي','نبات'],a:'البناء الضوئي تحويل الضوء والماء إلى غذاء وأكسجين في النباتات.'},
{k:['ثقب'],a:'الثقب الأسود منطقة جاذبيتها هائلة حتى الضوء لا يهرب منها.'},
{k:['ذاكر','مذاكر','نصيح'],a:'نصيحتي: خمس وعشرون دقيقة تركيز ثم خمس راحة، واختبر نفسك دائماً.'},
{k:['شكر'],a:'العفو! أنا هنا دائماً لخدمتك.'}];
function aiReply(t){var n=norm(t);for(var i=0;i<KB.length;i++){for(var j=0;j<KB[i].k.length;j++){if(n.indexOf(norm(KB[i].k[j]))>=0)return KB[i].a;}}
return 'سؤال جميل! اسألني عن النسبية، نيوتن، البرمجة، البناء الضوئي، أو نصائح المذاكرة.';}
function cleanSpeak(s){return s.replace(/[^\u0600-\u06FF a-zA-Z0-9.,!?؟،]/g,' ');}
var speaking=false;
function speak(txt,cb){if(!('speechSynthesis' in window)){cb&&cb();return;}
speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(cleanSpeak(txt));u.lang='ar-SA';
var vs=speechSynthesis.getVoices();for(var i=0;i<vs.length;i++){if(vs[i].lang.indexOf('ar')===0){u.voice=vs[i];break;}}
u.onend=function(){speaking=false;cb&&cb();};speaking=true;speechSynthesis.speak(u);}
function pushMsg(who,txt){var log=$('log');var d=document.createElement('div');
if(who==='u'){d.className='flex justify-end';d.innerHTML='<div class="bg-blue-600 text-white rounded-xl p-2.5 max-w-[80%] text-[11px]">'+txt+'</div>';}
else{d.innerHTML='<div class="flex gap-1.5"><span class="text-lg">🤖</span><div class="bg-gray-900 border border-gray-800 rounded-xl p-2.5 max-w-[80%] text-[11px] leading-relaxed">'+txt+'</div></div>';}
log.appendChild(d);log.scrollTop=log.scrollHeight;return d;}
function aiThink(txt,thenSpeak){pushMsg('u',txt);
var d=pushMsg('ai','…');
setTimeout(function(){var r=aiReply(txt);d.querySelector('div:last-child').textContent=r;
if(thenSpeak)speak(r,thenSpeak);},500);}
$('sendB').onclick=function(){var v=$('inp').value.trim();if(!v)return;$('inp').value='';aiThink(v);};
$('inp').onkeypress=function(e){if(e.key==='Enter')$('sendB').onclick();};
var SR=window.SpeechRecognition||window.webkitSpeechRecognition;
var rec=null,inCall=false,listening=false;
if(SR){rec=new SR();rec.lang='ar-SA';
rec.onresult=function(e){listening=false;var t=e.results[0][0].transcript;S.voice++;updateUI();
if(inCall){$('ovT').textContent='قلت: '+t;$('ovSt').textContent='الروبوت يتحدث…';$('ovW').classList.add('hidden');
pushMsg('u','🎙️ '+t);var r=aiReply(t);setTimeout(function(){pushMsg('ai',r);speak(r,function(){if(inCall)listen();});},400);}
else{$('inp').value=t;$('sendB').onclick();}};
rec.onerror=function(){listening=false;if(inCall){$('ovSt').textContent='تحدث بوضوح…';listen();}else toast('⚠️ اسمح بالمايكروفون','no');};}
function listen(){if(!rec||listening)return;try{listening=true;rec.start();
if(inCall){$('ovSt').textContent='أسمعك الآن… 🎙️';$('ovW').classList.remove('hidden');}}catch(e){}}
$('micB').onclick=function(){if(!SR)return toast('⚠️ استخدم متصفح Chrome','no');toast('🎙️ تحدث الآن','');listen();};
$('callB').onclick=function(){if(!SR)return toast('⚠️ استخدم متصفح Chrome','no');
inCall=true;$('ov').classList.remove('hidden');$('ovT').textContent='';sound('ok');
setTimeout(function(){speak('مرحباً! أنا روبوتك الذكي، تحدث الآن.',function(){if(inCall)listen();});},500);};
$('endB').onclick=function(){inCall=false;listening=false;if(rec)try{rec.stop()}catch(e){}
if('speechSynthesis' in window)speechSynthesis.cancel();
$('ov').classList.add('hidden');toast('📴 انتهت المكالمة','');};

updateUI();renderBadges();
pushMsg('ai','مرحباً! 🤖 اضغط "اتصال صوتي" وتحدث معي كأنه اتصال حقيقي، أو اكتب سؤالك هنا.');
</script>
</body>
</html>
"""

components.html(HTML, height=950, scrolling=True)
