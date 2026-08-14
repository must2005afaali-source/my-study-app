<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>أكاديمية الذكاء الاصطناعي - نظام متكامل</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;900&display=swap');
        
        * { font-family: 'Tajawal', sans-serif; box-sizing: border-box; }
        body { background-color: #030712; color: #f9fafb; overflow-x: hidden; }

        .glass-panel {
            background: rgba(17, 24, 39, 0.75);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }

        .glass-card {
            background: rgba(31, 41, 55, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        .glass-card:hover {
            transform: translateY(-3px);
            border-color: rgba(59, 130, 246, 0.4);
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.2);
        }

        .glass-button {
            background: rgba(59, 130, 246, 0.15);
            border: 1px solid rgba(59, 130, 246, 0.3);
            backdrop-filter: blur(8px);
            transition: all 0.3s ease;
        }
        .glass-button:hover {
            background: rgba(59, 130, 246, 0.35);
            border-color: rgba(96, 165, 250, 0.8);
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.4);
        }
        .glass-button:active { transform: scale(0.96); }

        /* زر الدعم الفني - تصميم خاص */
        .telegram-support-btn {
            background: linear-gradient(135deg, rgba(0, 136, 204, 0.2) 0%, rgba(36, 169, 220, 0.25) 100%);
            border: 1px solid rgba(36, 169, 220, 0.5);
            backdrop-filter: blur(10px);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        .telegram-support-btn::before {
            content: '';
            position: absolute;
            top: 0;
            right: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: right 0.6s;
        }
        .telegram-support-btn:hover::before { right: 100%; }
        .telegram-support-btn:hover {
            background: linear-gradient(135deg, rgba(0, 136, 204, 0.4) 0%, rgba(36, 169, 220, 0.5) 100%);
            border-color: rgba(56, 189, 240, 0.9);
            box-shadow: 0 0 25px rgba(36, 169, 220, 0.6), 0 0 40px rgba(0, 136, 204, 0.3);
            transform: translateY(-2px);
        }
        .telegram-support-btn:active { transform: translateY(0) scale(0.97); }
        
        .tg-icon-glow {
            filter: drop-shadow(0 0 8px rgba(36, 169, 220, 0.8));
            animation: tgPulse 2s ease-in-out infinite;
        }
        @keyframes tgPulse {
            0%, 100% { filter: drop-shadow(0 0 6px rgba(36, 169, 220, 0.6)); }
            50% { filter: drop-shadow(0 0 14px rgba(56, 189, 240, 1)); }
        }

        .online-dot {
            position: absolute;
            top: -2px;
            left: -2px;
            width: 8px;
            height: 8px;
            background: #22c55e;
            border-radius: 50%;
            border: 2px solid #030712;
            animation: onlinePing 1.5s infinite;
        }
        @keyframes onlinePing {
            0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
            70% { box-shadow: 0 0 0 8px rgba(34, 197, 94, 0); }
            100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
        }

        .glow-orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            z-index: 0;
            animation: floatOrb 12s infinite alternate ease-in-out;
        }
        @keyframes floatOrb {
            0% { transform: translate(0, 0) scale(1); }
            100% { transform: translate(-40px, 60px) scale(0.95); }
        }

        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #030712; }
        ::-webkit-scrollbar-thumb { background: #1f2937; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #374151; }

        .xp-float {
            position: fixed;
            pointer-events: none;
            font-weight: 900;
            font-size: 24px;
            color: #fbbf24;
            text-shadow: 0 0 20px rgba(251, 191, 36, 0.8);
            animation: floatUp 1.5s ease-out forwards;
            z-index: 9999;
        }
        @keyframes floatUp {
            0% { opacity: 1; transform: translateY(0) scale(1); }
            100% { opacity: 0; transform: translateY(-80px) scale(1.5); }
        }

        .toast {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 10000;
            animation: slideIn 0.3s ease-out;
        }
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        .card-flip { perspective: 1000px; }
        .card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }
        .card-flip.flipped .card-inner { transform: rotateY(180deg); }
        .card-front, .card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card-back { transform: rotateY(180deg); }

        .letter-tile {
            width: 44px;
            height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #1e40af, #3730a3);
            border: 2px solid #60a5fa;
            border-radius: 8px;
            font-weight: 900;
            font-size: 18px;
            cursor: pointer;
            transition: all 0.2s;
            user-select: none;
        }
        .letter-tile:hover { transform: translateY(-4px); box-shadow: 0 4px 12px rgba(96, 165, 250, 0.5); }
        .letter-tile.used { opacity: 0.3; pointer-events: none; }

        .drop-zone { min-height: 80px; transition: all 0.3s; }
        .drop-zone.drag-over { background: rgba(59, 130, 246, 0.2); border-color: #3b82f6; }

        .draggable-item {
            cursor: grab;
            user-select: none;
            transition: all 0.2s;
        }
        .draggable-item:active { cursor: grabbing; transform: scale(1.02); }
        .draggable-item.placed { opacity: 0.5; pointer-events: none; }

        .progress-bar { transition: width 0.5s ease; }

        .typing-indicator span {
            display: inline-block;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #60a5fa;
            animation: typing 1.4s infinite;
        }
        .typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
        .typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes typing {
            0%, 60%, 100% { transform: translateY(0); opacity: 0.7; }
            30% { transform: translateY(-8px); opacity: 1; }
        }

        .pulse-ring { animation: pulseRing 2s infinite; }
        @keyframes pulseRing {
            0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(239, 68, 68, 0); }
            100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
        }

        .tab-content { animation: fadeIn 0.4s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .achievement-badge { animation: badgePop 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55); }
        @keyframes badgePop { 0% { transform: scale(0); } 80% { transform: scale(1.1); } 100% { transform: scale(1); } }

        .shake { animation: shake 0.5s; }
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            75% { transform: translateX(10px); }
        }

        .combo-pulse { animation: comboPulse 0.3s; }
        @keyframes comboPulse { 0% { transform: scale(1); } 50% { transform: scale(1.3); } 100% { transform: scale(1); } }

        .gradient-text {
            background: linear-gradient(90deg, #3b82f6, #a855f7, #ec4899);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            background-size: 200% auto;
            animation: gradientFlow 3s linear infinite;
        }
        @keyframes gradientFlow { to { background-position: 200% center; } }

        /* نافذة الدعم الفني */
        .support-modal {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(8px);
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: fadeIn 0.3s ease;
        }
        .support-modal.hidden { display: none; }
        .support-box {
            background: linear-gradient(135deg, rgba(17, 24, 39, 0.95), rgba(31, 41, 55, 0.95));
            border: 1px solid rgba(36, 169, 220, 0.4);
            border-radius: 20px;
            padding: 30px;
            max-width: 420px;
            width: 90%;
            animation: modalPop 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }
        @keyframes modalPop {
            0% { transform: scale(0.7); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }

        /* زر عائم للدعم الفني */
        .floating-support {
            position: fixed;
            bottom: 25px;
            left: 25px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #0088cc, #24a9dc);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 30px rgba(0, 136, 204, 0.6), 0 0 0 4px rgba(0, 136, 204, 0.15);
            cursor: pointer;
            z-index: 500;
            transition: all 0.3s ease;
            animation: floatingBounce 3s ease-in-out infinite;
        }
        .floating-support:hover {
            transform: scale(1.1) rotate(-10deg);
            box-shadow: 0 12px 40px rgba(36, 169, 220, 0.8), 0 0 0 6px rgba(36, 169, 220, 0.25);
        }
        .floating-support::before {
            content: '';
            position: absolute;
            inset: -4px;
            border-radius: 50%;
            border: 2px solid rgba(56, 189, 240, 0.6);
            animation: ringExpand 2s infinite;
        }
        @keyframes floatingBounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
        @keyframes ringExpand {
            0% { transform: scale(1); opacity: 1; }
            100% { transform: scale(1.4); opacity: 0; }
        }
        .floating-support .badge {
            position: absolute;
            top: -4px;
            right: -4px;
            background: #ef4444;
            color: white;
            font-size: 10px;
            font-weight: 900;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px solid #030712;
            animation: onlinePing 1.5s infinite;
        }
    </style>
</head>
<body class="relative min-h-screen">

    <canvas id="bgCanvas" class="fixed top-0 left-0 w-full h-full pointer-events-none z-0"></canvas>
    <div class="glow-orb w-96 h-96 bg-blue-600/20 top-10 right-10"></div>
    <div class="glow-orb w-80 h-80 bg-purple-600/20 bottom-10 left-10" style="animation-delay: -5s;"></div>
    <div class="glow-orb w-72 h-72 bg-pink-600/15 top-1/2 left-1/2" style="animation-delay: -8s;"></div>

    <div id="toastContainer" class="fixed top-4 right-4 z-50 flex flex-col gap-2"></div>

    <div class="relative z-10 flex flex-col h-screen max-w-7xl mx-auto p-3 gap-3">

        <!-- Header -->
        <header class="glass-panel rounded-2xl p-3 flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <div class="p-3 bg-gradient-to-tr from-blue-600 to-indigo-500 rounded-xl shadow-lg shadow-blue-500/30 relative">
                    <i data-lucide="sparkles" class="w-6 h-6 text-white animate-pulse"></i>
                </div>
                <div>
                    <h1 class="font-black text-lg gradient-text">الأكاديمية الذكية الشاملة</h1>
                    <p class="text-[11px] text-gray-400">منظومة التعلم والتحدي الذهني v3.0</p>
                </div>
            </div>

            <div class="flex items-center gap-2 flex-wrap">
                <!-- Level Bar -->
                <div class="flex flex-col gap-0.5">
                    <div class="flex items-center justify-between text-[10px] text-gray-400">
                        <span>المستوى <span id="userLevel" class="text-amber-400 font-black">12</span></span>
                        <span id="xpToNext">320/500</span>
                    </div>
                    <div class="w-28 h-1.5 bg-gray-800 rounded-full overflow-hidden">
                        <div id="levelBar" class="progress-bar h-full bg-gradient-to-r from-amber-500 to-orange-500 rounded-full" style="width: 64%"></div>
                    </div>
                </div>

                <div class="flex items-center gap-1.5 bg-amber-500/10 border border-amber-500/30 px-2.5 py-1 rounded-lg text-[11px] font-bold text-amber-400">
                    <i data-lucide="flame" class="w-3.5 h-3.5 text-orange-400 animate-bounce"></i> 
                    <span id="streakDays">5</span> يوم
                </div>
                <div class="flex items-center gap-1.5 bg-purple-500/10 border border-purple-500/30 px-2.5 py-1 rounded-lg text-[11px] font-bold text-purple-300">
                    <i data-lucide="zap" class="w-3.5 h-3.5"></i>
                    <span id="comboCount">x1</span>
                </div>
                <div class="flex items-center gap-1.5 bg-amber-500/10 border border-amber-500/30 px-2.5 py-1 rounded-lg text-[11px] font-bold text-amber-400">
                    <i data-lucide="trophy" class="w-3.5 h-3.5"></i> 
                    <span id="xpValue">1250</span> XP
                </div>

                <!-- زر الدعم الفني في التلغرام - جديد -->
                <a href="https://t.me/m3v30" target="_blank" rel="noopener noreferrer" 
                   class="telegram-support-btn flex items-center gap-2 px-3 py-1.5 rounded-lg text-[11px] font-bold text-cyan-100 group"
                   onclick="trackSupportClick(event)">
                    <span class="relative">
                        <svg class="w-4 h-4 tg-icon-glow" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
                        </svg>
                        <span class="online-dot"></span>
                    </span>
                    <span class="flex flex-col items-start leading-tight">
                        <span class="text-[10px] text-cyan-100 group-hover:text-white">الدعم الفني</span>
                        <span class="text-[8px] text-cyan-300/80 font-normal">@m3v30</span>
                    </span>
                    <i data-lucide="external-link" class="w-3 h-3 text-cyan-300 group-hover:translate-x-[-3px] transition-transform"></i>
                </a>

                <button onclick="toggleSound()" id="soundToggle" class="p-2 glass-button rounded-lg" title="الصوت">
                    <i data-lucide="volume-2" class="w-4 h-4 text-cyan-300"></i>
                </button>
            </div>
        </header>

        <div class="flex-1 grid grid-cols-1 md:grid-cols-12 gap-3 overflow-hidden">

            <!-- Sidebar -->
            <aside class="md:col-span-3 glass-panel rounded-2xl p-3 flex flex-col gap-2 overflow-y-auto">
                <h2 class="text-[10px] font-black text-gray-500 tracking-widest uppercase mb-1">الوحدات الذكية</h2>
                
                <button onclick="switchTab('dashboard')" class="tab-btn glass-button flex items-center justify-between p-2.5 rounded-xl text-xs font-bold text-right w-full text-cyan-300">
                    <span class="flex items-center gap-2"><i data-lucide="layout-dashboard" class="w-4 h-4"></i> لوحة التحكم</span>
                    <i data-lucide="chevron-left" class="w-3.5 h-3.5"></i>
                </button>
                <button onclick="switchTab('games')" class="tab-btn glass-button flex items-center justify-between p-2.5 rounded-xl text-xs font-bold text-right w-full text-amber-400">
                    <span class="flex items-center gap-2"><i data-lucide="gamepad-2" class="w-4 h-4"></i> الألعاب (11 نمط)</span>
                    <i data-lucide="chevron-left" class="w-3.5 h-3.5"></i>
                </button>
                <button onclick="switchTab('leaderboard')" class="tab-btn glass-button flex items-center justify-between p-2.5 rounded-xl text-xs font-bold text-right w-full text-purple-300">
                    <span class="flex items-center gap-2"><i data-lucide="award" class="w-4 h-4"></i> التصنيف والشخصيات</span>
                    <i data-lucide="chevron-left" class="w-3.5 h-3.5"></i>
                </button>
                <button onclick="switchTab('chat')" class="tab-btn glass-button flex items-center justify-between p-2.5 rounded-xl text-xs font-bold text-right w-full text-emerald-300">
                    <span class="flex items-center gap-2"><i data-lucide="message-square-code" class="w-4 h-4"></i> المساعد الذكي</span>
                    <span class="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></span>
                </button>
                <button onclick="switchTab('camera')" class="tab-btn glass-button flex items-center justify-between p-2.5 rounded-xl text-xs font-bold text-right w-full text-rose-300">
                    <span class="flex items-center gap-2"><i data-lucide="camera" class="w-4 h-4"></i> الماسح البصري</span>
                    <i data-lucide="chevron-left" class="w-3.5 h-3.5"></i>
                </button>
                <button onclick="switchTab('pdf')" class="tab-btn glass-button flex items-center justify-between p-2.5 rounded-xl text-xs font-bold text-right w-full text-blue-300">
                    <span class="flex items-center gap-2"><i data-lucide="file-text" class="w-4 h-4"></i> تحليل PDF</span>
                    <i data-lucide="chevron-left" class="w-3.5 h-3.5"></i>
                </button>
                <button onclick="switchTab('quiz')" class="tab-btn glass-button flex items-center justify-between p-2.5 rounded-xl text-xs font-bold text-right w-full text-pink-300">
                    <span class="flex items-center gap-2"><i data-lucide="brain-circuit" class="w-4 h-4"></i> مولد الاختبارات</span>
                    <i data-lucide="chevron-left" class="w-3.5 h-3.5"></i>
                </button>
                <button onclick="switchTab('achievements')" class="tab-btn glass-button flex items-center justify-between p-2.5 rounded-xl text-xs font-bold text-right w-full text-yellow-300">
                    <span class="flex items-center gap-2"><i data-lucide="medal" class="w-4 h-4"></i> الإنجازات</span>
                    <span id="badgeCount" class="text-[9px] bg-yellow-500 text-black px-1.5 rounded-full">0</span>
                </button>

                <!-- زر الدعم الفني في الشريط الجانبي -->
                <div class="mt-2 pt-2 border-t border-gray-800">
                    <a href="https://t.me/m3v30" target="_blank" rel="noopener noreferrer" 
                       class="telegram-support-btn flex items-center justify-between p-2.5 rounded-xl text-xs font-bold w-full text-cyan-100 group">
                        <span class="flex items-center gap-2">
                            <svg class="w-4 h-4 tg-icon-glow" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
                            </svg>
                            <span class="flex flex-col text-right">
                                <span class="text-[11px] text-cyan-100 group-hover:text-white">الدعم الفني 24/7</span>
                                <span class="text-[9px] text-cyan-300/80 font-normal">@m3v30</span>
                            </span>
                        </span>
                        <span class="flex items-center gap-1">
                            <span class="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-pulse"></span>
                            <span class="text-[9px] text-emerald-300">متصل</span>
                        </span>
                    </a>
                </div>

                <!-- Stats Mini -->
                <div class="mt-auto pt-2 border-t border-gray-800">
                    <div class="grid grid-cols-2 gap-1.5 text-[10px]">
                        <div class="bg-gray-900/50 p-2 rounded-lg">
                            <p class="text-gray-500">الألعاب</p>
                            <p id="miniGames" class="font-black text-emerald-400">0</p>
                        </div>
                        <div class="bg-gray-900/50 p-2 rounded-lg">
                            <p class="text-gray-500">الدقة</p>
                            <p id="miniAccuracy" class="font-black text-amber-400">0%</p>
                        </div>
                    </div>
                </div>
            </aside>

            <!-- Main Panel -->
            <main class="md:col-span-9 glass-panel rounded-2xl p-3 flex flex-col relative overflow-hidden">

                <!-- DASHBOARD TAB -->
                <div id="tab-dashboard" class="tab-content flex-1 flex flex-col gap-3 overflow-y-auto pr-1">
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-2">
                        <div class="glass-card p-3 rounded-xl border-t-2 border-blue-500">
                            <i data-lucide="trending-up" class="w-4 h-4 text-blue-400 mb-1"></i>
                            <p class="text-[10px] text-gray-400">النقاط الكلية</p>
                            <h3 id="dashXP" class="text-lg font-black text-blue-400">0</h3>
                        </div>
                        <div class="glass-card p-3 rounded-xl border-t-2 border-emerald-500">
                            <i data-lucide="check-circle" class="w-4 h-4 text-emerald-400 mb-1"></i>
                            <p class="text-[10px] text-gray-400">التحديات المحلولة</p>
                            <h3 id="dashGames" class="text-lg font-black text-emerald-400">0</h3>
                        </div>
                        <div class="glass-card p-3 rounded-xl border-t-2 border-amber-500">
                            <i data-lucide="target" class="w-4 h-4 text-amber-400 mb-1"></i>
                            <p class="text-[10px] text-gray-400">أفضل سلسلة</p>
                            <h3 id="dashBestCombo" class="text-lg font-black text-amber-400">0x</h3>
                        </div>
                        <div class="glass-card p-3 rounded-xl border-t-2 border-purple-500">
                            <i data-lucide="medal" class="w-4 h-4 text-purple-400 mb-1"></i>
                            <p class="text-[10px] text-gray-400">الإنجازات</p>
                            <h3 id="dashBadges" class="text-lg font-black text-purple-400">0</h3>
                        </div>
                    </div>

                    <!-- بطاقة الدعم الفني في لوحة التحكم -->
                    <div class="bg-gradient-to-r from-cyan-900/40 via-blue-900/30 to-indigo-900/40 p-4 rounded-xl border border-cyan-500/30 flex items-center justify-between gap-3">
                        <div class="flex items-center gap-3">
                            <div class="p-2.5 bg-cyan-600/30 rounded-xl border border-cyan-500/40 relative">
                                <svg class="w-6 h-6 text-cyan-300 tg-icon-glow" viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
                                </svg>
                            </div>
                            <div>
                                <h3 class="font-black text-sm text-cyan-200 flex items-center gap-2">
                                    فريق الدعم الفني متاح
                                    <span class="flex items-center gap-1 bg-emerald-500/20 border border-emerald-500/40 px-1.5 py-0.5 rounded text-[9px] text-emerald-300 font-bold">
                                        <span class="w-1 h-1 bg-emerald-400 rounded-full animate-pulse"></span>
                                        متاح الآن
                                    </span>
                                </h3>
                                <p class="text-[11px] text-gray-400 mt-0.5">تواصل مع الدعم عبر تلغرام <span class="text-cyan-300 font-bold">@m3v30</span> لأي استفسار أو مشكلة تقنية</p>
                            </div>
                        </div>
                        <a href="https://t.me/m3v30" target="_blank" rel="noopener noreferrer" 
                           class="telegram-support-btn px-4 py-2 rounded-lg text-xs font-bold text-cyan-100 flex items-center gap-1.5 whitespace-nowrap">
                            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
                            </svg>
                            فتح المحادثة
                        </a>
                    </div>

                    <!-- Daily Challenge -->
                    <div class="bg-gradient-to-r from-indigo-900/60 via-purple-900/40 to-blue-900/60 p-4 rounded-xl border border-purple-500/30">
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex items-center gap-2">
                                <i data-lucide="sunrise" class="w-5 h-5 text-amber-300"></i>
                                <h3 class="font-black text-sm text-amber-200">تحدي اليوم</h3>
                            </div>
                            <span class="text-[10px] text-gray-400">متبقي: <span id="dailyTimer">--:--</span></span>
                        </div>
                        <p id="dailyChallengeText" class="text-xs text-gray-300 mb-3">أكمل 3 ألعاب مختلفة اليوم للحصول على 200 XP إضافي!</p>
                        <div class="flex items-center gap-2">
                            <div class="flex-1 h-2 bg-gray-800 rounded-full overflow-hidden">
                                <div id="dailyProgress" class="progress-bar h-full bg-gradient-to-r from-amber-500 to-pink-500" style="width: 0%"></div>
                            </div>
                            <span id="dailyProgressText" class="text-[10px] text-gray-400">0/3</span>
                        </div>
                    </div>

                    <!-- Recent Activity -->
                    <div class="bg-gray-900/60 p-3 rounded-xl border border-gray-800">
                        <h3 class="font-bold text-xs text-gray-300 mb-2 flex items-center gap-1">
                            <i data-lucide="activity" class="w-3.5 h-3.5"></i> النشاط الأخير
                        </h3>
                        <div id="activityFeed" class="space-y-1.5 max-h-40 overflow-y-auto text-xs">
                            <p class="text-gray-500 italic">لا يوجد نشاط بعد... ابدأ باللعب!</p>
                        </div>
                    </div>
                </div>

                <!-- GAMES TAB -->
                <div id="tab-games" class="tab-content hidden flex-1 flex flex-col gap-3 overflow-y-auto pr-1">
                    <div class="flex items-center justify-between bg-gray-900/80 p-2.5 rounded-xl border border-gray-800">
                        <div>
                            <h2 class="font-black text-xs text-amber-300 flex items-center gap-2">
                                <i data-lucide="trophy" class="w-4 h-4"></i> ساحة التحديات الذهنية
                            </h2>
                            <p class="text-[10px] text-gray-400">اختر نمط اللعبة</p>
                        </div>
                        <button onclick="openRandomGame()" class="glass-button px-3 py-1 rounded-lg text-[10px] font-bold text-amber-300 flex items-center gap-1">
                            <i data-lucide="shuffle" class="w-3 h-3"></i> عشوائي
                        </button>
                    </div>

                    <div id="gameArena" class="bg-gray-950/90 border-2 border-amber-500/20 rounded-xl p-4 hidden flex-col gap-3 relative">
                        <div class="flex justify-between items-center border-b border-gray-800 pb-2">
                            <h3 id="arenaTitle" class="font-bold text-sm text-amber-400">اللعبة</h3>
                            <div class="flex items-center gap-2">
                                <div id="gameTimer" class="text-xs font-mono font-black text-red-400 pulse-ring px-2 py-0.5 rounded bg-red-500/10 hidden">30</div>
                                <button onclick="closeGameArena()" class="text-[10px] text-gray-400 hover:text-white bg-gray-800 px-2.5 py-1 rounded-lg flex items-center gap-1">
                                    <i data-lucide="x" class="w-3 h-3"></i> خروج
                                </button>
                            </div>
                        </div>
                        <div id="arenaBody" class="min-h-[200px] flex flex-col justify-center items-center text-center gap-3">
                        </div>
                        <div id="arenaFeedback" class="hidden text-xs font-bold p-2 rounded-lg text-center"></div>
                    </div>

                    <!-- 11 Game Modes Grid -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2">
                        <div onclick="startMathBlitz()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-amber-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="calculator" class="w-4 h-4 text-amber-400"></i><h3 class="font-bold text-[11px]">1. الحساب الذهني</h3></div>
                            <p class="text-[10px] text-gray-400">معادلات سريعة تتسارع تدريجياً</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-amber-500">+50 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-blue-400">متوسط</span></div>
                        </div>
                        <div onclick="startHistoryRiddles()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-purple-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="scroll" class="w-4 h-4 text-purple-400"></i><h3 class="font-bold text-[11px]">2. الآلة الزمنية</h3></div>
                            <p class="text-[10px] text-gray-400">ألغاز تاريخية غامضة</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-purple-500">+75 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-emerald-400">سهل</span></div>
                        </div>
                        <div onclick="startTimelineGame()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-blue-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="hourglass" class="w-4 h-4 text-blue-400"></i><h3 class="font-bold text-[11px]">3. الخط الزمني</h3></div>
                            <p class="text-[10px] text-gray-400">ترتيب الأحداث زمنياً</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-blue-500">+60 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-amber-400">صعب</span></div>
                        </div>
                        <div onclick="startFallacySpotter()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-emerald-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="shield-alert" class="w-4 h-4 text-emerald-400"></i><h3 class="font-bold text-[11px]">4. المغالطات المنطقية</h3></div>
                            <p class="text-[10px] text-gray-400">اكتشف الأخطاء المنطقية</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-emerald-500">+80 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-amber-400">صعب</span></div>
                        </div>
                        <div onclick="startPhysicsBlitz()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-cyan-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="atom" class="w-4 h-4 text-cyan-400"></i><h3 class="font-bold text-[11px]">5. تحدي الفيزياء</h3></div>
                            <p class="text-[10px] text-gray-400">ألغاز فيزيائية مفاهيمية</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-cyan-500">+70 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-amber-400">صعب</span></div>
                        </div>
                        <div onclick="startMemoryMatch()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-pink-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="brain" class="w-4 h-4 text-pink-400"></i><h3 class="font-bold text-[11px]">6. الذاكرة العلمية</h3></div>
                            <p class="text-[10px] text-gray-400">مطابقة المفاهيم والقوانين</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-pink-500">+90 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-emerald-400">سهل</span></div>
                        </div>
                        <div onclick="startLogicMaze()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-indigo-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="code-2" class="w-4 h-4 text-indigo-400"></i><h3 class="font-bold text-[11px]">7. متاهة البرمجة</h3></div>
                            <p class="text-[10px] text-gray-400">تتبع الأكواد واكتشاف المخرج</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-indigo-500">+75 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-red-400">خبير</span></div>
                        </div>
                        <div onclick="startWordDecipher()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-rose-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="binary" class="w-4 h-4 text-rose-400"></i><h3 class="font-bold text-[11px]">8. تفكيك المصطلحات</h3></div>
                            <p class="text-[10px] text-gray-400">إعادة ترتيب الحروف</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-rose-500">+60 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-blue-400">متوسط</span></div>
                        </div>
                        <div onclick="startConceptClassifier()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-yellow-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="layers" class="w-4 h-4 text-yellow-400"></i><h3 class="font-bold text-[11px]">9. تصنيف المفاهيم</h3></div>
                            <p class="text-[10px] text-gray-400">فرز وسحب المفاهيم</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-yellow-500">+70 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-blue-400">متوسط</span></div>
                        </div>
                        <div onclick="startTwentyQuestions()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-teal-400">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="help-circle" class="w-4 h-4 text-teal-400"></i><h3 class="font-bold text-[11px]">10. تخمين الشخصية</h3></div>
                            <p class="text-[10px] text-gray-400">أسئلة ذكية للتخمين</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-teal-500">+85 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-amber-400">صعب</span></div>
                        </div>
                        <div onclick="startDailyBrainQuest()" class="glass-card p-3 rounded-xl cursor-pointer border-r-4 border-red-500 sm:col-span-2 lg:col-span-1">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="sparkles" class="w-4 h-4 text-red-400"></i><h3 class="font-bold text-[11px]">11. التحدي الشامل (IQ)</h3></div>
                            <p class="text-[10px] text-gray-400">تحدي مخلوط شامل</p>
                            <div class="mt-2 flex items-center gap-1"><span class="text-[9px] text-red-500">+150 XP</span><span class="text-[9px] text-gray-600">•</span><span class="text-[9px] text-red-400">خبير</span></div>
                        </div>
                    </div>
                </div>

                <!-- باقي التبويبات كما هي... -->
                <div id="tab-leaderboard" class="tab-content hidden flex-1 flex flex-col gap-3 overflow-y-auto pr-1">
                    <div class="bg-gradient-to-r from-purple-900/40 via-blue-900/30 to-gray-900 p-3 rounded-2xl border border-purple-500/30 flex flex-col md:flex-row items-center justify-between gap-3">
                        <div class="flex items-center gap-3">
                            <div class="p-2.5 bg-purple-600/30 rounded-xl border border-purple-500/40">
                                <i data-lucide="user-check" class="w-5 h-5 text-purple-300"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-xs text-purple-200">إعدادات الخصوصية</h3>
                                <p class="text-[10px] text-gray-400">مارس بخصوصية كاملة</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-2 flex-wrap">
                            <div class="flex items-center gap-1.5 bg-gray-900/80 p-1.5 rounded-lg border border-gray-800">
                                <span class="text-[10px] text-gray-300">التصنيف:</span>
                                <label class="relative inline-flex items-center cursor-pointer">
                                    <input type="checkbox" id="toggleLeaderboard" class="sr-only peer" checked onchange="toggleLeaderboardVisibility(this.checked)">
                                    <div class="w-8 h-4 bg-gray-700 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border after:rounded-full after:h-3 after:w-3 after:transition-all peer-checked:bg-purple-600"></div>
                                </label>
                            </div>
                            <select id="avatarSelect" onchange="changeUserAvatar(this.value)" class="bg-gray-800 text-[10px] text-purple-300 font-bold px-2 py-1 rounded-lg border border-purple-500/40">
                                <option value="الفيزيائي المجهول ⚛️">الفيزيائي المجهول ⚛️</option>
                                <option value="المحقق التاريخي 📜">المحقق التاريخي 📜</option>
                                <option value="عبقري الخوارزميات 💻">عبقري الخوارزميات 💻</option>
                                <option value="مكتشف المجرات 🌌">مكتشف المجرات 🌌</option>
                                <option value="الفيلسوف الغامض 🧠">الفيلسوف الغامض 🧠</option>
                            </select>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                        <div class="glass-card p-2.5 rounded-xl border-l-4 border-blue-500">
                            <p class="text-[10px] text-gray-400">النقاط</p>
                            <h3 id="statTotalXP" class="text-base font-black text-blue-400">0</h3>
                        </div>
                        <div class="glass-card p-2.5 rounded-xl border-l-4 border-emerald-500">
                            <p class="text-[10px] text-gray-400">التحديات</p>
                            <h3 id="statGamesWon" class="text-base font-black text-emerald-400">0</h3>
                        </div>
                        <div class="glass-card p-2.5 rounded-xl border-l-4 border-amber-500">
                            <p class="text-[10px] text-gray-400">الدقة</p>
                            <h3 id="statAccuracy" class="text-base font-black text-amber-400">0%</h3>
                        </div>
                        <div class="glass-card p-2.5 rounded-xl border-l-4 border-purple-500">
                            <p class="text-[10px] text-gray-400">الحالة</p>
                            <h3 id="statVisibility" class="text-[10px] font-bold text-emerald-400 mt-1">ظاهر</h3>
                        </div>
                    </div>

                    <div class="bg-gray-900/80 border border-gray-800 rounded-2xl p-3 flex flex-col gap-2">
                        <div class="flex items-center justify-between border-b border-gray-800 pb-2">
                            <h3 class="font-bold text-xs text-purple-300 flex items-center gap-1">
                                <i data-lucide="award" class="w-3.5 h-3.5"></i> لوحة المتصدرين
                            </h3>
                            <span class="text-[9px] text-gray-400">هويات رمزية</span>
                        </div>
                        <div class="space-y-1.5" id="leaderboardList">
                            <div class="flex items-center justify-between bg-amber-500/10 border border-amber-500/30 p-2 rounded-lg">
                                <div class="flex items-center gap-2">
                                    <span class="text-sm font-black text-amber-400 w-5">🥇</span>
                                    <div><h4 class="font-bold text-[11px] text-amber-200">الراحل عبر الزمن ⏳</h4><p class="text-[9px] text-amber-400/80">أسطورة الأكاديمية</p></div>
                                </div>
                                <span class="font-black text-[10px] text-amber-300">3,450 XP</span>
                            </div>
                            <div class="flex items-center justify-between bg-gray-800/60 border border-gray-700/40 p-2 rounded-lg">
                                <div class="flex items-center gap-2">
                                    <span class="text-sm font-black text-gray-300 w-5">🥈</span>
                                    <div><h4 class="font-bold text-[11px] text-gray-200">صانع المعادلات 🧮</h4><p class="text-[9px] text-gray-400">عبقري الحساب</p></div>
                                </div>
                                <span class="font-black text-[10px] text-gray-300">2,980 XP</span>
                            </div>
                            <div id="currentUserRankCard" class="flex items-center justify-between bg-blue-600/20 border border-blue-500/50 p-2 rounded-lg">
                                <div class="flex items-center gap-2">
                                    <span class="text-[10px] font-black text-blue-400 w-5">#3</span>
                                    <div>
                                        <h4 id="userDisplayName" class="font-bold text-[11px] text-blue-200 flex items-center gap-1">الفيزيائي المجهول ⚛️ <span class="bg-blue-500 text-[8px] text-white px-1 rounded">أنت</span></h4>
                                        <p class="text-[9px] text-blue-300">باحث متميز</p>
                                    </div>
                                </div>
                                <span id="lbUserXP" class="font-black text-[10px] text-blue-300">0 XP</span>
                            </div>
                            <div class="flex items-center justify-between bg-gray-900/50 border border-gray-800 p-2 rounded-lg">
                                <div class="flex items-center gap-2">
                                    <span class="text-[10px] font-black text-gray-500 w-5">#4</span>
                                    <div><h4 class="font-bold text-[11px] text-gray-300">فارس المنطق 🛡️</h4><p class="text-[9px] text-gray-500">محلل فلسفي</p></div>
                                </div>
                                <span class="font-black text-[10px] text-gray-400">950 XP</span>
                            </div>
                        </div>
                        <div id="disabledLbBanner" class="hidden p-5 text-center bg-gray-950 rounded-xl border border-dashed border-gray-800">
                            <i data-lucide="eye-off" class="w-7 h-7 text-gray-600 mx-auto mb-2"></i>
                            <h4 class="text-xs font-bold text-gray-400">وضع الخصوصية مفعّل</h4>
                            <p class="text-[9px] text-gray-500 mt-1">نقاطك تُحفظ محلياً فقط</p>
                        </div>
                    </div>
                </div>

                <div id="tab-chat" class="tab-content hidden flex-1 flex flex-col justify-between gap-2 overflow-hidden">
                    <div class="bg-gray-900/80 p-2 rounded-xl border border-gray-800 flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <div class="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></div>
                            <span class="text-xs font-bold text-emerald-300">المساعد الذكي متصل</span>
                        </div>
                        <button onclick="clearChat()" class="text-[10px] text-gray-400 hover:text-white px-2 py-0.5 bg-gray-800 rounded">مسح</button>
                    </div>
                    <div id="chatBox" class="flex-1 overflow-y-auto space-y-3 p-2 bg-gray-950/50 rounded-xl">
                        <div class="flex items-start gap-2">
                            <div class="w-8 h-8 rounded-lg bg-blue-600/30 border border-blue-500/40 flex items-center justify-center text-xs font-bold text-blue-400 shrink-0">AI</div>
                            <div class="bg-gr
