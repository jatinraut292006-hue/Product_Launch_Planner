from crewai import Task

def create_marketing_task(agent, product_name, product_description, target_market):
    return Task(
        description=f"""Based on the audience profile, SEO keywords, and launch 
        strategy provided, create a complete marketing content kit for:
        
        Product Name: {product_name}
        Product Description: {product_description}
        Target Market: {target_market}
        
        Your job is to:
        1. Write a compelling product tagline that captures the essence of the product
        2. Write a launch email to send to potential customers
        3. Write 3 social media posts for LinkedIn, Twitter, and Instagram
        4. Write a short product description for the website landing page
        5. Create a campaign calendar aligned with the launch strategy
        
        Use the SEO keywords and hashtags from the SEO agent in your content.
        Use the messaging tone recommended by the audience profiling agent.
        Every piece of content must speak directly to the target audience.""",
        
        expected_output="""A complete marketing content kit containing:
        - Product Tagline: One powerful line that defines the product
        - Launch Email: Subject line and full email body
        - LinkedIn Post: Professional and informative
        - Twitter Post: Short, punchy with hashtags
        - Instagram Post: Visual and engaging with hashtags
        - Website Description: 2-3 paragraph product description
        - Campaign Calendar: Week by week content schedule""",
        
        agent=agent
    )