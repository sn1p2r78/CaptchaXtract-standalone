from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.auth import validate_api_key
from src.utils import extract_text_from_base64

app = FastAPI()

class OCRRequest(BaseModel):
    api_key: str
    image_base64: str

@app.post("/extract-text")
async def extract_text(request: OCRRequest):
    """Endpoint to extract text from a Base64 image."""
    # Validate API key
    if not validate_api_key(request.api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")

    # Decode and process Base64 image
    try:
        text = await extract_text_from_base64(request.image_base64)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))