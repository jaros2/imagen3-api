# Imagen Python API

A FastAPI-based API wrapper for Google's Gemini Imagen model that generates images from text prompts.

## Setup

1. Clone this repository
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Running the API

Start the API server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### POST /generate-images

Generates images based on a text prompt.

Request body:
```json
{
    "prompt": "Your text prompt here",
    "number_of_images": 2  // Optional, defaults to 2
}
```

Response:
```json
{
    "images": [
        "base64_encoded_image_1",
        "base64_encoded_image_2"
    ]
}
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 