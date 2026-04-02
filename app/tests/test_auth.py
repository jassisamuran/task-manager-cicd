import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_success():
    response = client.post("/token", data={"username": "johndoe", "password": "fakehashedsecret"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_failure():
    response = client.post("/token", data={"username": "johndoe", "password": "wrongpassword"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect username or password"


def test_read_users_me_success():
    login_response = client.post("/token", data={"username": "johndoe", "password": "fakehashedsecret"})
    token = login_response.json()["access_token"]
    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["username"] == "johndoe"


def test_read_users_me_failure():
    response = client.get("/users/me", headers={"Authorization": "Bearer wrongtoken"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"