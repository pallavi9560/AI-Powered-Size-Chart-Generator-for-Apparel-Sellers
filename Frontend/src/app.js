import React, { useState } from 'react';
import SizeChartForm from './components/SizeChartForm';
import SizeChartDisplay from './components/SizeChartDisplay';

function App() {
    const [sizeChart, setSizeChart] = useState(null);

    const handleFormSubmit = async (formData) => {
        const response = await fetch('/api/size-chart/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });
        const data = await response.json();
        setSizeChart(data);
    };

    return (
        <div className="App">
            <h1>AI-Powered Size Chart Generator</h1>
            <SizeChartForm onSubmit={handleFormSubmit} />
            {sizeChart && <SizeChartDisplay sizeChart={sizeChart} />}
        </div>
    );
}

export default App;

