"""
数据库的引擎
数据库连接工厂
"""
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession, create_async_engine

from backend_service.config.settings import settings

session_engine: AsyncEngine | None = None
session_factory: async_sessionmaker[AsyncSession] | None = None

def init_db_engine():
    global session_engine, session_factory

    session_engine = create_async_engine(url=settings.database_url, echo=True)  # echo=True 可以显示SQL语句
    session_factory = async_sessionmaker(session_engine, expire_on_commit=False)

async def dispose_engine():
    await session_engine.dispose()