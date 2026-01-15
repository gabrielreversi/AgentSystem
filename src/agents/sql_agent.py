from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.agents.state import AgentSQLstate

from src.infra.database.schema import SchemaProvider
from src.infra.database.executor import SQLExecutor
from src.infra.database.connection import engine
from src.utils.prompts_template import PromptTemplate


class SQLAgentNode:
    def __init__(self, llm):
        self.llm = llm

        self.schema_provider = SchemaProvider(engine)
        self.sql_executor = SQLExecutor(engine)
        messages = PromptTemplate().prompt_query_sql()
        self.prompt_template = ChatPromptTemplate.from_messages(messages)
        self.parser = StrOutputParser()

    def __call__(self, state:AgentSQLstate) -> AgentSQLstate:
        try:
            question = state['question']
            schema = self.schema_provider.get_schema()

            sql=(
                self.prompt_template
                | self.llm
                | self.parser
            ).invoke(
                {
                    "schema": schema,
                    "question": question
                }
            )

            print("SQL GERADO:", sql)

            sql = sql.strip().rstrip(";")
            result = self.sql_executor.execute(sql)

            return {
                **state,
                "sql_query": sql,
                "sql_result": result,
                "error": None,
            }
        except Exception as e:
            return {
                **state,
                "sql_query": None,
                "sql_result": None,
                "error": str(e),
            }
