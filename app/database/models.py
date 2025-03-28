from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class IrisPrediction(Base):
    __tablename__ = "iris_predictions"

    id = Column(Integer, primary_key=True, index=True)
    sepal_length = Column(Float, nullable=False)
    sepal_width = Column(Float, nullable=False)
    petal_length = Column(Float, nullable=False)
    petal_width = Column(Float, nullable=False)
    prediction = Column(Integer, nullable=False)
    prediction_label = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    @classmethod
    def from_request(cls, features, prediction):
        """Create a prediction record from request data and model prediction"""
        # Map prediction integer to species label
        species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
        prediction_label = species_map.get(prediction, "unknown")
        
        return cls(
            sepal_length=features[0],
            sepal_width=features[1],
            petal_length=features[2],
            petal_width=features[3],
            prediction=prediction,
            prediction_label=prediction_label
        ) 