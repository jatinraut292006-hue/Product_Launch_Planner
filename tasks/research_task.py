from crewai import Task

def create_research_task(agent, product_name, product_description, target_market):
    return Task(
        description=f"""Research the market landscape for the following product:
        
        Product Name: {product_name}
        Product Description: {product_description}
        Target Market: {target_market}
        
        Your job is to:
        1. Identify the top 3-5 competitors in this space
        2. Find current market trends relevant to this product
        3. Identify gaps in the market that this product can fill
        4. Assess the overall market opportunity
        
        Use Tavily Search to find real, current information.
        Be specific and data-driven in your findings.""",
        
        expected_output="""A structured market research report containing:
        - Competitor Analysis: List of top competitors with their strengths and weaknesses
        - Market Trends: Current trends shaping this market
        - Market Gaps: Opportunities the product can exploit
        - Market Opportunity: Overall assessment of the market""",
        
        agent=agent
    )