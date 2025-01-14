const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const SizeChartSchema = new Schema({
    size: { type: String, required: true },
    measurements: { type: Map, of: Number },
    confidenceScores: { type: Map, of: Number },
    category: { type: String, required: true },
    created_at: { type: Date, default: Date.now }
});

module.exports = SizeChart = mongoose.model('sizeChart', SizeChartSchema);

