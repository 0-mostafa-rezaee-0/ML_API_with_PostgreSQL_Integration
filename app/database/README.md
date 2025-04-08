# Database Module

This module contains all the database-related components for the ML API with PostgreSQL Integration.

## Structure

- `__init__.py`: Exports components for easy importing
- `models.py`: SQLAlchemy ORM models
- `schema.py`: Pydantic models for request/response validation
- `crud.py`: Database operations (Create, Read, Update, Delete)
- `session.py`: Database connection and session management
- `deps.py`: FastAPI dependency injection

## Components

### Models

The primary model is `IrisPrediction`, which stores:

- Iris flower measurements (sepal_length, sepal_width, petal_length, petal_width)
- Prediction results (prediction integer and prediction_label string)
- Metadata (id, created_at)

### Schemas

Pydantic models for type validation:

- `IrisFeatures`: Input model for prediction requests
- `PredictionBase`: Base model with common attributes
- `PredictionCreate`: Model for creating predictions
- `PredictionInDB`: Model for predictions as stored in database
- `PredictionResponse`: Response model for prediction endpoint

### Database Operations

- `create_prediction()`: Save a prediction to the database
- `get_prediction()`: Retrieve a specific prediction by ID
- `get_all_predictions()`: Get all predictions with pagination
- `delete_prediction()`: Delete a prediction by ID

## Usage

Import components from the module:

```python
from app.database import (
    engine, Base, get_db, IrisPrediction, create_prediction,
    get_prediction, get_all_predictions
)
```

Create database tables:

```python
Base.metadata.create_all(bind=engine)
```

Use the dependency injection in FastAPI:

```python
@app.get("/predictions")
async def get_predictions(db: Session = Depends(get_db)):
    return get_all_predictions(db)
```

## Directory Structure

```
database/
├── __init__.py          # Package initialization and exports
├── session.py           # Database session configuration
├── deps.py              # FastAPI dependency injection
├── models.py            # SQLAlchemy ORM models
├── schema.py            # Pydantic schemas
├── crud.py              # Database CRUD operations
├── migrations/          # Alembic configuration
│   ├── env.py           # Migration environment configuration
│   ├── script.py.mako   # Migration script template
│   └── versions/        # Migration version directory (currently empty)
```

## Components

### Core Files

- **`__init__.py`**: Exports the main components from the database package for easy imports in other modules.

- **`session.py`**: Sets up the SQLAlchemy engine, session factory, and Base class for declarative models. It configures the database connection using the URL from settings.

- **`deps.py`**: Provides dependency injection utilities for FastAPI, particularly the `get_db()` function which yields a database session for API endpoints.

- **`models.py`**: Defines SQLAlchemy ORM models that map to database tables. The current model is:
  - `IrisPrediction`: Stores Iris flower predictions with input features and results.

- **`schema.py`**: Contains Pydantic models for:
  - Request validation (`IrisFeatures`)
  - Response serialization (`PredictionResponse`, `PredictionInDB`)

- **`crud.py`**: Implements database operations:
  - Create prediction records
  - Retrieve individual predictions
  - List multiple predictions with pagination

### Database Schema Management

The `migrations/` directory contains [Alembic](https://alembic.sqlalchemy.org/) configuration for database schema management:

- **`env.py`**: Configuration for the migration environment
- **`script.py.mako`**: Template for generating migration scripts
- **`versions/`**: Directory where migration scripts would be stored (currently empty)

While Alembic is configured, this project currently uses a direct table creation approach rather than migration scripts. Tables are created at application startup through SQLAlchemy's `Base.metadata.create_all()` method in `app/main.py` and through the custom setup script in `scripts/db_setup.py`.

## Database Model

The main database model is `IrisPrediction`, which stores:

- Input features (sepal_length, sepal_width, petal_length, petal_width)
- Prediction result (prediction as integer)
- Prediction label (human-readable class name)
- Creation timestamp

## Usage

The database components are used within the FastAPI application through dependency injection. Typical usage pattern:

```python
@app.post("/predict")
async def predict(data: IrisFeatures, db: Session = Depends(get_db)):
    # Use the database session for operations
    prediction_obj = IrisPrediction.from_request(features, prediction)
    db_prediction = create_prediction(db, prediction_obj)
```

## Schema Changes

To make database schema changes:

1. Modify the SQLAlchemy models in `models.py`
2. Restart the application, which will automatically update the schema using `Base.metadata.create_all()`

If you need to switch to a migration-based approach:

1. Make changes to SQLAlchemy models in `models.py`
2. Generate a migration script:
   ```
   alembic revision --autogenerate -m "Description"
   ```
3. Apply the migration:
   ```
   alembic upgrade head
   ```

The direct table creation approach was chosen for simplicity in a containerized environment where databases are often recreated from scratch. 