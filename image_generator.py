import os
import base64
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_marketing_image(visual_description, product_name):
    
    prompt = f"""Create a professional, eye-catching marketing advertisement image for a product called {product_name}.
    
    Use this visual concept as your guide:
    {visual_description[:1000]}
    
    The image should be:
    - Modern and professional
    - Suitable for social media marketing
    - Bold and attention grabbing
    - Clean and minimalist design
    - Include the product name prominently
    """
    
    model = genai.GenerativeModel("gemini-2.0-flash-preview-05-20")
    
    response = model.generate_content(
        contents=prompt,
        generation_config={"response_modalities": ["image", "text"]}
    )
    
    for part in response.candidates[0].content.parts:
        if hasattr(part, "inline_data") and part.inline_data:
            image_data = base64.b64decode(part.inline_data.data)
            return image_data
    
    return None