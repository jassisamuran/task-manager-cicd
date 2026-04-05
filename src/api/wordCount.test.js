const request = require('supertest');
const app = require('./wordCount');

describe('POST /api/wordcount', () => {
    it('should return counts of vowels, consonants, and digits', async () => {
        const response = await request(app)
            .post('/api/wordcount')
            .send({ input: 'Hello World 123!' });

        expect(response.status).toBe(200);
        expect(response.body).toEqual({
            vowelCount: 3,
            consonantCount: 7,
            digitCount: 3
        });
    });

    it('should return 400 for invalid input', async () => {
        const response = await request(app)
            .post('/api/wordcount')
            .send({ input: 12345 });

        expect(response.status).toBe(400);
        expect(response.body).toEqual({ error: 'Invalid input, expected a string.' });
    });
});
