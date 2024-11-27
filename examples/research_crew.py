from crewai import Agent, Task, Crew
from textwrap import dedent
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Ensure we have an API key
if not os.getenv("PERPLEXITY_API_KEY"):
    raise ValueError("Please set PERPLEXITY_API_KEY in your .env file")

# Configure the LLM to use Perplexity's API
llm = ChatOpenAI(
    model_name="perplexity/llama-3.1-sonar-large-128k-online",
    openai_api_key=os.getenv("PERPLEXITY_API_KEY"),
    openai_api_base="https://api.perplexity.ai",
    temperature=0.7
)

# Define our agents with their roles and goals
researcher = Agent(
    role='Research Specialist',
    goal='Conduct thorough research on given topics and provide detailed information',
    backstory=dedent("""
        You are an experienced research specialist with a keen eye for detail.
        You excel at gathering comprehensive information from various sources
        and presenting it in a clear, organized manner.
    """),
    verbose=True,
    allow_delegation=False,
    llm=llm
)

analyst = Agent(
    role='Data Analyst',
    goal='Analyze research findings and extract key insights',
    backstory=dedent("""
        You are a skilled data analyst with expertise in identifying patterns
        and drawing meaningful conclusions from research data. You excel at
        breaking down complex information into actionable insights.
    """),
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define the tasks for our agents
research_task = Task(
    description=dedent("""
        Research the latest developments in artificial intelligence and its impact
        on healthcare in the last 2 years. Focus on:
        1. Major breakthroughs
        2. Practical applications
        3. Challenges and limitations
        
        Provide specific examples and cite your sources.
    """),
    agent=researcher,
    expected_output="A comprehensive research report on AI in healthcare with specific examples and citations"
)

analysis_task = Task(
    description=dedent("""
        Analyze the research findings and create a summary that includes:
        1. Key trends and patterns
        2. Potential future implications
        3. Recommendations for healthcare providers
        
        Focus on practical insights and actionable recommendations.
    """),
    agent=analyst,
    expected_output="An analytical summary with key insights and actionable recommendations"
)

# Create a crew with our agents and tasks
crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    verbose=True
)

# Execute the crew's tasks
results = crew.kickoff()

print("\n=== Final Results ===")
print(results)
