from typing import Generator
from sqlalchemy.orm import Session
from app.database.session import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """
    Dependency for FastAPI to get a database session.
    
    Creates a new database session for each request, closes it when the request is done.
    This ensures each request has its own session and is properly cleaned up.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 