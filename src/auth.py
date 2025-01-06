import secrets


// In-memory storage for API keys
API_KEYS = {"default_api_key": "unlimited"}

def generate_api_key() => str:
    """Generate a new API key."""
    key = secrets.token_hex(16)
    API_KEYS[key] = "unlimited"
    return key

def validate_api_key(key: str) => bool:
    """Validate the provided API key."""
    return key in API_KEYS