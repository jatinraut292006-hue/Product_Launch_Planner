from crewai import Agent

def create_audience_profiling_agent():
    return Agent(
        role="Audience Profiling Specialist",
        goal="Define the target audience for the product, build user personas, identify pain points and recommend best channels to reach them",
        backstory="""You are an expert in consumer behavior and audience analysis. 
        You have deep experience in building detailed user personas and understanding 
        what drives people to buy products. You use market research data to craft 
        precise audience profiles that marketing teams can act on directly.""",
        tools=[],
        llm="gemini/gemini-2.5-flash-preview-04-17",
        verbose=True,
        allow_delegation=False
    )