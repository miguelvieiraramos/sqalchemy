from sqlalchemy import MetaData, Table, Column, Integer, String, select, Numeric
from sqlalchemy.sql.functions import user
from engine_usage import engine

metadata = MetaData()
user_table = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False),
    Column("classe", String(50)),
)

#create tables
with engine.begin() as conn:
    metadata.create_all(conn)

# stmt = user_table.insert().values(
#     classe="Mage", username="miguel.ramos"
# )

# with engine.begin() as conn:
#     conn.execute(stmt)