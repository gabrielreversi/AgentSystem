from src.infra.database.connection import engine
from src.infra.database.executor import SQLExecutor

executor = SQLExecutor(engine)

res = executor.execute("""
    SELECT
    sku_name,
    SUM(qty) AS total_qty
    FROM sales
    GROUP BY sku_name
"""
)

print(res)