from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional


# Классы валидации данных с помощью Pydantic
class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0.01)
    amount: float


class DegreeType(Enum):
    expert = 'expert'
    professor = 'professor'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    name: str
    degree: Optional[List[Degree]] = []
