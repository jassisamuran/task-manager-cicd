const formatResponse = require('../utils/responseFormatter');

const userAgeMessageController = (req, res) => {
    const age = req.body.age;
    let message;

    if (age < 18) {
        message = 'User is not eligible.';
    } else {
        message = 'User is eligible.';
    }

    res.json(formatResponse(message));
};

module.exports = userAgeMessageController;