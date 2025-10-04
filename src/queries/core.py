from sqlalchemy import text
from database import async_engine
from models import metadata_obj

async def create_tables():
    async_engine.echo = False
    # используем begin() чтобы выполнить все DDL в транзакции
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata_obj.create_all)
    async_engine.echo = True

async def insert_data(name, price):
    async with async_engine.connect() as conn:
        await conn.execute(
            text("INSERT INTO goods (name, price) VALUES (:name, :price)"),
            [{"name": name, "price": price}]
        )
        await conn.commit()
        