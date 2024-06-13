
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    role_id: int
