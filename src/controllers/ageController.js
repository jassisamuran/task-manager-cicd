const checkAge = (req, res) => {
    const { age } = req.body;
    if (age >= 18) {
        return res.status(200).json({ message: 'User is eligible' });
    } else {
        return res.status(200).json({ message: 'User is not eligible' });
    }
};

module.exports = { checkAge };
