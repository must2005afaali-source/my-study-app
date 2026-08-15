import streamlit as st
import streamlit.components.v1 as components
import json
from datetime import datetime

st.set_page_config(
    page_title="المختبر التفاعلي للدوائر الكهربائية",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        .block-container { padding: 1rem 2rem; }
        footer { visibility: hidden; }
        .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .main-header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 20px 30px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            border: 1px solid rgba(255,255,255,0.3);
        }
        .main-header h1 {
            color: #1e293b;
            font-size: 32px;
            font-weight: 800;
            margin: 0;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .main-header p {
            color: #64748b;
            margin: 8px 0 0 0;
            font-size: 16px;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        .feature-card {
            background: rgba(255,255,255,0.9);
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            transition: all 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        }
        .feature-icon { font-size: 32px; margin-bottom: 10px; }
        .feature-title { font-weight: 700; color: #1e293b; margin-bottom: 5px; }
        .feature-desc { color: #64748b; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>⚡ المختبر التفاعلي للدوائر الكهربائية</h1>
        <p>محاكاة احترافية للدوائر الكهربائية مع تحليل فوري ورسوم بيانية تفاعلية</p>
    </div>
    
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">🔧</div>
            <div class="feature-title">سحب وإفلات</div>
            <div class="feature-desc">اسحب المكونات من الشريط الجانبي إلى لوحة الرسم</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">تحليل فوري</div>
            <div class="feature-desc">حساب تلقائي للجهد والتيار والقدرة</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔗</div>
            <div class="feature-title">اتصال ذكي</div>
            <div class="feature-desc">اربط المكونات بأسلاك تفاعلية</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">💾</div>
            <div class="feature-title">حفظ وتحميل</div>
            <div class="feature-desc">احفظ دوائرك وحملها لاحقاً</div>
        </div>
    </div>
""", unsafe_allow_html=True)

react_flow_html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>المختبر الكهربائي</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800&display=swap" rel="stylesheet">
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://unpkg.com/reactflow@11.10.1/dist/umd/index.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/reactflow@11.10.1/dist/style.css" />
    
    <style>
        * {
            font-family: 'Tajawal', sans-serif;
            box-sizing: border-box;
            -webkit-font-smoothing: antialiased;
        }
        
        body, html, #root {
            width: 100%;
            height: 100vh;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        
        .app-container {
            display: flex;
            width: 100%;
            height: 100%;
            background: #f8fafc;
        }
        
        /* Sidebar */
        .sidebar {
            width: 280px;
            background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
            color: white;
            padding: 20px;
            overflow-y: auto;
            box-shadow: 4px 0 20px rgba(0,0,0,0.1);
            z-index: 100;
        }
        
        .sidebar-header {
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 2px solid rgba(255,255,255,0.1);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .component-section {
            margin-bottom: 20px;
        }
        
        .section-title {
            font-size: 12px;
            font-weight: 700;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }
        
        .component-item {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 14px;
            margin-bottom: 10px;
            cursor: grab;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .component-item:hover {
            background: rgba(59, 130, 246, 0.2);
            border-color: rgba(59, 130, 246, 0.5);
            transform: translateX(-5px);
        }
        
        .component-item:active {
            cursor: grabbing;
            transform: scale(0.95);
        }
        
        .component-icon {
            font-size: 24px;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
        }
        
        .component-info {
            flex: 1;
        }
        
        .component-name {
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 2px;
        }
        
        .component-desc {
            font-size: 11px;
            color: #94a3b8;
        }
        
        /* Main Canvas */
        .canvas-wrapper {
            flex: 1;
            position: relative;
            background: #f8fafc;
        }
        
        .canvas-toolbar {
            position: absolute;
            top: 20px;
            right: 20px;
            z-index: 10;
            display: flex;
            gap: 10px;
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(20px);
            padding: 10px 16px;
            border-radius: 16px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.5);
        }
        
        .toolbar-btn {
            background: #f1f5f9;
            border: 1px solid #e2e8f0;
            padding: 10px 14px;
            border-radius: 10px;
            cursor: pointer;
            font-weight: 600;
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
            color: #475569;
        }
        
        .toolbar-btn:hover {
            background: #3b82f6;
            color: white;
            border-color: #3b82f6;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        }
        
        .toolbar-btn.active {
            background: #3b82f6;
            color: white;
            border-color: #3b82f6;
        }
        
        .toolbar-btn.danger:hover {
            background: #ef4444;
            border-color: #ef4444;
            box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
        }
        
        /* Properties Panel */
        .properties-panel {
            width: 320px;
            background: white;
            border-left: 1px solid #e2e8f0;
            padding: 25px;
            overflow-y: auto;
            box-shadow: -4px 0 20px rgba(0,0,0,0.05);
            z-index: 50;
        }
        
        .panel-header {
            font-size: 18px;
            font-weight: 800;
            color: #1e293b;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .panel-empty {
            text-align: center;
            padding: 40px 20px;
            color: #94a3b8;
        }
        
        .panel-empty-icon {
            font-size: 48px;
            margin-bottom: 15px;
            opacity: 0.5;
        }
        
        .input-group {
            margin-bottom: 18px;
        }
        
        .input-group label {
            display: block;
            font-size: 13px;
            font-weight: 700;
            color: #475569;
            margin-bottom: 8px;
        }
        
        .input-group input, .input-group select {
            width: 100%;
            padding: 12px 16px;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            font-size: 14px;
            transition: all 0.2s;
            outline: none;
            background: #f8fafc;
        }
        
        .input-group input:focus, .input-group select:focus {
            border-color: #3b82f6;
            background: white;
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
        }
        
        .metrics-card {
            background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
            border: 1px solid #bfdbfe;
            border-radius: 16px;
            padding: 20px;
            margin-top: 20px;
        }
        
        .metrics-title {
            font-weight: 800;
            color: #1e40af;
            font-size: 14px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .metric-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            padding: 10px;
            background: rgba(255,255,255,0.6);
            border-radius: 10px;
            font-size: 13px;
        }
        
        .metric-label {
            color: #1e3a8a;
            font-weight: 600;
        }
        
        .metric-value {
            color: #1e40af;
            font-weight: 800;
            font-size: 15px;
        }
        
        .circuit-analysis {
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            border: 1px solid #fbbf24;
            border-radius: 16px;
            padding: 20px;
            margin-top: 20px;
        }
        
        .analysis-title {
            font-weight: 800;
            color: #92400e;
            font-size: 14px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .analysis-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            padding: 10px;
            background: rgba(255,255,255,0.6);
            border-radius: 10px;
            font-size: 13px;
        }
        
        /* Custom Nodes */
        .circuit-node {
            background: white;
            border-radius: 16px;
            padding: 16px;
            min-width: 200px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border: 2px solid #e2e8f0;
            transition: all 0.3s;
        }
        
        .circuit-node.selected {
            border-color: #3b82f6;
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2), 0 8px 30px rgba(59, 130, 246, 0.2);
            transform: scale(1.02);
        }
        
        .circuit-node.battery { border-left: 4px solid #ef4444; }
        .circuit-node.resistor { border-left: 4px solid #f59e0b; }
        .circuit-node.led { border-left: 4px solid #10b981; }
        .circuit-node.switch { border-left: 4px solid #8b5cf6; }
        .circuit-node.capacitor { border-left: 4px solid #06b6d4; }
        .circuit-node.ammeter { border-left: 4px solid #ec4899; }
        .circuit-node.voltmeter { border-left: 4px solid #6366f1; }
        
        .node-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }
        
        .node-title {
            font-weight: 700;
            font-size: 15px;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .node-badge {
            font-size: 10px;
            padding: 4px 10px;
            border-radius: 8px;
            font-weight: 700;
        }
        
        .node-badge.battery { background: #fee2e2; color: #991b1b; }
        .node-badge.resistor { background: #fef3c7; color: #92400e; }
        .node-badge.led { background: #d1fae5; color: #065f46; }
        .node-badge.switch { background: #ede9fe; color: #5b21b6; }
        .node-badge.capacitor { background: #cffafe; color: #155e75; }
        .node-badge.ammeter { background: #fce7f3; color: #9f1239; }
        .node-badge.voltmeter { background: #e0e7ff; color: #3730a3; }
        
        .node-body {
            font-size: 12px;
            color: #64748b;
        }
        
        .node-stat {
            display: flex;
            justify-content: space-between;
            margin-top: 6px;
            padding: 6px 10px;
            background: #f8fafc;
            border-radius: 8px;
        }
        
        .node-stat-label {
            font-weight: 600;
        }
        
        .node-stat-value {
            font-weight: 700;
            color: #1e293b;
        }
        
        .delete-btn {
            background: #fee2e2;
            color: #dc2626;
            border: none;
            width: 28px;
            height: 28px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }
        
        .delete-btn:hover {
            background: #dc2626;
            color: white;
            transform: scale(1.1);
        }
        
        /* React Flow overrides */
        .react-flow__node {
            font-family: 'Tajawal', sans-serif;
        }
        
        .react-flow__edge-path {
            stroke: #3b82f6;
            stroke-width: 2;
        }
        
        .react-flow__edge.selected .react-flow__edge-path {
            stroke: #1d4ed8;
            stroke-width: 3;
        }
        
        .react-flow__handle {
            width: 12px;
            height: 12px;
            background: #3b82f6;
            border: 2px solid white;
        }
        
        .react-flow__handle-right {
            right: -6px;
        }
        
        .react-flow__handle-left {
            left: -6px;
        }
        
        /* Loading Screen */
        .loading-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            color: white;
        }
        
        .loading-spinner {
            width: 60px;
            height: 60px;
            border: 4px solid rgba(255,255,255,0.3);
            border-top-color: white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-bottom: 20px;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .loading-text {
            font-size: 20px;
            font-weight: 700;
        }
        
        /* Toast Notifications */
        .toast {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%) translateY(-100px);
            background: rgba(0,0,0,0.9);
            color: white;
            padding: 14px 24px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 600;
            z-index: 10000;
            transition: transform 0.3s;
            backdrop-filter: blur(10px);
        }
        
        .toast.show {
            transform: translateX(-50%) translateY(0);
        }
        
        /* Status Bar */
        .status-bar {
            position: absolute;
            bottom: 20px;
            right: 20px;
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(20px);
            padding: 10px 20px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            font-size: 12px;
            color: #64748b;
            display: flex;
            gap: 20px;
            z-index: 10;
        }
        
        .status-item {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        
        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #10b981;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        /* Dark Mode */
        .dark-mode .canvas-wrapper {
            background: #0f172a;
        }
        
        .dark-mode .react-flow {
            background: #0f172a;
        }
        
        .dark-mode .react-flow__background {
            background: #0f172a;
        }
        
        .dark-mode .canvas-toolbar {
            background: rgba(30, 41, 59, 0.95);
            border-color: rgba(255,255,255,0.1);
        }
        
        .dark-mode .toolbar-btn {
            background: #334155;
            border-color: #475569;
            color: #e2e8f0;
        }
        
        .dark-mode .circuit-node {
            background: #1e293b;
            border-color: #334155;
        }
        
        .dark-mode .node-title,
        .dark-mode .node-stat-value {
            color: #f1f5f9;
        }
        
        .dark-mode .node-body,
        .dark-mode .node-stat-label {
            color: #94a3b8;
        }
        
        .dark-mode .properties-panel {
            background: #1e293b;
        }
        
        .dark-mode .panel-header {
            color: #f1f5f9;
        }
        
        .dark-mode .input-group label {
            color: #94a3b8;
        }
        
        .dark-mode .input-group input {
            background: #0f172a;
            border-color: #334155;
            color: #f1f5f9;
        }
        
        .dark-mode .status-bar {
            background: rgba(30, 41, 59, 0.95);
            color: #94a3b8;
        }
    </style>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useCallback, useMemo, useEffect, useRef } = React;
        
        // Safe React Flow initialization
        const RF = window.ReactFlow || {};
        const ReactFlowComponent = RF.default || RF.ReactFlow || (() => React.createElement('div', { style: { padding: 40, textAlign: 'center' } }, '⚠️ جاري تحميل المكتبة...'));
        const { 
            Handle, 
            Position, 
            useNodesState, 
            useEdgesState, 
            Background, 
            Controls, 
            MiniMap,
            MarkerType,
            addEdge,
            useReactFlow
        } = RF;

        // Component Types Configuration
        const COMPONENT_TYPES = {
            battery: {
                label: 'بطارية',
                icon: '🔋',
                desc: 'مصدر جهد ثابت',
                color: '#ef4444',
                badge: 'بطارية',
                defaults: { voltage: 12, current: 0, resistance: 0 }
            },
            resistor: {
                label: 'مقاومة',
                icon: '🔴',
                desc: 'مقاومة أومية',
                color: '#f59e0b',
                badge: 'مقاومة',
                defaults: { voltage: 0, current: 0, resistance: 100 }
            },
            led: {
                label: 'LED',
                icon: '💡',
                desc: 'صمام ثنائي باعث للضوء',
                color: '#10b981',
                badge: 'LED',
                defaults: { voltage: 2, current: 0.02, resistance: 100 }
            },
            switch: {
                label: 'مفتاح',
                icon: '🔘',
                desc: 'مفتاح فتح/غلق',
                color: '#8b5cf6',
                badge: 'مفتاح',
                defaults: { closed: true, voltage: 0, current: 0, resistance: 0 }
            },
            capacitor: {
                label: 'مكثف',
                icon: '⚡',
                desc: 'مكثف كهربائي',
                color: '#06b6d4',
                badge: 'مكثف',
                defaults: { capacitance: 100, voltage: 0, current: 0 }
            },
            ammeter: {
                label: 'أميتر',
                icon: '🔵',
                desc: 'مقياس التيار',
                color: '#ec4899',
                badge: 'أميتر',
                defaults: { current: 0, voltage: 0 }
            },
            voltmeter: {
                label: 'فولتميتر',
                icon: '🔷',
                desc: 'مقياس الجهد',
                color: '#6366f1',
                badge: 'فولتميتر',
                defaults: { voltage: 0, current: 0 }
            }
        };

        // Custom Node Component
        const CircuitNode = ({ data, selected, id }) => {
            const componentType = data.type || 'resistor';
            const config = COMPONENT_TYPES[componentType];
            
            const v = Number(data.voltage) || 0;
            const r = Number(data.resistance) || 0;
            const i = Number(data.current) || 0;
            const p = v * i;
            const c = Number(data.capacitance) || 0;
            
            const getDisplayValue = () => {
                if (componentType === 'battery') return `${v}V`;
                if (componentType === 'resistor') return `${r}Ω`;
                if (componentType === 'capacitor') return `${c}μF`;
                if (componentType === 'led') return `${v}V`;
                if (componentType === 'switch') return data.closed ? 'مغلق' : 'مفتوح';
                if (componentType === 'ammeter') return `${i.toFixed(3)}A`;
                if (componentType === 'voltmeter') return `${v.toFixed(2)}V`;
                return '';
            };
            
            return (
                <div className={`circuit-node ${selected ? 'selected' : ''} ${componentType}`}>
                    <Handle type="target" position={Position.Left} />
                    <div className="node-header">
                        <div className="node-title">
                            <span>{config.icon}</span>
                            <span>{data.label || config.label}</span>
                        </div>
                        <span className={`node-badge ${componentType}`}>{getDisplayValue()}</span>
                    </div>
                    <div className="node-body">
                        {componentType !== 'switch' && (
                            <>
                                <div className="node-stat">
                                    <span className="node-stat-label">الجهد:</span>
                                    <span className="node-stat-value">{v.toFixed(2)} V</span>
                                </div>
                                <div className="node-stat">
                                    <span className="node-stat-label">التيار:</span>
                                    <span className="node-stat-value">{i.toFixed(3)} A</span>
                                </div>
                                {r > 0 && (
                                    <div className="node-stat">
                                        <span className="node-stat-label">المقاومة:</span>
                                        <span className="node-stat-value">{r} Ω</span>
                                    </div>
                                )}
                            </>
                        )}
                        {componentType === 'switch' && (
                            <div className="node-stat">
                                <span className="node-stat-label">الحالة:</span>
                                <span className="node-stat-value">{data.closed ? '🟢 مغلق' : '🔴 مفتوح'}</span>
                            </div>
                        )}
                    </div>
                    <Handle type="source" position={Position.Right} />
                </div>
            );
        };

        // Toast Component
        const Toast = ({ message, show }) => (
            <div className={`toast ${show ? 'show' : ''}`}>
                {message}
            </div>
        );

        // Main App Component
        function App() {
            const nodeTypes = useMemo(() => ({
                circuit: CircuitNode
            }), []);
            
            const [nodes, setNodes, onNodesChange] = useNodesState([]);
            const [edges, setEdges, onEdgesChange] = useEdgesState([]);
            const [selectedNode, setSelectedNode] = useState(null);
            const [darkMode, setDarkMode] = useState(false);
            const [toast, setToast] = useState({ show: false, message: '' });
            const [connectionMode, setConnectionMode] = useState(false);
            const [circuitStats, setCircuitStats] = useState({
                totalResistance: 0,
                totalVoltage: 0,
                totalCurrent: 0,
                totalPower: 0,
                nodeCount: 0,
                edgeCount: 0
            });
            
            const reactFlowWrapper = useRef(null);
            
            // Show toast notification
            const showToast = useCallback((message) => {
                setToast({ show: true, message });
                setTimeout(() => setToast({ show: false, message: '' }), 3000);
            }, []);
            
            // Calculate circuit statistics
            const calculateCircuitStats = useCallback(() => {
                const batteries = nodes.filter(n => n.data.type === 'battery');
                const resistors = nodes.filter(n => n.data.type === 'resistor');
                
                const totalVoltage = batteries.reduce((sum, n) => sum + (Number(n.data.voltage) || 0), 0);
                const totalResistance = resistors.reduce((sum, n) => {
                    const r = Number(n.data.resistance) || 0;
                    return r > 0 ? sum + r : sum;
                }, 0);
                
                const totalCurrent = totalResistance > 0 ? totalVoltage / totalResistance : 0;
                const totalPower = totalVoltage * totalCurrent;
                
                setCircuitStats({
                    totalResistance,
                    totalVoltage,
                    totalCurrent,
                    totalPower,
                    nodeCount: nodes.length,
                    edgeCount: edges.length
                });
            }, [nodes, edges]);
            
            useEffect(() => {
                calculateCircuitStats();
            }, [nodes, edges, calculateCircuitStats]);
            
            // Handle node selection
            const onSelectionChange = useCallback(({ nodes: selectedNodes }) => {
                setSelectedNode(selectedNodes.length > 0 ? selectedNodes[0] : null);
            }, []);
            
            // Handle property changes
            const handlePropertyChange = (key, value) => {
                if (!selectedNode) return;
                
                const updatedNodes = nodes.map(node => {
                    if (node.id === selectedNode.id) {
                        const updatedData = { ...node.data, [key]: value };
                        setSelectedNode({ ...node, data: updatedData });
                        return { ...node, data: updatedData };
                    }
                    return node;
                });
                setNodes(updatedNodes);
            };
            
            // Delete selected node
            const deleteSelectedNode = useCallback(() => {
                if (!selectedNode) return;
                
                setNodes(nds => nds.filter(n => n.id !== selectedNode.id));
                setEdges(eds => eds.filter(e => e.source !== selectedNode.id && e.target !== selectedNode.id));
                setSelectedNode(null);
                showToast('تم حذف العنصر ✓');
            }, [selectedNode, showToast]);
            
            // Add new node from drag
            const onDragOver = useCallback((event) => {
                event.preventDefault();
                event.dataTransfer.dropEffect = 'move';
            }, []);
            
            const onDrop = useCallback((event) => {
                event.preventDefault();
                
                const type = event.dataTransfer.getData('application/reactflow');
                if (!type || !COMPONENT_TYPES[type]) return;
                
                const position = reactFlowWrapper.current
                    ? {
                        x: event.clientX - reactFlowWrapper.current.getBoundingClientRect().left,
                        y: event.clientY - reactFlowWrapper.current.getBoundingClientRect().top
                    }
                    : { x: event.clientX, y: event.clientY };
                
                const newNode = {
                    id: `${type}-${Date.now()}`,
                    type: 'circuit',
                    position,
                    data: {
                        type,
                        label: `${COMPONENT_TYPES[type].label} ${nodes.length + 1}`,
                        ...COMPONENT_TYPES[type].defaults
                    }
                };
                
                setNodes(nds => nds.concat(newNode));
                showToast(`تمت إضافة ${COMPONENT_TYPES[type].label} ✓`);
            }, [nodes, showToast]);
            
            // Handle edge connections
            const onConnect = useCallback((params) => {
                setEdges(eds => addEdge({
                    ...params,
                    type: 'smoothstep',
                    animated: true,
                    style: { stroke: '#3b82f6', strokeWidth: 2 },
                    markerEnd: { type: MarkerType.ArrowClosed, color: '#3b82f6' }
                }, eds));
                showToast('تم ربط المكونات ✓');
            }, [showToast]);
            
            // Drag start from sidebar
            const onDragStart = (event, nodeType) => {
                event.dataTransfer.setData('application/reactflow', nodeType);
                event.dataTransfer.effectAllowed = 'move';
            };
            
            // Save circuit to localStorage
            const saveCircuit = useCallback(() => {
                const circuitData = {
                    nodes,
                    edges,
                    timestamp: new Date().toISOString(),
                    stats: circuitStats
                };
                localStorage.setItem('savedCircuit', JSON.stringify(circuitData));
                showToast('تم حفظ الدائرة بنجاح ✓');
            }, [nodes, edges, circuitStats, showToast]);
            
            // Load circuit from localStorage
            const loadCircuit = useCallback(() => {
                const saved = localStorage.getItem('savedCircuit');
                if (saved) {
                    const data = JSON.parse(saved);
                    setNodes(data.nodes || []);
                    setEdges(data.edges || []);
                    showToast('تم تحميل الدائرة ✓');
                } else {
                    showToast('لا توجد دائرة محفوظة');
                }
            }, [showToast]);
            
            // Clear canvas
            const clearCanvas = useCallback(() => {
                if (nodes.length === 0) {
                    showToast('اللوحة فارغة بالفعل');
                    return;
                }
                setNodes([]);
                setEdges([]);
                setSelectedNode(null);
                showToast('تم مسح اللوحة ✓');
            }, [nodes, showToast]);
            
            // Export as PNG
            const exportAsPNG = useCallback(() => {
                showToast('جارٍ تصدير الصورة...');
                // Using html2canvas for export
                const script = document.createElement('script');
                script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
                script.onload = () => {
                    const canvas = document.querySelector('.react-flow');
                    if (canvas && window.html2canvas) {
                        window.html2canvas(canvas).then(canvas => {
                            const link = document.createElement('a');
                            link.download = `circuit-${Date.now()}.png`;
                            link.href = canvas.toDataURL();
                            link.click();
                            showToast('تم تصدير الصورة ✓');
                        });
                    }
                };
                document.head.appendChild(script);
            }, [showToast]);
            
            // Toggle dark mode
            const toggleDarkMode = useCallback(() => {
                setDarkMode(prev => !prev);
                document.body.classList.toggle('dark-mode', !darkMode);
            }, [darkMode]);
            
            // Initial setup
            useEffect(() => {
                // Add initial demo circuit
                const initialNodes = [
                    {
                        id: 'battery-1',
                        type: 'circuit',
                        position: { x: 100, y: 200 },
                        data: { type: 'battery', label: 'بطارية رئيسية', voltage: 12, current: 0 }
                    },
                    {
                        id: 'resistor-1',
                        type: 'circuit',
                        position: { x: 400, y: 150 },
                        data: { type: 'resistor', label: 'مقاومة R1', voltage: 0, current: 0, resistance: 100 }
                    },
                    {
                        id: 'resistor-2',
                        type: 'circuit',
                        position: { x: 400, y: 300 },
                        data: { type: 'resistor', label: 'مقاومة R2', voltage: 0, current: 0, resistance: 200 }
                    },
                    {
                        id: 'led-1',
                        type: 'circuit',
                        position: { x: 700, y: 225 },
                        data: { type: 'led', label: 'LED أخضر', voltage: 2, current: 0.02, resistance: 100 }
                    }
                ];
                
                const initialEdges = [
                    { id: 'e1-2', source: 'battery-1', target: 'resistor-1', type: 'smoothstep', animated: true },
                    { id: 'e1-3', source: 'battery-1', target: 'resistor-2', type: 'smoothstep', animated: true },
                    { id: 'e2-4', source: 'resistor-1', target: 'led-1', type: 'smoothstep', animated: true },
                    { id: 'e3-4', source: 'resistor-2', target: 'led-1', type: 'smoothstep', animated: true }
                ];
                
                setNodes(initialNodes);
                setEdges(initialEdges);
            }, []);
            
            return (
                <div className={`app-container ${darkMode ? 'dark-mode' : ''}`}>
                    {/* Sidebar */}
                    <div className="sidebar">
                        <div className="sidebar-header">
                            <span>🔧</span>
                            <span>صندوق الأدوات</span>
                        </div>
                        
                        <div className="component-section">
                            <div className="section-title">مصادر الطاقة</div>
                            {['battery'].map(type => (
                                <div
                                    key={type}
                                    className="component-item"
                                    draggable
                                    onDragStart={(e) => onDragStart(e, type)}
                                >
                                    <div className="component-icon">{COMPONENT_TYPES[type].icon}</div>
                                    <div className="component-info">
                                        <div className="component-name">{COMPONENT_TYPES[type].label}</div>
                                        <div className="component-desc">{COMPONENT_TYPES[type].desc}</div>
                                    </div>
                                </div>
                            ))}
                        </div>
                        
                        <div className="component-section">
                            <div className="section-title">المكونات السلبية</div>
                            {['resistor', 'capacitor'].map(type => (
                                <div
                                    key={type}
                                    className="component-item"
                                    draggable
                                    onDragStart={(e) => onDragStart(e, type)}
                                >
                                    <div className="component-icon">{COMPONENT_TYPES[type].icon}</div>
                                    <div className="component-info">
                                        <div className="component-name">{COMPONENT_TYPES[type].label}</div>
                                        <div className="component-desc">{COMPONENT_TYPES[type].desc}</div>
                                    </div>
                                </div>
                            ))}
                        </div>
                        
                        <div className="component-section">
                            <div className="section-title">أشباه الموصلات</div>
                            {['led', 'switch'].map(type => (
                                <div
                                    key={type}
                                    className="component-item"
                                    draggable
                                    onDragStart={(e) => onDragStart(e, type)}
                                >
                                    <div className="component-icon">{COMPONENT_TYPES[type].icon}</div>
                                    <div className="component-info">
                                        <div className="component-name">{COMPONENT_TYPES[type].label}</div>
                                        <div className="component-desc">{COMPONENT_TYPES[type].desc}</div>
                                    </div>
                                </div>
                            ))}
                        </div>
                        
                        <div className="component-section">
                            <div className="section-title">أجهزة القياس</div>
                            {['ammeter', 'voltmeter'].map(type => (
                                <div
                                    key={type}
                                    className="component-item"
                                    draggable
                                    onDragStart={(e) => onDragStart(e, type)}
                                >
                                    <div className="component-icon">{COMPONENT_TYPES[type].icon}</div>
                                    <div className="component-info">
                                        <div className="component-name">{COMPONENT_TYPES[type].label}</div>
                                        <div className="component-desc">{COMPONENT_TYPES[type].desc}</div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                    
                    {/* Main Canvas */}
                    <div className="canvas-wrapper" ref={reactFlowWrapper}>
                        <div className="canvas-toolbar">
                            <button className="toolbar-btn" onClick={saveCircuit}>
                                <span>💾</span> حفظ
                            </button>
                            <button className="toolbar-btn" onClick={loadCircuit}>
                                <span>📂</span> تحميل
                            </button>
                            <button className="toolbar-btn" onClick={exportAsPNG}>
                                <span>📸</span> تصدير
                            </button>
                            <button className="toolbar-btn" onClick={toggleDarkMode}>
                                <span>{darkMode ? '☀️' : '🌙'}</span> {darkMode ? 'نهاري' : 'ليلي'}
                            </button>
                            <button className="toolbar-btn danger" onClick={clearCanvas}>
                                <span>🗑️</span> مسح
                            </button>
                        </div>
                        
                        {typeof ReactFlowComponent === 'function' ? (
                            <ReactFlowComponent
                                nodes={nodes}
                                edges={edges}
                                onNodesChange={onNodesChange}
                                onEdgesChange={onEdgesChange}
                                onSelectionChange={onSelectionChange}
                                onConnect={onConnect}
                                onDragOver={onDragOver}
                                onDrop={onDrop}
                                nodeTypes={nodeTypes}
                                fitView
                                attributionPosition="bottom-left"
                            >
                                <Background color={darkMode ? '#334155' : '#cbd5e1'} gap={16} size={1} />
                                <Controls />
                                <MiniMap 
                                    nodeColor={(n) => {
                                        const type = n.data?.type || 'resistor';
                                        return COMPONENT_TYPES[type]?.color || '#3b82f6';
                                    }}
                                    style={{ backgroundColor: darkMode ? '#1e293b' : '#f8fafc' }}
                                />
                            </ReactFlowComponent>
                        ) : (
                            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%', flexDirection: 'column' }}>
                                <div style={{ fontSize: 48, marginBottom: 20 }}>⚡</div>
                                <div style={{ fontSize: 18, color: '#64748b' }}>جاري تحميل المختبر الكهربائي...</div>
                            </div>
                        )}
                        
                        <div className="status-bar">
                            <div className="status-item">
                                <div className="status-dot"></div>
                                <span>متصل</span>
                            </div>
                            <div className="status-item">
                                <span>📦 العناصر: {circuitStats.nodeCount}</span>
                            </div>
                            <div className="status-item">
                                <span>🔗 الروابط: {circuitStats.edgeCount}</span>
                            </div>
                            <div className="status-item">
                                <span>⚡ الطاقة: {circuitStats.totalPower.toFixed(2)}W</span>
                            </div>
                        </div>
                    </div>
                    
                    {/* Properties Panel */}
                    <div className="properties-panel">
                        <div className="panel-header">
                            <span>⚙️</span>
                            <span>خصائص العنصر</span>
                        </div>
                        
                        {selectedNode ? (
                            <>
                                <div className="input-group">
                                    <label>اسم العنصر</label>
                                    <input
                                        type="text"
                                        value={selectedNode.data.label || ''}
                                        onChange={(e) => handlePropertyChange('label', e.target.value)}
                                        placeholder="أدخل اسم العنصر"
                                    />
                                </div>
                                
                                {selectedNode.data.type === 'battery' && (
                                    <div className="input-group">
                                        <label>فولتية البطارية (V)</label>
                                        <input
                                            type="number"
                                            value={selectedNode.data.voltage || 0}
                                            onChange={(e) => handlePropertyChange('voltage', Number(e.target.value))}
                                            step="0.1"
                                        />
                                    </div>
                                )}
                                
                                {selectedNode.data.type === 'resistor' && (
                                    <div className="input-group">
                                        <label>قيمة المقاومة (Ω)</label>
                                        <input
                                            type="number"
                                            value={selectedNode.data.resistance || 0}
                                            onChange={(e) => handlePropertyChange('resistance', Number(e.target.value))}
                                            step="1"
                                        />
                                    </div>
                                )}
                                
                                {selectedNode.data.type === 'capacitor' && (
                                    <div className="input-group">
                                        <label>سعة المكثف (μF)</label>
                                        <input
                                            type="number"
                                            value={selectedNode.data.capacitance || 0}
                                            onChange={(e) => handlePropertyChange('capacitance', Number(e.target.value))}
                                            step="1"
                                        />
                                    </div>
                                )}
                                
                                {selectedNode.data.type === 'switch' && (
                                    <div className="input-group">
                                        <label>حالة المفتاح</label>
                                        <select
                                            value={selectedNode.data.closed ? 'closed' : 'open'}
                                            onChange={(e) => handlePropertyChange('closed', e.target.value === 'closed')}
                                        >
                                            <option value="closed">مغلق (ON)</option>
                                            <option value="open">مفتوح (OFF)</option>
                                        </select>
                                    </div>
                                )}
                                
                                {selectedNode.data.type !== 'switch' && (
                                    <>
                                        <div className="input-group">
                                            <label>الجهد المطبق (V)</label>
                                            <input
                                                type="number"
                                                value={selectedNode.data.voltage || 0}
                                                onChange={(e) => handlePropertyChange('voltage', Number(e.target.value))}
                                                step="0.1"
                                            />
                                        </div>
                                    </>
                                )}
                                
                                <div className="metrics-card">
                                    <div className="metrics-title">
                    
