import os
import base64
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_marketing_image(visual_description, product_name):
    
    prompt = f"""Create a professional, eye-catching marketing advertisement image for a product called {product_name}.
    
    The image should be:
    - Modern and professional
    - Suitable for social media marketing
    - Bold and attention grabbing
    - Clean and minimalist design
    - Dark background with vibrant accent colors
    - Include the product name prominently
    - Tech startup aesthetic
    
    Visual concept: {visual_description[:500]}
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["image", "text"]
        )
    )
    
    for part in response.candidates[0].content.parts:
        if hasattr(part, "inline_data") and part.inline_data:
            return base64.b64decode(part.inline_data.data)
    
    return None