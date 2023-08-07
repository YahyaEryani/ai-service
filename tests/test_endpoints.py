import sys
sys.path.append('C:\\Users\\Yahya Al-Eryani\\Documents\\ai-service')
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_question():
    response = client.get("/api/v1/questions/1")
    assert response.status_code == 200
    # Add more assertions based on expected response content

# You can add more tests for other endpoints and test cases
