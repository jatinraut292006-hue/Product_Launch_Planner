from crewai import Task

def create_visual_task(agent, product_name, product_description, target_market):
    return Task(
        description=f"""Based on the audience profile, tagline, and marketing content 
        created by the previous agents, create a detailed visual advertisement 
        concept for:
        
        Product Name: {product_name}
        Product Description: {product_description}
        Target Market: {target_market}
        
        Your job is to:
        1. Design a concept for an eye-catching marketing visual/ad creative
        2. Describe the visual layout, colors, and design elements in detail
        3. Specify what text appears on the visual and where
        4. Describe the imagery or illustrations to be used
        5. Create versions for three formats — social media post, banner ad, and story format
        
        The visual must:
        - Speak directly to the target audience
        - Include the product tagline
        - Use colors and design that match the brand tone
        - Be bold, modern, and attention grabbing
        - Be described in enough detail that a designer can recreate it exactly""",
        
        expected_output="""A detailed visual advertisement concept containing:
        - Social Media Post Visual: Full description of the design
        - Banner Ad Visual: Full description of the design
        - Story Format Visual: Full description of the design
        - Color Palette: Specific colors to use with reasoning
        - Typography: Font style and hierarchy recommendations
        - Key Design Elements: Icons, imagery, and layout details
        - Design Rationale: Why these choices work for this audience""",
        
        agent=agent
    )