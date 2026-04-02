const request = require('supertest');
const express = require('express');
const checkAge = require('./check_age');

const app = express();
app.use(express.json());
app.post('/check_age', checkAge);

describe('POST /check_age', () => {
    it('should return eligible message for age 20', async () => {
        const response = await request(app).post('/check_age').send({ age: 20 });
        expect(response.status).toBe(200);
        expect(response.body.message).toBe('User is eligible');
    });

    it('should return not eligible message for age 16', async () => {
        const response = await request(app).post('/check_age').send({ age: 16 });
        expect(response.status).toBe(200);
        expect(response.body.message).toBe('User is not eligible');
    });

    it('should return 400 for missing age', async () => {
        const response = await request(app).post('/check_age').send({});
        expect(response.status).toBe(400);
        expect(response.body.message).toBe('Invalid age input');
    });

    it('should return 400 for non-integer age', async () => {
        const response = await request(app).post('/check_age').send({ age: 'twenty' });
        expect(response.status).toBe(400);
        expect(response.body.message).toBe('Invalid age input');
    });
});
