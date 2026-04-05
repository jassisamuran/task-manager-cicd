def word_count(text):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    digit_count = 0
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char.isdigit():
            digit_count += 1

    return {
        'vowels': vowel_count,
        'consonants': consonant_count,
        'digits': digit_count
    }