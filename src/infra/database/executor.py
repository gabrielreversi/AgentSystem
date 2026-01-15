from sqlalchemy import text

class SQLExecutor:
    def __init__(self, engine):
        self.engine = engine

    def execute(self, sql:str):
        sql_clean = sql.strip().lower()

        if not sql_clean.startswith("select"):
            raise ValueError("Only SELECT statements are allowed")
        
        with self.engine.connect() as conn:
            result = conn.execute(text(sql))

            return {
                "columns": list(result.keys()),
                "rows": [list(row) for row in result.fetchall()]
            }