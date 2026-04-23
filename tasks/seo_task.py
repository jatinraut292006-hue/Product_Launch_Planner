from crewai import Task

def create_seo_task(agent, product_name, product_description, target_market):
    return Task(
        description=f"""Research and identify the best SEO keywords, trending search 
        terms, and hashtags for the following product:
        
        Product Name: {product_name}
        Product Description: {product_description}
        Target Market: {target_market}
        
        Your job is to:
        1. Find the top 10 high-value SEO keywords relevant to this product
        2. Identify trending search terms people use to find similar products
        3. Find the top 10 hashtags relevant to this product and audience
        4. Identify the best time to post on social media for this audience
        5. Find any trending topics or conversations this product can tap into
        
        Use Tavily Search to find real, current, and trending information.
        Be specific — generic keywords are not useful.""",
        
        expected_output="""A structured SEO and keywords report containing:
        - Top SEO Keywords: 10 high value keywords with brief reasoning
        - Trending Search Terms: What people are actively searching for
        - Top Hashtags: 10 relevant hashtags for social media
        - Best Posting Times: When to post for maximum reach
        - Trending Topics: Conversations this product can join""",
        
        agent=agent
    )