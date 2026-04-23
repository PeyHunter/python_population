from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Backend is running"}
    
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    
'''   
This tests your FastAPI app directly.
TestClient(app)
Creates a test version of your backend so you can call endpoints without running the real server manually.
test_root()
Checks:
- the / endpoint exists
- it returns status 200
- it returns the expected JSON


test_health()
Checks:
- the /health endpoint works
- it returns the correct health response
These''' 