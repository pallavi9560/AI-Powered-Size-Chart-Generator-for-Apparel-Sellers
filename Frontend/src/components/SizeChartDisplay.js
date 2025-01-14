import React from 'react';

function SizeChartDisplay({ sizeChart }) {
    return (
        <div>
            <h3>Generated Size Chart</h3>
            <ul>
                {Object.keys(sizeChart).map(size => (
                    <li key={size}>
                        <strong>{size}</strong>: {JSON.stringify(sizeChart[size])}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default SizeChartDisplay;

