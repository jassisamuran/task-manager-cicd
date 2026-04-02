const express = require('express');
const userAgeMessageController = require('../controllers/userAgeMessageController');

const router = express.Router();

router.post('/user-age-message', userAgeMessageController);

module.exports = router;