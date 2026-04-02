const express = require('express');
const ageRoutes = require('../routes/ageRoutes');

const app = express();
app.use(express.json());
app.use('/api', ageRoutes);

module.exports = app;