const express = require('express');
const wordCountController = require('../controllers/wordCountController');

const router = express.Router();

router.post('/wordcount', wordCountController);

module.exports = router;