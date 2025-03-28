from pydantic import BaseModel
from datetime import datetime
from typing import List

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    status: str
    prediction: int
    prediction_label: str
    input_features: List[float]

class PredictionInDB(BaseModel):
    id: int
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    prediction: int
    prediction_label: str
    created_at: datetime
    
    class Config:
        from_attributes = True 