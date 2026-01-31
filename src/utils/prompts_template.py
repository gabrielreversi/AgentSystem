class PromptTemplate:
    def prompt_query_sql(self):
        return [
            (
                "system",
                """
You are a senior data analyst.
Your task is to generate a PostgreSQL SQL query.

Rules:
- Use ONLY the tables and columns provided in the schema.
- Do NOT hallucinate tables or columns.
- Do NOT use SELECT *.
- Generate ONLY valid PostgreSQL SQL.
- Output ONLY the SQL query. No explanation.
- Do NOT wrap the SQL in markdown
- Do NOT use ```sql
- Output raw SQL only
"""
            ),
            (
                "human",
                """
Schema:
{schema}

Question:
{question}

SQL:
"""
            ),
        ]
    
    def prompt_sql_to_answer(self):
        return [
            (
                "system",
                """
You are a senior Business analyst.
Your task is to analyse the Data from databse and provide a clear, concise summary.

Rules:
- You should to analyze ONLY the data provided in the SQL results.
- Do NOT hallucinate create new data or make assumptions beyond what is in the data.
- AWAYS provide the answer in PORTUGUESE-BR.
"""
            ),
            (
                "human",
                """
Data:
{data}

Question:
{question}

Answer:
"""
            ),
        ]