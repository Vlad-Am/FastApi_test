from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, JSON

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50), nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(50), unique=True),
    Column("password", String),
    Column("username", String(50), nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)
