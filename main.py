from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv
import base64
from io import BytesIO
from google import genai
from google.genai import types
from PIL import Image

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Imagen API", description="API for generating images using Google's Gemini Imagen model")

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

# Initialize Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

class ImageGenerationRequest(BaseModel):
    prompt: str
    number_of_images: int = 2  # Default to 2 images

class ImageGenerationResponse(BaseModel):
    images: List[str]  # List of base64 encoded images

@app.post("/generate-images", response_model=ImageGenerationResponse)
async def generate_images(request: ImageGenerationRequest):
    try:
        # Generate images using Gemini API
        response = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt=request.prompt,
            config=types.GenerateImagesConfig(
                number_of_images=request.number_of_images,
                aspect_ratio='4:3'
            ),
        )
        
        # Convert images to base64
        base64_images = []
        for generated_image in response.generated_images:
            # Convert bytes to base64 string
            base64_string = base64.b64encode(generated_image.image.image_bytes).decode('utf-8')
            base64_images.append(base64_string)
        
        return ImageGenerationResponse(images=base64_images)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 