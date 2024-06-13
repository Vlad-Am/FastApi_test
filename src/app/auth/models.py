from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, JSON, Boolean, MetaData

from src.app.database import Base

metadata = MetaData()

Role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50), nullable=False),
    Column("permissions", JSON),
)

user = Table(
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


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    email = Column("email", String(50), unique=True)
    username = Column("username", String(50), nullable=False)
    created_at = Column("created_at", TIMESTAMP, default=datetime.utcnow)
    role_id = Column("role_id", Integer, ForeignKey(Role.c.id))
    is_active = Column("is_active", Boolean, default=True, nullable=False)
    is_superuser = Column("is_superuser", Boolean, default=False, nullable=False)
    is_verified = Column('is_verified', Boolean, default=False, nullable=False)
