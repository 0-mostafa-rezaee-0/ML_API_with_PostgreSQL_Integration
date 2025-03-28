# Models

This directory contains trained machine learning models used by the application for making predictions. 

- You can easily adapt the repository to work with any dataset of your choice.   
- The structure is flexible and can be applied to various machine learning models, including regression, classification, and clustering. 

## Contents

- **`ml_model.pkl`**: A pickled machine learning model trained on the Iris dataset. This model is:
  - Loaded by the FastAPI application at startup
  - Used to make predictions through the `/predict` endpoint
  - Trained to classify iris flowers into three species based on their measurements

## Model Details

The model is trained to predict iris flower species using four input features:
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

## Usage

The model is automatically loaded by the FastAPI application when it starts. The loading process is handled in `app/main.py`, and any errors during model loading are logged for debugging purposes.

## Important Notes

- Keep your trained models in this directory
- Models should be saved in pickle format (`.pkl`)
- Ensure model versions are tracked and documented
- Back up your models regularly
- Consider adding model performance metrics and training dates in model metadata 