from typing import TypedDict, Optional

class AgentSQLstate(TypedDict):
    question: str
    sql_query: Optional[str]
    sql_result: Optional[str]
    answer: Optional[str]
    error: Optional[str]