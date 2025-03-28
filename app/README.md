# Application Directory

This directory contains the core application code for the ML API with PostgreSQL integration. The application is built using FastAPI and integrates a machine learning model for Iris flower classification with PostgreSQL database for storing predictions.

## Directory Structure

```
app/
├── main.py              # Main FastAPI application entry point
├── config.py            # Application configuration settings
├── database.py          # Main database connection configuration
├── database/            # Database components
│   ├── __init__.py      # Package initialization
│   ├── crud.py          # Database CRUD operations
│   ├── deps.py          # Dependency injection for database
│   ├── models.py        # SQLAlchemy models
│   ├── schema.py        # Pydantic schemas for request/response
│   ├── session.py       # Database session management
│   └── migrations/      # Alembic database migrations
```

## Components

### Core Files

- **`main.py`**: The main FastAPI application that includes route definitions, middleware configuration, model loading, and API endpoints. It serves as the entry point for the application.

- **`config.py`**: Contains application configuration using Pydantic settings management. It handles environment variables, default values, and configuration validation.

- **`database.py`**: Configures the main database connection and provides essential database utilities.

### Database Package

The `database/` directory contains all database-related components:

- **`models.py`**: Defines SQLAlchemy ORM models that represent database tables
- **`schema.py`**: Defines Pydantic models for request/response validation and serialization
- **`crud.py`**: Implements Create, Read, Update, Delete operations for database entities
- **`session.py`**: Manages database session creation and configuration
- **`deps.py`**: Provides dependency injection utilities for FastAPI
- **`migrations/`**: Contains Alembic migration scripts and configuration

## API Endpoints

The application exposes the following endpoints:

- `GET /`: Root endpoint with welcome message
- `GET /health`: Health check endpoint
- `POST /predict`: Endpoint to make Iris flower predictions and store in database
- `GET /predictions`: Retrieve all stored predictions with pagination
- `GET /predictions/{prediction_id}`: Retrieve a specific prediction by ID

## ML Model Integration

The application loads a pre-trained Scikit-learn model for Iris classification from the `models/` directory at startup. Predictions are made using this model and then stored in the PostgreSQL database.

## Database Integration

The PostgreSQL database is used to:
1. Store prediction inputs and results
2. Retrieve prediction history
3. Allow for tracking and analysis of prediction patterns

## Usage

This application is designed to be run using Docker Compose, which will set up both the FastAPI application and the PostgreSQL database:

```bash
docker-compose up
```

Once running, the API is accessible at http://localhost:8000 with API documentation at http://localhost:8000/docs. 