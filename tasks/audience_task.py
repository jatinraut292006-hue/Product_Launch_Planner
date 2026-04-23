from crewai import Task

def create_audience_task(agent, product_name, product_description, target_market):
    return Task(
        description=f"""Based on the market research provided, build a detailed 
        audience profile for the following product:
        
        Product Name: {product_name}
        Product Description: {product_description}
        Target Market: {target_market}
        
        Your job is to:
        1. Build a detailed user persona with name, age, occupation, and lifestyle
        2. Identify the top 3-5 pain points this product solves for them
        3. Understand their buying behavior and decision making process
        4. Recommend the top 3 channels to reach this audience
        5. Define what messaging tone works best for this audience
        
        Use the market research output from the previous agent as your foundation.""",
        
        expected_output="""A structured audience profile containing:
        - User Persona: Detailed profile of the ideal customer
        - Pain Points: Top problems this product solves for them
        - Buying Behavior: How and why they make purchase decisions
        - Recommended Channels: Best platforms to reach this audience
        - Messaging Tone: The right voice and tone for this audience""",
        
        agent=agent
    )