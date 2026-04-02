function checkEligibility(age) {
    if (age === 20) {
        return 'eligible';
    } else {
        return 'not eligible';
    }
}

module.exports = checkEligibility;