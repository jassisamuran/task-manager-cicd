const express = require('express');
const wordCountRoutes = require('../routes/wordCountRoutes');

const app = express();
app.use(express.json());
app.use('/api', wordCountRoutes);

module.exports = app;