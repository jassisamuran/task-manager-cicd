const checkEligibility = require('./ageEligibility');

describe('checkEligibility', () => {
    test('returns eligible when age is 20', () => {
        expect(checkEligibility(20)).toBe('eligible');
    });

    test('returns not eligible when age is not 20', () => {
        expect(checkEligibility(19)).toBe('not eligible');
        expect(checkEligibility(21)).toBe('not eligible');
    });
});
