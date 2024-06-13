from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, JSON, Boolean, MetaData

metadata = MetaData()

Role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50), nullable=False),
    Column("permissions", JSON),
)

User = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(50), unique=True),
    Column("hashed_password", String),
    Column("username", String(50), nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(Role.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
