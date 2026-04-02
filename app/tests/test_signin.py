import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_signin_success():
    response = client.post("/signin", data={"username": "johndoe", "password": "secret"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_signin_failure():
    response = client.post("/signin", data={"username": "johndoe", "password": "wrongpassword"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect username or password"
