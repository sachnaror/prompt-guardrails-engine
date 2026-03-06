from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_endpoint():

    payload = {
        "text": "Customer filed a vehicle damage claim worth 2000 dollars"
    }

    response = client.post("/generate", json=payload)

    assert response.status_code == 200
    assert "input_text" in response.json()
