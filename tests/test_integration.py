from fastapi.testclient import TestClient
from app.main import app
from app.models import Base
from app.database import engine
from sqlalchemy.orm import sessionmaker
import pytest

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_read_user():
    response = client.post(
        "/users/",
        json={"username": "testuser", "email": "test@example.com"}
    )
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "test@example.com"