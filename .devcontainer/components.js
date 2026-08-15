// تعريف عقدة مصدر الجهد المستقلة (Voltage Source Node)
export const VoltageSourceNode = ({ data, selected }) => {
  const voltage = Number(data.voltage) || 0;

  return (
    <div style={{
      padding: '10px 15px',
      borderRadius: '50%',
      width: '80px',
      height: '80px',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      border: selected ? '3px solid #28a745' : '2px solid #333',
      background: '#fff',
      boxShadow: '0 2px 5px rgba(0,0,0,0.1)'
    }}>
      <strong>{data.label || 'V1'}</strong>
      <span style={{ fontSize: '12px', color: '#28a745' }}>{voltage} V</span>
    </div>
  );
};

// تعريف عقدة المكثف (Capacitor Node)
export const CapacitorNode = ({ data, selected }) => {
  const capacitance = Number(data.capacitance) || 0;

  return (
    <div style={{
      padding: '10px 15px',
      borderRadius: '6px',
      border: selected ? '2px solid #ffc107' : '2px solid #555',
      background: '#fff',
      textAlign: 'center'
    }}>
      <strong>{data.label || 'C1'}</strong>
      <div style={{ fontSize: '12px', color: '#666' }}>{capacitance} µF</div>
    </div>
  );
};
