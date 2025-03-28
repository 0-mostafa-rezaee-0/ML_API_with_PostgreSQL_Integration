from sqlalchemy.orm import Session
from app.database.models import IrisPrediction

def create_prediction(db: Session, prediction_data: IrisPrediction):
    """
    Create a new prediction record in the database
    """
    db.add(prediction_data)
    db.commit()
    db.refresh(prediction_data)
    return prediction_data

def get_prediction(db: Session, prediction_id: int):
    """
    Get a specific prediction by ID
    """
    return db.query(IrisPrediction).filter(IrisPrediction.id == prediction_id).first()

def get_all_predictions(db: Session, skip: int = 0, limit: int = 100):
    """
    Get all prediction records with pagination
    """
    return db.query(IrisPrediction).offset(skip).limit(limit).all() 