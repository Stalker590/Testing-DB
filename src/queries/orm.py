from sqlalchemy import text
from database import async_engine,session_async
from models import metadata_obj, Goods

async def create_tables():
    async_engine.echo = False
    # используем begin() чтобы выполнить все DDL в транзакции
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata_obj.create_all)
    async_engine.echo = True

async def insert_data(name, price):
    good = Goods(name=name, price=price)
    async with session_async() as session:
        session.add(good)
        await session.commit()
