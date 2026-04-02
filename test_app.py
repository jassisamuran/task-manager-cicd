import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_login(client):
    response = client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
    print('Login Response:', response.data)  # Debugging line
    assert response.status_code == 200
    json_data = json.loads(response.data)
    assert 'token' in json_data
    assert 'refresh_token' in json_data


def test_refresh(client):
    login_response = client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
    refresh_token = json.loads(login_response.data)['refresh_token']
    response = client.post('/refresh', json={'refresh_token': refresh_token})
    print('Refresh Response:', response.data)  # Debugging line
    assert response.status_code == 200
    json_data = json.loads(response.data)
    assert 'token' in json_data


def test_refresh_invalid_token(client):
    response = client.post('/refresh', json={'refresh_token': 'invalid_token'})
    print('Invalid Token Response:', response.data)  # Debugging line
    assert response.status_code == 401
    json_data = json.loads(response.data)
    assert 'message' in json_data
    assert json_data['message'] == 'Token is invalid'