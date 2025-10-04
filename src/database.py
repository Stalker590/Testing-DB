from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text 
from config import DATABASE_URL

async_engine = create_async_engine(DATABASE_URL)

session_async = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass