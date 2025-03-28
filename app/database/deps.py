from typing import Generator
from .session import SessionLocal

def get_db() -> Generator:
    """
    Dependency function that yields database sessions.
    To be used in FastAPI dependency injection system.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 