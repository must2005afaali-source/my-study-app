import streamlit as st
import base64

st.set_page_config(page_title="المختبر التفاعلي للدوائر الكهربائية", layout="wide")

# إخفاء التذييل
st.markdown("""
    <style>
        .block-container { padding: 1rem 2rem; }
        footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# كود الـ HTML الخاص بك (تم الإبقاء عليه كما هو)
react_flow_html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script src="https://unpkg.com/reactflow@11.10.1/dist/umd/index.js"></script>
  <link rel="stylesheet" href="https://unpkg.com/reactflow@11.10.1/dist/style.css" />
  <style>
    * { font-family: 'Tajawal', sans-serif; box-sizing: border-box; }
    body, html, #root { width: 100%; height: 100%; margin: 0; padding: 0; background-color: #f4f6f9; overflow: hidden; }
    .app-layout { display: flex; width: 100vw; height: 100vh; position: relative; }
    .top-toolbar { position: absolute; top: 15px; right: 310px; z-index: 10; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(8px); padding: 8px 16px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); display: flex; gap: 10px; align-items: center; border: 1px solid #e2e8f0; }
    .btn-add { background: #3b82f6; color: white; border: none; padding: 8px 14px; border-radius: 8px; cursor: pointer; font-weight: 600; display: flex; align-items: center; gap: 6px; transition: all 0.2s; font-size: 13px; }
    .btn-add:hover { background: #2563eb; transform: translateY(-1px); }
    .properties-panel { width: 290px; height: 100%; background: #ffffff; border-left: 1px solid #e2e8f0; padding: 20px; box-shadow: -4px 0 15px rgba(0,0,0,0.03); z-index: 5; overflow-y: auto; }
    .panel-header { font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 20px; display: flex; align-items: center; gap: 8px; }
    .input-group { margin-bottom: 16px; }
    .input-group label { display: block; font-size: 13px; font-weight: 600; color: #64748b; margin-bottom: 6px; }
    .input-group input { width: 100%; padding: 10px 12px; border: 1.5px solid #e2e8f0; border-radius: 8px; font-size: 14px; transition: border-color 0.2s; outline: none; }
    .input-group input:focus { border-color: #3b82f6; }
    .metrics-card { background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border: 1px solid #bfdbfe; border-radius: 12px; padding: 15px; margin-top: 20px; }
    .metrics-title { font-weight: 700; color: #1e40af; font-size: 14px; margin-bottom: 10px; }
    .metric-row { display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 13px; color: #1e3a8a; }
    .custom-node { background: #ffffff; border-radius: 12px; padding: 14px; min-width: 170px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); border: 2px solid #e2e8f0; transition: all 0.2s; }
    .custom-node.selected { border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2); }
    .node-title { font-weight: 700; font-size: 14px; color: #0f172a; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center; }
    .node-badge { background: #e0e7ff; color: #3730a3; font-size: 10px; padding: 2px 6px; border-radius: 6px; font-weight: 700; }
    .node-body { font-size: 12px; color: #475569; }
    .node-stat { display: flex; justify-content: space-between; margin-top: 4px; }
  </style>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
    const { useState, useCallback, useMemo } = React;
    const { ReactFlow, Handle, Position, useNodesState, useEdgesState, Background, Controls } = ReactFlowRenderer;

    const ComponentNode = ({ data, selected }) => {
      const v = Number(data.voltage) || 0;
      const r = Number(data.resistance) || 1;
      const i = r > 0 ? v / r : 0;
      const p = v * i;
      return (
        <div className={`custom-node ${selected ? 'selected' : ''}`}>
          <Handle type="target" position={Position.Left} style={{ background: '#3b82f6', width: 10, height: 10 }} />
          <div className="node-title"><span>⚡ {data.label || 'عنصر كهربائي'}</span><span className="node-badge">{r} Ω</span></div>
          <div className="node-body">
            <div className="node-stat"><span>الجهد:</span> <strong>{v} V</strong></div>
            <div className="node-stat"><span>التيار:</span> <strong style={{ color: '#2563eb' }}>{i.toFixed(2)} A</strong></div>
            <div className="node-stat"><span>القدرة:</span> <strong style={{ color: '#d97706' }}>{p.toFixed(2)} W</strong></div>
          </div>
          <Handle type="source" position={Position.Right} style={{ background: '#3b82f6', width: 10, height: 10 }} />
        </div>
      );
    };

    const initialNodes = [
      { id: '1', type: 'component', position: { x: 80, y: 120 }, data: { label: 'مقاومة الحمل R1', voltage: 12, resistance: 10 } },
      { id: '2', type: 'component', position: { x: 340, y: 120 }, data: { label: 'مقاومة الحماية R2', voltage: 24, resistance: 50 } }
    ];

    function App() {
      const nodeTypes = useMemo(() => ({ component: ComponentNode }), []);
      const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
      const [edges, setEdges, onEdgesChange] = useEdgesState([]);
      const [selectedNode, setSelectedNode] = useState(initialNodes[0]);
      const onSelectionChange = useCallback(({ nodes }) => { setSelectedNode(nodes.length > 0 ? nodes[0] : null); }, []);
      
      const handleChange = (key, val) => {
        if (!selectedNode) return;
        const updatedNodes = nodes.map((node) => {
          if (node.id === selectedNode.id) {
            const updatedData = { ...node.data, [key]: val };
            setSelectedNode({ ...node, data: updatedData });
            return { ...node, data: updatedData };
          }
          return node;
        });
        setNodes(updatedNodes);
      };

      const addNode = () => {
        const newId = String(nodes.length + 1);
        const newNode = { id: newId, type: 'component', position: { x: 150 + nodes.length * 30, y: 180 }, data: { label: `مقاومة R${newId}`, voltage: 12, resistance: 20 } };
        setNodes((nds) => nds.concat(newNode));
      };

      const v = selectedNode ? Number(selectedNode.data.voltage) || 0 : 0;
      const r = selectedNode ? Number(selectedNode.data.resistance) || 0 : 0;
      const i = r > 0 ? v / r : 0;
      const p = v * i;

      return (
        <div className="app-layout">
          <div className="top-toolbar"><button className="btn-add" onClick={addNode}>➕ إضافة عنصر جديد</button></div>
          <div style={{ flexGrow: 1, height: '100%' }}>
            <ReactFlow nodes={nodes} edges={edges} onNodesChange={onNodesChange} onEdgesChange={onEdgesChange} onSelectionChange={onSelectionChange} nodeTypes={nodeTypes} fitView>
              <Background color="#cbd5e1" gap={16} size={1} /><Controls />
            </ReactFlow>
          </div>
          <div className="properties-panel">
            <div className="panel-header">⚙️ لوحة خصائص العنصر</div>
            {selectedNode ? (
              <>
                <div className="input-group"><label>اسم المكون</label><input type="text" value={selectedNode.data.label} onChange={(e) => handleChange('label', e.target.value)} /></div>
                <div className="input-group"><label>فولتية المصدر (Volt)</label><input type="number" value={v} onChange={(e) => handleChange('voltage', Number(e.target.value))} /></div>
                <div className="input-group"><label>قيمة المقاومة (Ohm Ω)</label><input type="number" value={r} onChange={(e) => handleChange('resistance', Number(e.target.value))} /></div>
                <div className="metrics-card"><div className="metrics-title">📊 التحليل الحسابي الفوري</div><div className="metric-row"><span>التيار المار (I):</span><strong>{i.toFixed(3)} A</strong></div><div className="metric-row"><span>القدرة المستهلكة (P):</span><strong>{p.toFixed(3)} W</strong></div></div>
              </>
            ) : (<p style={{ color: '#94a3b8', textAlign: 'center', marginTop: '40px' }}>اضغط على أي عنصر في المخطط لتعديل قيمه وتفاصيله</p>)}
          </div>
        </div>
      );
    }
    ReactDOM.createRoot(document.getElementById('root')).render(<App />);
  </script>
</body>
</html>
"""

# تحويل كود الـ HTML إلى صيغة Base64 ليعمل مع st.iframe
b64_html = base64.b64encode(react_flow_html.encode('utf-8')).decode('utf-8')
data_url = f"data:text/html;base64,{b64_html}"

# استخدام st.iframe بدلاً من components.html
st.iframe(src=data_url, height=750)
