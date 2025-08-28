from dotenv import load_dotenv
load_dotenv()

from crewai.agents import Agent
from tools import FinancialDocumentTool

# Replace this with your actual LLM initialization
llm = "your_llm_instance"

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide data-driven financial analysis and investment advice for query: {query}",
    verbose=True,
    memory=True,
    backstory="Analyze financial reports carefully and deliver accurate advice.",
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True,
)
