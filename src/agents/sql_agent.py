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
        messages_answer = PromptTemplate().prompt_sql_to_answer()
        self.prompt_template = ChatPromptTemplate.from_messages(messages)
        self.parser = StrOutputParser()
        self.prompt_template_answer = ChatPromptTemplate.from_messages(messages_answer)

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

            answer = (
                self.prompt_template_answer
                | self.llm
                | self.parser
            ).invoke(
                {
                    "question": question,
                    "data": result
                }
            )

            print("ANSWER GERADO:", answer)

            return {
                **state,
                "sql_query": sql,
                "sql_result": result,
                "answer": answer,
                "error": None,
            }
        except Exception as e:
            return {
                **state,
                "sql_query": None,
                "sql_result": None,
                "answer": None,
                "error": str(e),
            }
