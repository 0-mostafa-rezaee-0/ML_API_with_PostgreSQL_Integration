<div align="center">
    <img src="assets/logo.png" alt="ML API with PostgreSQL Integration" width="80%">
</div>

# ML API with PostgreSQL Integration

- ML Engineering best practices with database persistence
- ML model deployment as a FastAPI service with PostgreSQL integration, containerized with Docker for scalability and reproducibility

---

- $\textcolor{#FF4500}{\text{You can easily adapt the repository to work with any dataset of your choice.}}$
- The structure is flexible and can be applied to various machine learning models, including $\textcolor{#1E90FF}{\text{regression, classification, and clustering}}$.

---

***Table of Contents***

<details open>
  <summary><a href="#1-about-this-repository"><i><b>1. About this Repository</b></i></a></summary>
  <div>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#11-who-is-this-project-for">1.1. Who Is This Project For?</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#12-what-will-you-learn">1.2. What Will You Learn?</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#13-prerequisites">1.3. Prerequisites</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#14-contents-of-this-repository">1.4. Contents of this Repository</a><br>
  </div>
</details>
&nbsp;

<details>
  <summary><a href="#2-project-structure"><i><b>2. Project Structure</b></i></a></summary>
  <div>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#21-production-environment-dockerization">2.1. Production Environment (Dockerization)</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#22-machine-learning-components">2.2. Machine Learning Components</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#23-database-integration-components">2.3. Database Integration Components</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#24-testing-components">2.4. Testing Components</a><br>
  </div>
</details>
&nbsp;

<div>
  &nbsp;&nbsp;&nbsp;&nbsp;<a href="#3-project-files-and-folders-overview"><i><b>3. Project Files and Folders Overview</b></i></a>
</div>
&nbsp;

<details>
  <summary><a href="#4-how-to-use-and-test-the-project"><i><b>4. How to Use and Test the Project</i></b></a></summary>
  <div>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#41-build-and-start-the-containers">4.1. Build and Start the Containers</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#42-test-the-api-endpoints">4.2. Test the API Endpoints</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#43-run-the-tests">4.3. Run the Tests</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#44-use-jupyter-for-development">4.4. Use Jupyter for Development</a><br>
  </div>
</details>
&nbsp;

<details>
  <summary><a href="#5-database-setup"><i><b>5. Database Setup</b></i></a></summary>
  <div>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#51-direct-table-creation">5.1. Direct Table Creation</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#52-using-migrations">5.2. Using Migrations</a><br>
  </div>
</details>
&nbsp;

<div>
  &nbsp;&nbsp;&nbsp;&nbsp;<a href="#6-summary"><i><b>6. Summary</b></i></a>
</div>
&nbsp;

<div>
  &nbsp;&nbsp;&nbsp;&nbsp;<a href="#7-for-additional-questions"><i><b>7. For Additional Questions</b></i></a>
</div>
&nbsp;

# 1. About this Repository

This project demonstrates an end-to-end ML engineering workflow with database integration. You can train a machine learning model, serve it using a FastAPI application, store predictions in a PostgreSQL database, and experiment interactively with Jupyter Notebook – all within Docker containers. The project is designed to be reproducible and maintainable.

## 1.1. Who Is This Project For?

This project is designed for anyone interested in machine learning, API development, database integration, or containerization with Docker. Whether you're a student, developer, or data scientist, this resource will guide you through building and deploying a machine learning API with database persistence using FastAPI, PostgreSQL, and Docker.

## 1.2. What Will You Learn?

By the end of this project, you will:
- Develop a foundational understanding of FastAPI and its setup
- Learn how to integrate PostgreSQL with a FastAPI application
- Understand how to containerize applications using Docker
- Explore how to train and deploy simple machine learning models
- Work with practical examples to build scalable APIs with data persistence
- Gain insights into storing and retrieving ML predictions from a database

## 1.3. Prerequisites

This project is suitable for three types of learners:

1. **For those familiar with Docker, FastAPI, and databases**: You can dive straight into the deployment phase. The examples and configurations provided will help you enhance your skills and explore best practices in building and deploying APIs with database integration.

2. **For those who know Docker and FastAPI but are new to database integration**: This project will introduce you to integrating PostgreSQL with FastAPI, guiding you through building and deploying an API with database persistence.

3. **For beginners**: This project is designed with you in mind. You'll start with the basics, learning how to set up Docker, FastAPI, and PostgreSQL, and then move on to building and deploying a machine learning model with database integration.

## 1.4. Contents of this Repository 

```
Folder PATH listing
.
+---app                           <-- Contains the main application code
|   |   config.py                 <-- Application configuration
|   |   database.py               <-- Database connection configuration
|   |   main.py                   <-- Main FastAPI application
|   |
|   \---database                  <-- Database components
|       |   crud.py               <-- Database CRUD operations
|       |   deps.py               <-- Dependency injection
|       |   models.py             <-- SQLAlchemy models
|       |   schema.py             <-- Pydantic schemas
|       |   session.py            <-- Database session management
|       |
|       \---migrations            <-- Alembic migrations
|
+---assets                        <-- Contains static assets (images, styles, etc.)
|       logo.png                  <-- Project logo image
|
+---data                          <-- Directory for storing datasets
|       original_dataset.csv      <-- Example dataset for model training
|
+---docker                        <-- Contains Docker configuration files
|       Dockerfile                <-- Dockerfile for building the API service
|       Dockerfile.jupyter        <-- Dockerfile for setting up Jupyter Notebook
|
+---models                        <-- Stores trained machine learning models
|       ml_model.pkl              <-- Serialized ML model
|
+---notebooks                     <-- Jupyter notebooks for experiments and analysis
|       data_exploration.ipynb    <-- Notebook for data exploration
|       train_dev.ipynb           <-- Notebook for training and development
|
+---scripts                       <-- Contains utility scripts
|       db_setup.py               <-- Script for setting up the database
|       train.py                  <-- Script for training models
|
+---tests                         <-- Contains automated tests
|       __init__.py               <-- Initializes the tests package
|       test_api.py               <-- API endpoint tests
|
|   .gitignore                    <-- Specifies files to ignore in Git version control
|   alembic.ini                   <-- Alembic configuration
|   docker-compose.yml            <-- Docker Compose configuration
|   LICENSE                       <-- License information for the project
|   README.md                     <-- Project overview and instructions
|   requirements.txt              <-- Lists Python dependencies
```

# 2. Project Structure

## 2.1. Production Environment (Dockerization)

- **docker/Dockerfile**  
  Dockerfile for building the FastAPI application container. It installs the dependencies required for serving the model and connecting to PostgreSQL in a production environment.

- **docker/Dockerfile.jupyter**  
  Dockerfile for building the Jupyter Notebook container. It installs additional dependencies for interactive development and experimentation, including PostgreSQL client libraries.

- **docker-compose.yml**  
  Defines three services:
  - `web`: Runs the FastAPI application, exposing it on port 8000.
  - `jupyter`: Runs a Jupyter Notebook server accessible on port 8888.
  - `db`: Runs PostgreSQL database for storing predictions.
  
  The project uses volume mounts to ensure data persistence and code accessibility across containers.

## 2.2. Machine Learning Components

- **models/ml_model.pkl**  
  A pre-trained machine learning model for Iris flower classification.

- **scripts/train.py**  
  A training script that loads the Iris dataset, trains a logistic regression model, evaluates its performance, and saves the trained model.
  
- **app/main.py**  
  The FastAPI application that loads the model and exposes several endpoints for making predictions and accessing the database.

## 2.3. Database Integration Components

- **app/database/**  
  Contains all the database-related components:
  - **models.py**: Defines SQLAlchemy ORM model for storing predictions.
  - **schema.py**: Defines Pydantic models for request/response validation.
  - **crud.py**: Implements database operations for creating and retrieving predictions.
  - **session.py**: Manages database session creation and configuration.
  - **deps.py**: Provides dependency injection for FastAPI.

- **scripts/db_setup.py**  
  A script for setting up the PostgreSQL database and creating necessary tables.

## 2.4. Testing Components

- **tests/**  
  Contains automated tests for the API endpoints and database operations:
  - Tests for health check and root endpoints
  - Tests for prediction endpoint and database storage
  - Tests for retrieving predictions
  - Error handling tests

# 3. Project Files and Folders Overview

- **app/**  
  Contains the main application code:
  - **main.py:** Main FastAPI application with endpoints and model loading.
  - **config.py:** Application configuration settings using Pydantic.
  - **database.py:** Database connection configuration.
  - **database/:** Database components for PostgreSQL integration.

- **assets/**  
  Contains static assets like images and styles, including the project logo.

- **data/**  
  Directory for storing datasets used in the project, including the Iris dataset.

- **docker/**  
  Contains Docker configuration files:
  - **Dockerfile:** Builds the FastAPI API container.
  - **Dockerfile.jupyter:** Builds the Jupyter Notebook container.

- **models/**  
  Stores trained machine learning models, specifically the Iris classifier.

- **notebooks/**  
  Jupyter notebooks for experiments and analysis:
  - **data_exploration.ipynb:** Notebook for exploring the Iris dataset.
  - **train_dev.ipynb:** Notebook for model training and development.

- **scripts/**  
  Contains utility scripts:
  - **train.py:** Script for training the ML model.
  - **db_setup.py:** Script for setting up the PostgreSQL database.

- **tests/**  
  Contains automated tests for the application.

# 4. How to Use and Test the Project

## 4.1. Build and Start the Containers

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ML_API_with_PostgreSQL_Integration
   ```

2. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

This will start three containers:
- FastAPI application: available at http://localhost:8000
- PostgreSQL database: available at localhost:5432
- Jupyter Notebook: available at http://localhost:8888

## 4.2. Test the API Endpoints

Once the application is running, you can test the endpoints:

1. Swagger UI documentation:
   ```
   http://localhost:8000/docs
   ```

2. Make a prediction using curl:
   ```bash
   curl -X 'POST' \
     'http://localhost:8000/predict' \
     -H 'Content-Type: application/json' \
     -d '{
       "sepal_length": 5.1,
       "sepal_width": 3.5,
       "petal_length": 1.4,
       "petal_width": 0.2
     }'
   ```

3. Get all predictions:
   ```bash
   curl -X 'GET' 'http://localhost:8000/predictions'
   ```

## 4.3. Run the Tests

To run the automated tests:

```bash
docker-compose exec web pytest tests/
```

## 4.4. Use Jupyter for Development

Jupyter Notebook provides an interactive environment for data exploration, model development, and visualization. This project includes a containerized Jupyter Notebook server to facilitate development and experimentation.

### Accessing Jupyter Notebook

1. After starting the containers with `docker-compose up`, access the Jupyter Notebook interface at:
   ```
   http://localhost:8888
   ```

2. You'll be presented with the Jupyter file explorer. The project directory is mounted in the container, so you have access to all project files.

### Using the Provided Notebooks

The project includes several pre-configured notebooks in the `notebooks/` directory:

- **data_exploration.ipynb**: Explore and visualize the Iris dataset, including:
  - Distribution of feature values
  - Correlation between features
  - Visualizations of class separability

- **train_dev.ipynb**: Develop and evaluate the machine learning model, including:
  - Data preprocessing techniques
  - Model selection and hyperparameter tuning
  - Performance evaluation on validation data

### Creating New Notebooks

You can create new notebooks for your specific use cases:

1. Click the "New" button in the Jupyter interface and select "Python 3"
2. Your new notebook will have access to all the project dependencies
3. To connect to the PostgreSQL database from a notebook, use the same connection string as the main application

### Sharing Code Between Notebooks and the Application

The project structure allows you to:
- Develop and test code in notebooks
- Extract and refactor successful code into Python modules
- Import these modules in both the FastAPI application and other notebooks

This workflow enables rapid prototyping while maintaining code quality and reusability.

# 5. Database Setup

The project uses PostgreSQL for storing prediction data. There are two approaches to database schema management:

## 5.1. Direct Table Creation

By default, this project uses direct table creation for simplicity:

1. Tables are automatically created at application startup using SQLAlchemy's `Base.metadata.create_all()` method in `app/main.py`.
2. The custom setup script `scripts/db_setup.py` runs during container initialization to ensure tables exist.

This approach was chosen for simplicity in a containerized environment where databases are often recreated from scratch.

## 5.2. Using Migrations

While the project is configured with Alembic for migrations, it currently doesn't use migration scripts. To switch to a migration-based approach:

1. Modify the SQLAlchemy models in `app/database/models.py`
2. Generate a migration script:
   ```bash
   alembic revision --autogenerate -m "Description"
   ```
3. Apply the migration:
   ```bash
   alembic upgrade head
   ```

# 6. Summary

This project demonstrates how to build a machine learning API with PostgreSQL integration using FastAPI and Docker. It provides a complete framework for:

1. Training and serving machine learning models
2. Storing predictions in a PostgreSQL database
3. Retrieving prediction history
4. Running everything in Docker containers for reproducibility and scalability

The project is designed to be easily adaptable for different machine learning tasks and datasets while maintaining a strong focus on engineering best practices.

# 7. For Additional Questions

If you have any questions or encounter issues while working with this project, here are several resources to help you:

- **GitHub Issues**: Open an issue in the GitHub repository
- **Documentation**: Refer to the documentation in the respective README files within each directory
- **External Resources**:
  - [FastAPI Documentation](https://fastapi.tiangolo.com/)
  - [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
  - [PostgreSQL Documentation](https://www.postgresql.org/docs/)
  - [Docker Documentation](https://docs.docker.com/)
- **Contact**: Feel free to reach out to the maintainers of this project
