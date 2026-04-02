const express = require('express');
const { checkAge } = require('../controllers/ageController');
const validateAge = require('../middleware/validateAge');

const router = express.Router();

router.post('/', validateAge, checkAge);

module.exports = router;
