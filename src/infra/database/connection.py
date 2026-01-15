import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL_DATABASE = "postgresql+psycopg2://agent:agent123@localhost:5432/agents_db"

engine = create_engine(
    URL_DATABASE,
    pool_pre_ping=True
)

Sessionlocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)