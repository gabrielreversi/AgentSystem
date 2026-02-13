from langgraph.graph import StateGraph
from langchain_openai import AzureChatOpenAI

from src.agents.state import AgentSQLstate
from src.agents.sql_agent import SQLAgentNode
from src.infra.memory.checkpointer import CheckpointerFactory
from dotenv import load_dotenv
import os

load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0.2,
    max_tokens=500,
    seed=123
)

sql_node = SQLAgentNode(llm)

graph = StateGraph(AgentSQLstate)
graph.add_node("sql_agent", sql_node)
graph.set_entry_point("sql_agent")

# memory checkpointer setup
factory = CheckpointerFactory()
checkpointer = factory.create()

app = graph.compile(checkpointer=checkpointer)