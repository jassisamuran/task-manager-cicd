const validateAge = (req, res, next) => {
    const { age } = req.body;
    if (age === undefined) {
        return res.status(400).json({ message: 'Age is required' });
    }
    if (typeof age !== 'number' || age < 0) {
        return res.status(400).json({ message: 'Age must be a positive integer' });
    }
    next();
};

module.exports = validateAge;
