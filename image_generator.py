import os
import base64
from dotenv import load_dotenv
from google import genai

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
    
    response = client.models.generate_images(
        model="imagen-4.0-fast-generate-001",
        prompt=prompt,
        config=genai.types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="1:1",
        )
    )
    
    for image in response.generated_images:
        return image.image.image_bytes
    
    return None