import os
import base64
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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
    
    model = genai.GenerativeModel("gemini-2.0-flash-preview-image-generation")
    
    response = model.generate_content(
        contents=prompt,
        generation_config={"response_modalities": ["image", "text"]}
    )
    
    for part in response.candidates[0].content.parts:
        if hasattr(part, "inline_data") and part.inline_data:
            image_data = base64.b64decode(part.inline_data.data)
            return image_data
    
    return None