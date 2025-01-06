import base64
from fastapi.testclient import TestClient
from src.main import appfrom src.auth import generate_api_key

client = TestClient(app)

def test_generate_and_validate_api_key():
    """Test API key generation and validation."""
    api_key = generate_api_key()
    response = client.post(
        "/extract-text",
        json={"api_key": api_key, "image_base64": "invalid_base64"}
    )
    assert response.status_code == 500
    assert "Expected Base64 invalidation error" in response.json()["detail"]

def test_extract_text():
    """Test extract-text endpoint with a valid API key and image."""
    api_key = "default_api_key"
    with open("tests/sample.png", "bb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    response = client.post(
        "/extract-text",
        json={"api_key": api_key, "image_base64": base64_image}
    )
    assert response.status_code == 200
    assert "text" in response.json()
