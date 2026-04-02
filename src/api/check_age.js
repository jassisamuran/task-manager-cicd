const formatResponse = require('../utils/responseFormatter');

function checkAge(req, res) {
    const { age } = req.body;
    const eligibilityMessage = age >= 18 ? 'User is eligible' : 'User is not eligible';
    return res.status(200).json(formatResponse(eligibilityMessage));
}

module.exports = checkAge;