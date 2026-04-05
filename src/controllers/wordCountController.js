const { countCharacters } = require('../utils/countUtils');

const wordCountController = (req, res) => {
    const { input } = req.body;

    if (typeof input !== 'string') {
        return res.status(400).json({ error: 'Invalid input, expected a string.' });
    }

    const counts = countCharacters(input);
    return res.status(200).json(counts);
};

module.exports = wordCountController;