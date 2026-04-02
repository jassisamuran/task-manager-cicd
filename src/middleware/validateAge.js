function validateAge(req, res, next) {
    const { age } = req.body;
    if (age === undefined || typeof age !== 'number') {
        return res.status(400).json({ message: 'Invalid age input' });
    }
    next();
}

module.exports = validateAge;