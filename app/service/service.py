from sqlalchemy import select
from app import async_session_maker


class BaseCRUD:
    model = None

    @classmethod
    async def find_all(cls, **filters):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            res = await session.execute(query)
            return res.scalars().all()

    @classmethod
    async def find_one_or_none(cls, **filters):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            res = await session.execute(query)
            return res.scalar_one_or_none()
