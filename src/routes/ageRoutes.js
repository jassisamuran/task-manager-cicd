const express = require('express');
const validateAge = require('../middleware/validateAge');
const checkAge = require('../api/check_age');

const router = express.Router();

router.post('/check_age', validateAge, checkAge);

module.exports = router;