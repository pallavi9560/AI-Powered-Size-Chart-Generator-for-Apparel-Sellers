
const SizeChart = require('../models/SizeChart');
const { spawn } = require('child_process');

// Generate Size Chart
const generateSizeChart = (req, res) => {
    const userData = req.body;
    const pythonProcess = spawn('python3', ['./ml/sizeChartModel.py', JSON.stringify(userData)]);

    pythonProcess.stdout.on('data', (data) => {
        const sizeChart = JSON.parse(data.toString());
        const newSizeChart = new SizeChart(sizeChart);
        newSizeChart.save().then(chart => res.json(chart));
    });
};

// Get Size Chart by ID
const getSizeChart = (req, res) => {
    SizeChart.findById(req.params.id)
        .then(chart => res.json(chart))
        .catch(err => res.status(404).json({ nosizechartfound: 'No size chart found with that ID' }));
};

module.exports = { generateSizeChart, getSizeChart };
