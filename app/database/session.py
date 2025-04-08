from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Create database URL
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Create engine with appropriate connection settings
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,  # Helps with connection issues after idle periods
    connect_args={} if SQLALCHEMY_DATABASE_URL.startswith("postgresql") else {"check_same_thread": False}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Import and re-export Base from models
from app.database.models import Base 