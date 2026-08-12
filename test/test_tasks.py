from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/api/v1/tasks",
        json={
            "title": "Learn Fast API",
            "decription": "Learn Fast API for building production",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Learn Fast API"
    assert data["decription"] == "Learn Fast API for building production"
    assert data["status"] == "pending"


def test_get_tasks():
    response = client.get("/api/v1/tasks")
    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_get_task_not_found():
    response = client.get("/api/v1/tasks/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}
