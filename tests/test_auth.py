import pytest
from fastapi.testclient import TestClient
from main import app
from auth import create_access_token

client = TestClient(app)

@pytest.fixture
def token():
    return create_access_token(data={"sub": "testuser"})

def test_access_token(token):
    response = client.post("/token", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_protected_route(token):
    response = client.get("/protected-route", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"message": "You are authorized!"}

def test_protected_route_no_token():
    response = client.get("/protected-route")
    assert response.status_code == 401
    assert response.json() == {"detail": "Could not validate credentials"}
