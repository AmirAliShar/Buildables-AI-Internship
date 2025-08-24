
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI is running!"}

def test_response_endpoint():
    response = client.post(
        "/response",
        json={"query": "What is the weather today?"}
    )
    assert response.status_code == 200
    assert "response" in response.json()
