from sqlalchemy import inspect

class SchemaProvider:
    def __init__(self, engine):
        self.engine = engine

    def get_schema(self,) -> str:
        inspector = inspect(self.engine)

        schema_txt = []

        for table_name in inspector.get_table_names():
            columns = inspector.get_columns(table_name)

            cols = ", ".join(
                f"{col['name']} ({col['type']})"
                for col in columns
            )

            schema_txt.append(f"table {table_name}: {cols}")
        return "\n".join(schema_txt)