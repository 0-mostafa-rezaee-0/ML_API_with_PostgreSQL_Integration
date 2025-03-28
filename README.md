# ML API with PostgreSQL Integration

This project implements a Machine Learning API using FastAPI and PostgreSQL for data persistence. It provides a robust framework for deploying machine learning models with database integration.

## Features

- FastAPI for high-performance API development
- PostgreSQL integration using SQLAlchemy
- Docker and Docker Compose setup for development and production environments
- ML model serving capabilities using the Iris dataset
- Prediction history stored in PostgreSQL database
- RESTful API endpoints for predictions and retrieving prediction history
- Database migrations using Alembic

## Project Structure

```
ML_API_with_PostgreSQL_Integration/
├── app/                    # Main application directory
│   ├── main.py            # FastAPI application
│   ├── config.py          # Settings and configuration
│   ├── database/          # Database components
│   │   ├── __init__.py
│   │   ├── crud.py        # Database operations
│   │   ├── deps.py        # Dependency injection
│   │   ├── models.py      # SQLAlchemy models
│   │   ├── schema.py      # Pydantic schemas
│   │   └── session.py     # Database session
├── models/                # ML model files
│   ├── ml_model.pkl       # Trained Iris classifier model
│   └── README.md          # Model documentation
├── data/                  # Data files
├── tests/                 # Test files
├── docker/                # Docker configuration
├── scripts/               # Utility scripts
├── notebooks/             # Jupyter notebooks
├── assets/                # Static files
├── alembic.ini            # Alembic configuration
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ML_API_with_PostgreSQL_Integration
   ```

2. Create a `.env` file in the root directory:
   ```
   DATABASE_URL=postgresql://user:password@db:5432/ml_api_db
   SECRET_KEY=your-secret-key-here
   ```

3. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `POST /predict`: Make an Iris prediction and save to database
- `GET /predictions`: Get all prediction records with pagination
- `GET /predictions/{prediction_id}`: Get a specific prediction by ID

## Prediction Input Format

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

## Development

### Running Tests
```bash
pytest
```

### Database Migrations
```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
