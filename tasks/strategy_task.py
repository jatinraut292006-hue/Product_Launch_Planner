from crewai import Task

def create_strategy_task(agent, product_name, product_description, target_market):
    return Task(
        description=f"""Based on the market research, audience profile, and SEO data 
        provided, create a detailed phased launch strategy and roadmap for:
        
        Product Name: {product_name}
        Product Description: {product_description}
        Target Market: {target_market}
        
        Your job is to:
        1. Define a pre-launch phase with specific actions and timeline
        2. Define a launch phase with specific actions and timeline
        3. Define a post-launch phase with specific actions and timeline
        4. Set clear milestones and success metrics for each phase
        5. Identify potential risks and how to mitigate them
        6. Recommend the launch channels based on the audience profile
        
        Be realistic with timelines. A typical product launch spans 8-12 weeks.
        Use all previous agent outputs to inform your strategy.""",
        
        expected_output="""A structured launch strategy containing:
        - Pre-Launch Phase: Actions, timeline, and milestones (weeks 1-4)
        - Launch Phase: Actions, timeline, and milestones (weeks 5-6)
        - Post-Launch Phase: Actions, timeline, and milestones (weeks 7-12)
        - Success Metrics: How to measure the launch success
        - Risk Mitigation: Potential risks and contingency plans
        - Launch Channels: Where and how to launch based on audience""",
        
        agent=agent
    )