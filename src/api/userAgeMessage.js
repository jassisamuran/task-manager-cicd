const express = require('express');
const userAgeMessageRoutes = require('../routes/userAgeMessageRoutes');

const app = express();

app.use(express.json());
app.use('/api', userAgeMessageRoutes);

module.exports = app;