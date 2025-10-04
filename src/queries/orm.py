from sqlalchemy import text
from database import async_engine,session_async
from models import Base, Users

async def create_tables():
    async_engine.echo = False
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async_engine.echo = True

async def insert_data(name, email):
    user = Users(name=name, email=email)
    async with session_async() as session:
        session.add(user)
        await session.commit()
