const express = require('express');
const router = express.Router();
const { generateSizeChart, getSizeChart } = require('../controllers/sizeChartController');

router.post('/generate', generateSizeChart);
router.get('/:id', getSizeChart);

module.exports = router;

