
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const sizeChartRoutes = require('./routes/sizeChartRoutes');
const dbConfig = require('./config/db');

const app = express();
app.use(bodyParser.json());

// Database connection
mongoose.connect(dbConfig.mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.log(err));

// Routes
app.use('/api/size-chart', sizeChartRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
