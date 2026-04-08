const request = require('supertest');
const app = require('../api/userAgeMessage');

describe('POST /user-age-message', () => {
    it('should return not eligible message for age < 18', async () => {
        const response = await request(app)
            .post('/api/user-age-message')
            .send({ age: 17 });
        expect(response.body.message).toBe('User is not eligible.');
    });

    it('should return eligible message for age >= 18', async () => {
        const response = await request(app)
            .post('/api/user-age-message')
            .send({ age: 18 });
        expect(response.body.message).toBe('User is eligible.');
    });

    it('should return eligible message for age > 18', async () => {
        const response = await request(app)
            .post('/api/user-age-message')
            .send({ age: 19 });
        expect(response.body.message).toBe('User is eligible.');
    });
});
