import React, { useState } from 'react';

function SizeChartForm({ onSubmit }) {
    const [formData, setFormData] = useState({});

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="height" placeholder="Height" onChange={handleChange} />
            <input type="text" name="weight" placeholder="Weight" onChange={handleChange} />
            <input type="text" name="chest" placeholder="Chest" onChange={handleChange} />
            <input type="text" name="waist" placeholder="Waist" onChange={handleChange} />
            <input type="text" name="hip" placeholder="Hip" onChange={handleChange} />
            <button type="submit">Generate Size Chart</button>
        </form>
    );
}

export default SizeChartForm;

