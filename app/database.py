# This file re-exports components from the database package for backward compatibility
# In a real project, you would use the package structure directly

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from app.database.session import engine, SessionLocal
from app.database.models import Base, IrisPrediction
from app.database.deps import get_db
from app.database.crud import (
    create_prediction,
    get_prediction,
    get_all_predictions,
    delete_prediction
)
from app.database.schema import (
    IrisFeatures,
    PredictionResponse,
    PredictionInDB,
    PredictionCreate,
    PredictionBase
) 