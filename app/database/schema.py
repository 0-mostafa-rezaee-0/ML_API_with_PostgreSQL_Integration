from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class IrisFeatures(BaseModel):
    """Pydantic model for Iris prediction request"""
    sepal_length: float = Field(..., example=5.1, description="Sepal length in cm")
    sepal_width: float = Field(..., example=3.5, description="Sepal width in cm")
    petal_length: float = Field(..., example=1.4, description="Petal length in cm")
    petal_width: float = Field(..., example=0.2, description="Petal width in cm")
    
    class Config:
        json_schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }

class PredictionBase(BaseModel):
    """Base prediction model with common attributes"""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    prediction: int
    prediction_label: str

class PredictionCreate(PredictionBase):
    """Model for creating a prediction (no ID or timestamp)"""
    pass

class PredictionInDB(PredictionBase):
    """Model for prediction as stored in database, including ID and timestamp"""
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class PredictionResponse(BaseModel):
    """Response model for prediction endpoint"""
    status: str
    prediction: int
    prediction_label: str
    input_features: List[float]
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "prediction": 0,
                "prediction_label": "setosa",
                "input_features": [5.1, 3.5, 1.4, 0.2]
            }
        } 