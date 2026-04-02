const request = require('supertest');
const express = require('express');
const bodyParser = require('body-parser');
const ageRoutes = require('../routes/ageRoutes');

const app = express();
app.use(bodyParser.json());
app.use('/check_age', ageRoutes);

describe('POST /check_age', () => {
    it('should return 200 and eligible message for age 20', async () => {
        const response = await request(app)
            .post('/check_age')
            .send({ age: 20 });
        expect(response.status).toBe(200);
        expect(response.body.message).toBe('User is eligible');
    });

    it('should return 200 and not eligible message for age 16', async () => {
        const response = await request(app)
            .post('/check_age')
            .send({ age: 16 });
        expect(response.status).toBe(200);
        expect(response.body.message).toBe('User is not eligible');
    });

    it('should return 400 for missing age', async () => {
        const response = await request(app)
            .post('/check_age')
            .send({});
        expect(response.status).toBe(400);
        expect(response.body.message).toBe('Age is required');
    });

    it('should return 400 for invalid age', async () => {
        const response = await request(app)
            .post('/check_age')
            .send({ age: -5 });
        expect(response.status).toBe(400);
        expect(response.body.message).toBe('Age must be a positive integer');
    });
});
