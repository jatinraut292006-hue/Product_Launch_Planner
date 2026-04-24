import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def evaluate_output(product_name, target_market, crew_output):

    model = genai.GenerativeModel("gemini-2.0-flash")

    evaluation_prompt = f"""You are an expert evaluator assessing the quality of an 
    AI-generated product launch plan. 
    
    Product Name: {product_name}
    Target Market: {target_market}
    
    Generated Launch Plan:
    {crew_output}
    
    Evaluate this launch plan against the following rubric. 
    Score each criterion from 1 to 10 and provide brief reasoning.
    
    EVALUATION RUBRIC:
    
    1. Market Research Quality
       - Are competitors clearly identified?
       - Are market trends relevant and specific?
       - Are market gaps clearly defined?
    
    2. Audience Profile Quality
       - Is the persona detailed and realistic?
       - Are pain points specific to the product?
       - Are recommended channels appropriate?
    
    3. SEO & Keywords Quality
       - Are keywords specific and relevant?
       - Are hashtags appropriate for the audience?
       - Are trending topics relevant?
    
    4. Strategy & Roadmap Quality
       - Is the roadmap realistic and actionable?
       - Are milestones clearly defined?
       - Are timelines reasonable?
    
    5. Marketing Content Quality
       - Is the tagline compelling and memorable?
       - Is the email copy engaging and clear?
       - Are social media posts platform appropriate?
    
    6. Visual Concept Quality
       - Is the visual concept detailed enough to execute?
       - Does it align with the target audience?
       - Is it creative and attention grabbing?
    
    7. Overall Coherence
       - Does everything work together as one unified plan?
       - Is there consistency across all sections?
       - Would this plan actually work in the real world?
    
    Return your evaluation in this exact format:
    
    SCORES:
    1. Market Research Quality: X/10 — reasoning
    2. Audience Profile Quality: X/10 — reasoning
    3. SEO & Keywords Quality: X/10 — reasoning
    4. Strategy & Roadmap Quality: X/10 — reasoning
    5. Marketing Content Quality: X/10 — reasoning
    6. Visual Concept Quality: X/10 — reasoning
    7. Overall Coherence: X/10 — reasoning
    
    TOTAL SCORE: X/70
    
    OVERALL ASSESSMENT:
    Write 2-3 sentences summarizing the overall quality of this launch plan.
    
    SUGGESTIONS FOR IMPROVEMENT:
    List 3 specific things that could make this plan better."""

    response = model.generate_content(evaluation_prompt)
    return response.text