import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    # ensure fresh store for each test
    app.config["WORKOUTS"] = []
    with app.test_client() as client:
        yield client

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"

def test_add_and_list_workout(client):
    r = client.post("/workouts", json={"workout": "Jogging", "duration": 25})
    assert r.status_code == 201
    data = r.get_json()
    assert data["workout"] == "Jogging"
    assert data["duration"] == 25

    r = client.get("/workouts")
    assert r.status_code == 200
    arr = r.get_json()
    assert isinstance(arr, list)
    assert any(w["workout"] == "Jogging" for w in arr)

def test_invalid_duration(client):
    r = client.post("/workouts", json={"workout": "Run", "duration": "abc"})
    assert r.status_code == 400

def test_get_not_found(client):
    r = client.get("/workouts/999")
    assert r.status_code == 404
