from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./data/database.db"

# Async engine
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, 
    echo=False, 
    future=True
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Base class for models
Base = declarative_base()