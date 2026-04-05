function countCharacters(input) {
    const vowels = input.match(/[aeiou]/gi) || [];
    const consonants = input.match(/[bcdfghjklmnpqrstvwxyz]/gi) || [];
    const digits = input.match(/[0-9]/g) || [];

    return {
        vowelCount: vowels.length,
        consonantCount: consonants.length,
        digitCount: digits.length
    };
}

module.exports = { countCharacters };