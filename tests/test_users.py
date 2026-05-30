from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def test_create_user():

    response = client.post(
        "/users",
        json={
            "name": "Test User",
            "email": f"{uuid.uuid4()}@test.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200