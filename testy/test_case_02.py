from fastapi.testclient import TestClient
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from unittest.mock import Mock
import pytest


# Mock dla bazy danych
def get_mock_db():
    yield Mock()


# Aplikacja testowa
app = FastAPI()


# Mock CRUD operations
class MockUser:
    def __init__(self, id=1, name="Tomek"):
        self.id = id
        self.name = name


def mock_create_user(db: Session, name: str):
    return MockUser(id=1, name=name)


def mock_get_user(db: Session, user_id: int):
    return MockUser(id=user_id, name="Tomek")


@app.post("/users")
def create_user(name: str, db: Session = Depends(get_mock_db)):
    return mock_create_user(db, name)


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_mock_db)):
    return mock_get_user(db, user_id)


client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Mock - nie potrzebujemy prawdziwej bazy
    yield
    # Czyści po testach - Mock nie wymaga czyszczenia
    pass


def test_create_user():
    response = client.post("/users", params={"name": "Tomek"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Tomek"


def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["name"] == "Tomek"
