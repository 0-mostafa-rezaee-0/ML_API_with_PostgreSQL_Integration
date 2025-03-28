import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.database import Base
from app.database.deps import get_db
from app.main import app

# Create test database in memory
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Set up / tear down
@pytest.fixture(scope="function")
def test_db():
    # Create the test database and tables
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Clean up after the test
        Base.metadata.drop_all(bind=engine)

# Override the get_db dependency
@pytest.fixture(scope="function")
def client(test_db):
    # Dependency override
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Welcome" in response.json()["message"]

def test_predict_valid_input(client):
    # Test with Iris setosa features
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "prediction" in data
    assert "prediction_label" in data
    assert "input_features" in data
    assert len(data["input_features"]) == 4

def test_get_predictions(client):
    # First, create a prediction
    client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )
    
    # Now get the predictions
    response = client.get("/predictions")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert "id" in data[0]
    assert "prediction" in data[0]
    assert "prediction_label" in data[0]

def test_get_prediction_by_id(client):
    # First, create a prediction
    client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )
    
    # Get all predictions to find the ID
    all_preds = client.get("/predictions").json()
    pred_id = all_preds[0]["id"]
    
    # Now get the specific prediction
    response = client.get(f"/predictions/{pred_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == pred_id
    assert "prediction" in data
    assert "prediction_label" in data

def test_predict_invalid_input(client):
    # Test with missing features
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5
            # missing petal_length and petal_width
        }
    )
    assert response.status_code == 422  # Validation error

def test_predict_invalid_values(client):
    # Test with invalid data types
    response = client.post(
        "/predict",
        json={
            "sepal_length": "invalid",
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )
    assert response.status_code == 422  # Validation error

def test_get_nonexistent_prediction(client):
    # Test retrieving a prediction that doesn't exist
    response = client.get("/predictions/999")
    assert response.status_code == 404  # Not found 