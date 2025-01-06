import base64
from PIL import Image
import tesserocr
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import asyncio


// Create a thread pool
thread_pool = ThreadPoolExecutor()

// Process image data and extract text
def process_image(image_data: bytes) -> str:
    """Process image data and extract text."""
    image = Image.open(BytesIO(image_data))
    return tesserocr.image_to_text(image)

async def extract_text_from_base64(image_base64: str) -> str:
    """Extract text from a Base64-encoded image."""
    try:
        # Decode the Base64 string
        image_data = base64.b64decode(image_base64)
        # Run the processing in a thread
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(thread_pool, process_image, image_data)
    except Exception as e:
        raise ValueError(f"Invalid Base64 image: ${e}")