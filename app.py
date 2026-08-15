import streamlit as st
import streamlit.components.v1 as components
import os
import tempfile
import base64

st.set_page_config(
    page_title="المختبر التفاعلي للدوائر الكهربائية",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header styling
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

# Create HTML content as a function to avoid string parsing issues
def get_html_content():
    return '''<!DOCTYPE html>
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
        
        .toolbar-btn.danger:hover {
            background: #ef4444;
            border-color: #ef4444;
            box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
        }
        
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

    <script>
        // Load React Flow safely
        window.addEventListener('DOMContentLoaded', function() {
            const RF = window.ReactFlow || {};
            const ReactFlowComponent = RF.default || RF.ReactFlow || function() {
                return React.createElement('div', { style: { padding: 40, textAlign: 'center', color: '#64748b' } }, '⚠️ جاري تحميل المكتبة...');
            };
            
            const Handle = RF.Handle;
            const Position = RF.Position;
            const useNodesState = RF.useNodesState;
            const useEdgesState = RF.useEdgesState;
            const Background = RF.Background;
            const Controls = RF.Controls;
            const MiniMap = RF.MiniMap;
            const MarkerType = RF.MarkerType;
            const addEdge = RF.addEdge;
            
            const COMPONENT_TYPES = {
                battery: { label: 'بطارية', icon: '🔋', desc: 'مصدر جهد ثابت', color: '#ef4444', defaults: { voltage: 12, current: 0, resistance: 0 } },
                resistor: { label: 'مقاومة', icon: '🔴', desc: 'مقاومة أومية', color: '#f59e0b', defaults: { voltage: 0, current: 0, resistance: 100 } },
                led: { label: 'LED', icon: '💡', desc: 'صمام ثاعي باعث للضوء', color: '#10b981', defaults: { voltage: 2, current: 0.02, resistance: 100 } },
                switch: { label: 'مفتاح', icon: '🔘', desc: 'مفتاح فتح/غلق', color: '#8b5cf6', defaults: { closed: true, voltage: 0, current: 0, resistance: 0 } },
                capacitor: { label: 'مكثف', icon: '⚡', desc: 'مكثف كهربائي', color: '#06b6d4', defaults: { capacitance: 100, voltage: 0, current: 0 } },
                ammeter: { label: 'أميتر', icon: '🔵', desc: 'مقياس التيار', color: '#ec4899', defaults: { current: 0, voltage: 0 } },
                voltmeter: { label: 'فولتميتر', icon: '🔷', desc: 'مقياس الجهد', color: '#6366f1', defaults: { voltage: 0, current: 0 } }
            };

            function CircuitNode(props) {
                const data = props.data || {};
                const selected = props.selected || false;
                const componentType = data.type || 'resistor';
                const config = COMPONENT_TYPES[componentType];
                
                const v = Number(data.voltage) || 0;
                const r = Number(data.resistance) || 0;
                const i = Number(data.current) || 0;
                
                const getDisplayValue = function() {
                    if (componentType === 'battery') return v + 'V';
                    if (componentType === 'resistor') return r + 'Ω';
                    if (componentType === 'capacitor') return (Number(data.capacitance) || 0) + 'μF';
                    if (componentType === 'led') return v + 'V';
                    if (componentType === 'switch') return data.closed ? 'مغلق' : 'مفتوح';
                    if (componentType === 'ammeter') return i.toFixed(3) + 'A';
                    if (componentType === 'voltmeter') return v.toFixed(2) + 'V';
                    return '';
                };
                
                return React.createElement('div', {
                    className: 'circuit-node ' + (selected ? 'selected' : '') + ' ' + componentType
                }, [
                    React.createElement(Handle, { key: 'target', type: 'target', position: Position.Left }),
                    React.createElement('div', { key: 'header', className: 'node-header' }, [
                        React.createElement('div', { key: 'title', className: 'node-title' }, [
                            React.createElement('span', { key: 'icon' }, config.icon),
                            React.createElement('span', { key: 'label' }, data.label || config.label)
                        ]),
                        React.createElement('span', { key: 'badge', className: 'node-badge ' + componentType }, getDisplayValue())
                    ]),
                    React.createElement('div', { key: 'body', className: 'node-body' }, 
                        componentType !== 'switch' ? [
                            React.createElement('div', { key: 'v', className: 'node-stat' }, [
                                React.createElement('span', { key: 'l', className: 'node-stat-label' }, 'الجهد:'),
                                React.createElement('span', { key: 'v', className: 'node-stat-value' }, v.toFixed(2) + ' V')
                            ]),
                            React.createElement('div', { key: 'i', className: 'node-stat' }, [
                                React.createElement('span', { key: 'l', className: 'node-stat-label' }, 'التيار:'),
                                React.createElement('span', { key: 'i', className: 'node-stat-value' }, i.toFixed(3) + ' A')
                            ]),
                            r > 0 ? React.createElement('div', { key: 'r', className: 'node-stat' }, [
                                React.createElement('span', { key: 'l', className: 'node-stat-label' }, 'المقاومة:'),
                                React.createElement('span', { key: 'r', className: 'node-stat-value' }, r + ' Ω')
                            ]) : null
                        ] : [
                            React.createElement('div', { key: 's', className: 'node-stat' }, [
                                React.createElement('span', { key: 'l', className: 'node-stat-label' }, 'الحالة:'),
                                React.createElement('span', { key: 's', className: 'node-stat-value' }, data.closed ? '🟢 مغلق' : '🔴 مفتوح')
                            ])
                        ]
                    ),
                    React.createElement(Handle, { key: 'source', type: 'source', position: Position.Right })
                ]);
            }

            function App() {
                const [nodes, setNodes, onNodesChange] = useNodesState([]);
                const [edges, setEdges, onEdgesChange] = useEdgesState([]);
                const [selectedNode, setSelectedNode] = React.useState(null);
                const [darkMode, setDarkMode] = React.useState(false);
                const [toast, setToast] = React.useState({ show: false, message: '' });
                const reactFlowWrapper = React.useRef(null);
                
                const showToast = React.useCallback(function(message) {
                    setToast({ show: true, message: message });
                    setTimeout(function() { setToast({ show: false, message: '' }); }, 3000);
                }, []);
                
                React.useEffect(function() {
                    const initialNodes = [
                        { id: 'battery-1', type: 'circuit', position: { x: 100, y: 200 }, data: { type: 'battery', label: 'بطارية رئيسية', voltage: 12, current: 0 } },
                        { id: 'resistor-1', type: 'circuit', position: { x: 400, y: 150 }, data: { type: 'resistor', label: 'مقاومة R1', voltage: 0, current: 0, resistance: 100 } },
                        { id: 'resistor-2', type: 'circuit', position: { x: 400, y: 300 }, data: { type: 'resistor', label: 'مقاومة R2', voltage: 0, current: 0, resistance: 200 } },
                        { id: 'led-1', type: 'circuit', position: { x: 700, y: 225 }, data: { type: 'led', label: 'LED أخضر', voltage: 2, current: 0.02, resistance: 100 } }
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
                
                const onSelectionChange = React.useCallback(function(params) {
                    const selectedNodes = params.nodes || [];
                    setSelectedNode(selectedNodes.length > 0 ? selectedNodes[0] : null);
                }, []);
                
                const handlePropertyChange = function(key, value) {
                    if (!selectedNode) return;
                    const updatedNodes = nodes.map(function(node) {
                        if (node.id === selectedNode.id) {
                            const updatedData = Object.assign({}, node.data, { [key]: value });
                            setSelectedNode(Object.assign({}, node, { data: updatedData }));
                            return Object.assign({}, node, { data: updatedData });
                        }
                        return node;
                    });
                    setNodes(updatedNodes);
                };
                
                const deleteSelectedNode = React.useCallback(function() {
                    if (!selectedNode) return;
                    setNodes(function(nds) { return nds.filter(function(n) { return n.id !== selectedNode.id; }); });
                    setEdges(function(eds) { return eds.filter(function(e) { return e.source !== selectedNode.id && e.target !== selectedNode.id; }); });
                    setSelectedNode(null);
                    showToast('تم حذف العنصر ✓');
                }, [selectedNode, showToast]);
                
                const onDragOver = React.useCallback(function(event) {
                    event.preventDefault();
                    event.dataTransfer.dropEffect = 'move';
                }, []);
                
                const onDrop = React.useCallback(function(event) {
                    event.preventDefault();
                    const type = event.dataTransfer.getData('application/reactflow');
                    if (!type || !COMPONENT_TYPES[type]) return;
                    
                    const position = {
                        x: event.clientX - 300,
                        y: event.clientY - 100
                    };
                    
                    const newNode = {
                        id: type + '-' + Date.now(),
                        type: 'circuit',
                        position: position,
                        data: Object.assign({ type: type, label: COMPONENT_TYPES[type].label + ' ' + (nodes.length + 1) }, COMPONENT_TYPES[type].defaults)
                    };
                    
                    setNodes(function(nds) { return nds.concat(newNode); });
                    showToast('تمت إضافة ' + COMPONENT_TYPES[type].label + ' ✓');
                }, [nodes, showToast]);
                
                const onConnect = React.useCallback(function(params) {
                    setEdges(function(eds) {
                        return addEdge(Object.assign({}, params, {
                            type: 'smoothstep',
                            animated: true,
                            style: { stroke: '#3b82f6', strokeWidth: 2 }
                        }), eds);
                    });
                    showToast('تم ربط المكونات ✓');
                }, [showToast]);
                
                const onDragStart = function(event, nodeType) {
                    event.dataTransfer.setData('application/reactflow', nodeType);
                    event.dataTransfer.effectAllowed = 'move';
                };
                
                const saveCircuit = React.useCallback(function() {
                    const circuitData = { nodes: nodes, edges: edges, timestamp: new Date().toISOString() };
                    localStorage.setItem('savedCircuit', JSON.stringify(circuitData));
                    showToast('تم حفظ الدائرة بنجاح ✓');
                }, [nodes, edges, showToast]);
                
                const loadCircuit = React.useCallback(function() {
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
                
                const clearCanvas = React.useCallback(function() {
                    if (nodes.length === 0) {
                        showToast('اللوحة فارغة بالفعل');
                        return;
                    }
                    setNodes([]);
                    setEdges([]);
                    setSelectedNode(null);
                    showToast('تم مسح اللوحة ✓');
                }, [nodes, showToast]);
                
                const toggleDarkMode = React.useCallback(function() {
                    setDarkMode(function(prev) { return !prev; });
                    document.body.classList.toggle('dark-mode', !darkMode);
                }, [darkMode]);
                
                const nodeTypes = React.useMemo(function() { return { circuit: CircuitNode }; }, []);
                
                const circuitStats = React.useMemo(function() {
                    const batteries = nodes.filter(function(n) { return n.data && n.data.type === 'battery'; });
                    const resistors = nodes.filter(function(n) { return n.data && n.data.type === 'resistor'; });
                    
                    const totalVoltage = batteries.reduce(function(sum, n) { return sum + (Number(n.data.voltage) || 0); }, 0);
                    const totalResistance = resistors.reduce(function(sum, n) {
                        const r = Number(n.data.resistance) || 0;
                        return r > 0 ? sum + r : sum;
                    }, 0);
                    
                    const totalCurrent = totalResistance > 0 ? totalVoltage / totalResistance : 0;
                    const totalPower = totalVoltage * totalCurrent;
                    
                    return {
                        totalResistance: totalResistance,
                        totalVoltage: totalVoltage,
                        totalCurrent: totalCurrent,
                        totalPower: totalPower,
                        nodeCount: nodes.length,
                        edgeCount: edges.length
                    };
                }, [nodes, edges]);
                
                return React.createElement('div', { className: 'app-container' + (darkMode ? ' dark-mode' : '') }, [
                    React.createElement('div', { key: 'sidebar', className: 'sidebar' }, [
                        React.createElement('div', { key: 'header', className: 'sidebar-header' }, [
                            React.createElement('span', { key: 'icon' }, '🔧'),
                            React.createElement('span', { key: 'title' }, 'صندوق الأدوات')
                        ]),
                        React.createElement('div', { key: 'power', className: 'component-section' }, [
                            React.createElement('div', { key: 'title', className: 'section-title' }, 'مصادر الطاقة'),
                            React.createElement('div', {
                                key: 'battery',
                                className: 'component-item',
                                draggable: true,
                                onDragStart: function(e) { onDragStart(e, 'battery'); }
                            }, [
                                React.createElement('div', { key: 'icon', className: 'component-icon' }, COMPONENT_TYPES.battery.icon),
                                React.createElement('div', { key: 'info', className: 'component-info' }, [
                                    React.createElement('div', { key: 'name', className: 'component-name' }, COMPONENT_TYPES.battery.label),
                                    React.createElement('div', { key: 'desc', className: 'component-desc' }, COMPONENT_TYPES.battery.desc)
                                ])
                            ])
                        ]),
                        React.createElement('div', { key: 'passive', className: 'component-section' }, [
                            React.createElement('div', { key: 'title', className: 'section-title' }, 'المكونات السلبية'),
                            ['resistor', 'capacitor'].map(function(type) {
                                return React.createElement('div', {
                                    key: type,
                                    className: 'component-item',
                                    draggable: true,
                                    onDragStart: function(e) { onDragStart(e, type); }
                                }, [
                                    React.createElement('div', { key: 'icon', className: 'component-icon' }, COMPONENT_TYPES[type].icon),
                                    React.createElement('div', { key: 'info', className: 'component-info' }, [
                                        React.createElement('div', { key: 'name', className: 'component-name' }, COMPONENT_TYPES[type].label),
                                        React.createElement('div', { key: 'desc', className: 'component-desc' }, COMPONENT_TYPES[type].desc)
                                    ])
                                ]);
                            })
                        ]),
                        React.createElement('div', { key: 'semi', className: 'component-section' }, [
                            React.createElement('div', { key: 'title', className: 'section-title' }, 'أشباه الموصلات'),
                            ['led', 'switch'].map(function(type) {
                                return React.createElement('div', {
                                    key: type,
                                    className: 'component-item',
                                    draggable: true,
                                    onDragStart: function(e) { onDragStart(e, type); }
                                }, [
                                    React.createElement('div', { key: 'icon', className: 'component-icon' }, COMPONENT_TYPES[type].icon),
                                    React.createElement('div', { key: 'info', className: 'component-info' }, [
                                        React.createElement('div', { key: 'name', className: 'component-name' }, COMPONENT_TYPES[type].label),
                                        React.createElement('div', { key: 'desc', className: 'component-desc' }, COMPONENT_TYPES[type].desc)
                                    ])
                                ]);
                            })
                        ]),
                        React.createElement('div', { key: 'measure', className: 'component-section' }, [
                            React.createElement('div', { key: 'title', className: 'section-title' }, 'أجهزة القياس'),
                            ['ammeter', 'voltmeter'].map(function(type) {
                                return React.createElement('div', {
                                    key: type,
                                    className: 'component-item',
                                    draggable: true,
                                    onDragStart: function(e) { onDragStart(e, type); }
                                }, [
                                    React.createElement('div', { key: 'icon', className: 'component-icon' }, COMPONENT_TYPES[type].icon),
                                    React.createElement('div', { key: 'info', className: 'component-info' }, [
                                        React.createElement('div', { key: 'name', className: 'component-name' }, COMPONENT_TYPES[type].label),
                                        React.createElement('div', { key: 'desc', className: 'component-desc' }, COMPONENT_TYPES[type].desc)
                                    ])
                                ]);
                            })
                        ])
                    ]),
                    React.createElement('div', { key: 'canvas', className: 'canvas-wrapper', ref: reactFlowWrapper }, [
                        React.createElement('div', { key: 'toolbar', className: 'canvas-toolbar' }, [
                            React.createElement('button', { key: 'save', className: 'toolbar-btn', onClick: saveCircuit }, [
                                React.createElement('span', { key: 'icon' }, '💾'),
                                React.createElement('span', { key: 'text' }, 'حفظ')
                            ]),
                            React.createElement('button', { key: 'load', className: 'toolbar-btn', onClick: loadCircuit }, [
                                React.createElement('span', { key: 'icon' }, '📂'),
                                React.createElement('span', { key: 'text' }, 'تحميل')
                            ]),
                            React.createElement('button', { key: 'mode', className: 'toolbar-btn', onClick: toggleDarkMode }, [
                                React.createElement('span', { key: 'icon' }, darkMode ? '☀️' : '🌙'),
                                React.createElement('span', { key: 'text' }, darkMode ? 'نهاري' : 'ليلي')
                            ]),
                            React.createElement('button', { key: 'clear', className: 'toolbar-btn danger', onClick: clearCanvas }, [
                                React.createElement('span', { key: 'icon' }, '🗑️'),
                                React.createElement('span', { key: 'text' }, 'مسح')
                            ])
                        ]),
                        React.createElement(ReactFlowComponent, {
                            key: 'flow',
                            nodes: nodes,
                            edges: edges,
                            onNodesChange: onNodesChange,
                            onEdgesChange: onEdgesChange,
                            onSelectionChange: onSelectionChange,
                            onConnect: onConnect,
                            onDragOver: onDragOver,
                            onDrop: onDrop,
                            nodeTypes: nodeTypes,
                            fitView: true,
                            attributionPosition: 'bottom-left'
                        }, [
                            React.createElement(Background, { key: 'bg', color: darkMode ? '#334155' : '#cbd5e1', gap: 16, size: 1 }),
                            React.createElement(Controls, { key: 'ctrl' }),
                            React.createElement(MiniMap, {
                                key: 'map',
                                nodeColor: function(n) {
                                    const type = (n.data && n.data.type) || 'resistor';
                                    return COMPONENT_TYPES[type] ? COMPONENT_TYPES[type].color : '#3b82f6';
                                },
                                style: { backgroundColor: darkMode ? '#1e293b' : '#f8fafc' }
                            })
                        ]),
                        React.createElement('div', { key: 'status', className: 'status-bar' }, [
                            React.createElement('div', { key: 'conn', className: 'status-item' }, [
                                React.createElement('div', { key: 'dot', className: 'status-dot' }),
                                React.createElement('span', { key: 'text' }, 'متصل')
                            ]),
                            React.createElement('div', { key: 'nodes', className: 'status-item' }, [
                                React.createElement('span', { key: 'text' }, '📦 العناصر: ' + circuitStats.nodeCount)
                            ]),
                            React.createElement('div', { key: 'edges', className: 'status-item' }, [
                                React.createElement('span', { key: 'text' }, '🔗 الروابط: ' + circuitStats.edgeCount)
                            ]),
                            React.createElement('div', { key: 'power', className: 'status-item' }, [
                                React.createElement('span', { key: 'text' }, '⚡ الطاقة: ' + circuitStats.totalPower.toFixed(2) + 'W')
                            ])
                        ])
                    ]),
                    React.createElement('div', { key: 'props', className: 'properties-panel' }, [
                        React.createElement('div', { key: 'header', className: 'panel-header' }, [
                            React.createElement('span', { key: 'icon' }, '⚙️'),
                            React.createElement('span', { key: 'text' }, 'خصائص العنصر')
                        ]),
                        selectedNode ? [
                            React.createElement('div', { key: 'label', className: 'input-group' }, [
                                React.createElement('label', { key: 'l' }, 'اسم العنصر'),
                                React.createElement('input', {
                                    key: 'i',
                                    type: 'text',
                                    value: selectedNode.data.label || '',
                                    onChange: function(e) { handlePropertyChange('label', e.target.value); }
                                })
                            ]),
                            selectedNode.data.type === 'battery' ? React.createElement('div', { key: 'voltage', className: 'input-group' }, [
                                React.createElement('label', { key: 'l' }, 'فولتية البطارية (V)'),
                                React.createElement('input', {
                                    key: 'i',
                                    type: 'number',
                                    value: selectedNode.data.voltage || 0,
                                    onChange: function(e) { handlePropertyChange('voltage', Number(e.target.value)); },
                                    step: '0.1'
                                })
                            ]) : null,
                            selectedNode.data.type === 'resistor' ? React.createElement('div', { key: 'resistance', className: 'input-group' }, [
                                React.createElement('label', { key: 'l' }, 'قيمة المقاومة (Ω)'),
                                React.createElement('input', {
                                    key: 'i',
                                    type: 'number',
                                    value: selectedNode.data.resistance || 0,
                                    onChange: function(e) { handlePropertyChange('resistance', Number(e.target.value)); },
                                    step: '1'
                                })
                            ]) : null,
                            selectedNode.data.type === 'switch' ? React.createElement('div', { key: 'switch', className: 'input-group' }, [
                                React.createElement('label', { key: 'l' }, 'حالة المفتاح'),
                                React.createElement('select', {
                                    key: 's',
                                    value: selectedNode.data.closed ? 'closed' : 'open',
                                    onChange: function(e) { handlePropertyChange('closed', e.target.value === 'closed'); }
                                }, [
                                    React.createElement('option', { key: 'c', value: 'closed' }, 'مغلق (ON)'),
                                    React.createElement('option', { key: 'o', value: 'open' }, 'مفتوح (OFF)')
                                ])
                            ]) : null,
                            React.createElement('div', { key: 'metrics', className: 'metrics-card' }, [
                                React.createElement('div', { key: 'title', className: 'metrics-title' }, [
                                    React.createElement('span', { key: 'icon' }, '📊'),
                                    React.createElement('span', { key: 'text' }, 'التحليل الكهربائي')
                                ]),
                                React.createElement('div', { key: 'v', className: 'metric-row' }, [
                                    React.createElement('span', { key: 'l', className: 'metric-label' }, 'الجهد (V):'),
                                    React.createElement('span', { key: 'v', className: 'metric-value' }, (Number(selectedNode.data.voltage) || 0).toFixed(2) + ' V')
                                ]),
                                React.createElement('div', { key: 'i', className: 'metric-row' }, [
                                    React.createElement('span', { key: 'l', className: 'metric-label' }, 'التيار (I):'),
                                    React.createElement('span', { key: 'i', className: 'metric-value' }, (Number(selectedNode.data.current) || 0).toFixed(3) + ' A')
                                ]),
                                selectedNode.data.resistance > 0 ? React.createElement('div', { key: 'r', className: 'metric-row' }, [
                                    React.createElement('span', { key: 'l', className: 'metric-label' }, 'المقاومة (R):'),
                                    React.createElement('span', { key: 'r', className: 'metric-value' }, selectedNode.data.resistance + ' Ω')
                                ]) : null,
                                React.createElement('div', { key: 'p', className: 'metric-row' }, [
                                    React.createElement('span', { key: 'l', className: 'metric-label' }, 'القدرة (P):'),
                                    React.createElement('span', { key: 'p', className: 'metric-value' }, ((Number(selectedNode.data.voltage) || 0) * (Number(selectedNode.data.current) || 0)).toFixed(3) + ' W')
                                ])
                            ]),
                            React.createElement('button', {
                                key: 'delete',
                                className: 'toolbar-btn danger',
                                onClick: deleteSelectedNode,
                                style: { width: '100%', marginTop: '20px', justifyContent: 'center' }
                            }, [
                                React.createElement('span', { key: 'icon' }, '🗑️'),
                                React.createElement('span', { key: 'text' }, 'حذف العنصر')
             
