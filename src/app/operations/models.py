from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData


metadata = MetaData()

operations = Table(
    "operations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("quantity", String, nullable=False),
    Column("description", String, nullable=True),
    Column('figi', String),
    Column('instrument_type', String, nullable=True),
    Column("date", TIMESTAMP),
    Column("type", String),
)
