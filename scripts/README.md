# Scripts

This directory contains utility scripts and automation tools used in the project.

- You can easily adapt the repository to work with any dataset of your choice.
- The structure is flexible and can be applied to various machine learning models, including regression, classification, and clustering.

## Contents

- **`train.py`**: Script for training a machine learning model on the Iris dataset
  - Loads data, trains a LogisticRegression model
  - Evaluates model performance
  - Saves the model to the models directory

- **`db_setup.py`**: Script for setting up the PostgreSQL database
  - Creates the iris_predictions table if it doesn't exist
  - Handles database connection using SQLAlchemy
  - Provides useful database utilities

## Database Integration

The scripts in this directory are designed to work with both the ML components and PostgreSQL:
- `train.py` focuses on model training and evaluation
- `db_setup.py` handles database setup and initialization
- Together, they provide a complete workflow from data to deployed model with database persistence

## Usage

The scripts can be run from the command line or imported as modules:

```bash
# To train the model
python scripts/train.py

# To set up the database
python scripts/db_setup.py
```

## Important Notes

- Keep scripts modular and well-documented
- Include docstrings and type hints
- Add error handling and logging
- Use consistent coding style
- Test scripts thoroughly before deployment
- Document dependencies and requirements 