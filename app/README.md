# ML API with PostgreSQL Integration

This directory contains the main API application code organized in a modular structure.

## Components

### Main Application Files

- `main.py`: FastAPI application entry point with route definitions
- `config.py`: Configuration settings using Pydantic
- `database.py`: Re-exports database components (legacy file, use database/ package directly)

### Database Package

The `database/` directory contains a complete implementation of database integration:

- SQLAlchemy ORM models for storing predictions
- Pydantic models for request/response validation
- CRUD operations for database access
- Session management and dependency injection

See the [database README](./database/README.md) for detailed information.

## API Endpoints

The application provides the following endpoints:

- `GET /`: Root endpoint returning a welcome message
- `GET /health`: Health check endpoint for monitoring
- `POST /predict`: Make Iris flower predictions and store in database
- `GET /predictions`: Retrieve all predictions with pagination
- `GET /predictions/{prediction_id}`: Retrieve a specific prediction

## Configuration

Application configuration is defined in `config.py` and can be overridden using environment variables or a `.env` file. Important settings include:

- `DATABASE_URL`: PostgreSQL connection string
- `MODEL_PATH`: Path to the trained ML model
- `SECRET_KEY`: Secret key for security features

## Database Integration

The application uses SQLAlchemy ORM for database integration:

1. Models are defined in `database/models.py`
2. Database tables are created automatically at startup
3. Predictions are stored in the database when the `/predict` endpoint is called
4. Stored predictions can be retrieved via the `/predictions` endpoints 