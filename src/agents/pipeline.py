from langgraph.graph import StateGraph
from langchain_openai import AzureChatOpenAI

from src.agents.state import AgentSQLstate
from src.agents.sql_agent import SQLAgentNode

llm = AzureChatOpenAI(
    azure_endpoint="<>",
    api_key="<>",
    azure_deployment="<>",
    api_version="<>",
    temperature=0.2,
    max_tokens=500,
    seed=123
)

sql_node = SQLAgentNode(llm)

graph = StateGraph(AgentSQLstate)
graph.add_node("sql_agent", sql_node)
graph.set_entry_point("sql_agent")

app = graph.compile()