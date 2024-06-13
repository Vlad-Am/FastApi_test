from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.database import get_async_session
from src.app.operations.models import operations
from src.app.operations.schemas import OperationCreate

router = APIRouter(
    prefix='/operations',
    tags=["Operations"]
)


@router.get('/')
async def get_specific_operations(operations_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operations).where(operations.c.type == operations_type)
    result = await session.execute(query)
    return result.all()


@router.post('/')
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    statement = insert(operations).values(**new_operation.dict())
    await session.execute(statement)
    await session.commit()
    return {'status': 'success'}
