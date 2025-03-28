# Database Package

This directory contains the database components for the ML API with PostgreSQL integration. It implements a clean, modular architecture for database operations using SQLAlchemy ORM and Pydantic.

## Directory Structure

```
database/
├── __init__.py          # Package initialization and exports
├── session.py           # Database session configuration
├── deps.py              # FastAPI dependency injection
├── models.py            # SQLAlchemy ORM models
├── schema.py            # Pydantic schemas
├── crud.py              # Database CRUD operations
├── migrations/          # Alembic migrations
│   ├── env.py           # Migration environment configuration
│   ├── script.py.mako   # Migration script template
│   └── versions/        # Migration version scripts
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

### Database Migrations

The `migrations/` directory contains [Alembic](https://alembic.sqlalchemy.org/) configuration for database schema migrations:

- **`env.py`**: Configuration for the migration environment
- **`script.py.mako`**: Template for generating migration scripts
- **`versions/`**: Directory where migration scripts are stored

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

## Migrations

Database migrations are managed with Alembic. The migration workflow is:

1. Make changes to SQLAlchemy models in `models.py`
2. Generate a migration script:
   ```
   alembic revision --autogenerate -m "Description"
   ```
3. Apply the migration:
   ```
   alembic upgrade head
   ```

In this project, migrations are typically handled through the Docker entrypoint script, which runs the database setup automatically. 