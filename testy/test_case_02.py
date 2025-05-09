from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import pytest

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Tworzy tabele przed testami
    Base.metadata.create_all(bind=engine)
    yield
    # Czyści po testach
    Base.metadata.drop_all(bind=engine)

def test_create_and_read_user():
    response = client.post("/users", params={"name": "Tomek"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Tomek"

    response = client.get("/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["name"] == "Tomek"
