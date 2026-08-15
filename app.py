import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="React Flow Circuit Calculator", layout="wide")

st.title("⚡ حاسبة الدوائر الكهربائية - React Flow")

react_flow_html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script src="https://unpkg.com/reactflow@11.10.1/dist/umd/index.js"></script>
  <link rel="stylesheet" href="https://unpkg.com/reactflow@11.10.1/dist/style.css" />
  <style>
    body, html, #root { width: 100%; height: 100%; margin: 0; padding: 0; font-family: sans-serif; }
    .app-container { display: flex; width: 100vw; height: 100vh; }
    .flow-container { flex-grow: 1; height: 100%; }
    .panel { width: 280px; padding: 15px; background: #f8f9fa; border-right: 1px solid #ddd; box-sizing: border-box; }
    .field { margin-bottom: 12px; display: flex; flex-direction: column; gap: 4px; }
    .field input { padding: 6px; border: 1px solid #ccc; border-radius: 4px; }
    .results { margin-top: 15px; padding: 10px; background: #eef6ff; border-radius: 6px; }
    .node-box { padding: 10px 15px; border-radius: 6px; background: #fff; text-align: center; border: 2px solid #333; }
  </style>
</head>
<body>
  <div id="root"></div>

  <script type="text/babel">
    const { useState, useCallback, useMemo } = React;
    const { ReactFlow, Handle, Position, useNodesState, useEdgesState } = ReactFlowRenderer;

    const ResistorNode = ({ data, selected }) => {
      const v = Number(data.voltage) || 0;
      const r = Number(data.resistance) || 1;
      const i = r > 0 ? v / r : 0;
      const p = v * i;

      return (
        <div className="node-box" style={{ borderColor: selected ? '#007bff' : '#555' }}>
          <Handle type="target" position={Position.Left} />
          <div><strong>{data.label || 'مقاومة'}</strong></div>
          <small>V: {v} V | R: {r} Ω</small>
          <div style={{ color: '#0066cc', fontSize: '12px', marginTop: '4px' }}>
            I: {i.toFixed(2)} A | P: {p.toFixed(2)} W
          </div>
          <Handle type="source" position={Position.Right} />
        </div>
      );
    };

    const initialNodes = [
      { id: '1', type: 'resistor', position: { x: 100, y: 150 }, data: { label: 'R1', voltage: 12, resistance: 10 } },
      { id: '2', type: 'resistor', position: { x: 350, y: 150 }, data: { label: 'R2', voltage: 24, resistance: 20 } }
    ];

    function App() {
      const nodeTypes = useMemo(() => ({ resistor: ResistorNode }), []);
      const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
      const [edges, setEdges, onEdgesChange] = useEdgesState([]);
      const [selectedNode, setSelectedNode] = useState(initialNodes[0]);

      const onSelectionChange = useCallback(({ nodes }) => {
        setSelectedNode(nodes.length > 0 ? nodes[0] : null);
      }, []);

      const handleChange = (key, val) => {
        if (!selectedNode) return;
        const newNodes = nodes.map((node) => {
          if (node.id === selectedNode.id) {
            const updatedData = { ...node.data, [key]: val };
            setSelectedNode({ ...node, data: updatedData });
            return { ...node, data: updatedData };
          }
          return node;
        });
        setNodes(newNodes);
      };

      const v = selectedNode ? Number(selectedNode.data.voltage) || 0 : 0;
      const r = selectedNode ? Number(selectedNode.data.resistance) || 0 : 0;
      const i = r > 0 ? v / r : 0;
      const p = v * i;

      return (
        <div className="app-container">
          <div className="panel">
            <h3>تعديل الخصائص</h3>
            {selectedNode ? (
              <>
                <div className="field">
                  <label>الاسم:</label>
                  <input type="text" value={selectedNode.data.label} onChange={(e) => handleChange('label', e.target.value)} />
                </div>
                <div className="field">
                  <label>الجهد (Volt):</label>
                  <input type="number" value={v} onChange={(e) => handleChange('voltage', Number(e.target.value))} />
                </div>
                <div className="field">
                  <label>المقاومة (Ohm):</label>
                  <input type="number" value={r} onChange={(e) => handleChange('resistance', Number(e.target.value))} />
                </div>
                <div className="results">
                  <strong>النتائج المحسوبة:</strong>
                  <div>التيار (I): <b>{i.toFixed(2)} A</b></div>
                  <div>القدرة (P): <b>{p.toFixed(2)} W</b></div>
                </div>
              </>
            ) : <p>حدد عنصر لتعديل قيمته</p>}
          </div>
          <div className="flow-container">
            <ReactFlow
              nodes={nodes}
              edges={edges}
              onNodesChange={onNodesChange}
              onEdgesChange={onEdgesChange}
              onSelectionChange={onSelectionChange}
              nodeTypes={nodeTypes}
              fitView
            />
          </div>
        </div>
      );
    }

    ReactDOM.createRoot(document.getElementById('root')).render(<App />);
  </script>
</body>
</html>
"""

components.html(react_flow_html, height=700, scrolling=True)
