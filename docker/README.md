# Docker

This directory contains Dockerfiles for setting up and running different components of the project in isolated environments. Docker allows for consistent and reproducible environments, making it easier to deploy and manage applications.

## Contents

- **`Dockerfile`**: This Dockerfile is used to build a Docker image for running the FastAPI application with PostgreSQL integration. It includes:
  - **Base Image**: Uses `python:3.10-slim` as the base image for a lightweight Python environment.
  - **Dependencies**: Installs required system packages (`build-essential`, `libpq-dev`) and Python packages from `requirements.txt`.
  - **Database Setup**: Includes an entrypoint script to wait for PostgreSQL to become available and set up the database tables.
  - **Port Exposure**: Exposes port 8000 for the FastAPI application.
  - **Command**: Runs the FastAPI application using Uvicorn.

- **`Dockerfile.jupyter`**: This Dockerfile is used to build a Docker image for running Jupyter Notebook and JupyterLab with PostgreSQL support. It includes:
  - **Base Image**: Uses `python:3.10-slim` for a lightweight Python environment.
  - **PostgreSQL Support**: Installs PostgreSQL client libraries for database access from notebooks.
  - **Dependencies**: Installs required Python packages from `requirements.txt` and additional packages for Jupyter.
  - **Port Exposure**: Exposes port 8888 for Jupyter Notebook.
  - **Command**: Runs Jupyter Notebook, allowing access without a token for ease of use.

## Docker Compose

The project uses Docker Compose to orchestrate multiple services:

1. **Web Service**: Runs the FastAPI application with PostgreSQL integration
2. **Database Service**: Runs PostgreSQL for data persistence
3. **Jupyter Service**: Optional service for data exploration and model development

The services are configured in the `docker-compose.yml` file at the root of the project.

## Usage

To build and run the Docker images, navigate to the root of the project and use Docker Compose:

```bash
# Start all services
docker-compose up

# Start only web and database services
docker-compose up web db

# Build and start with rebuilt images
docker-compose up --build
```

Access the services at:
- FastAPI application: http://localhost:8000
- FastAPI documentation: http://localhost:8000/docs
- Jupyter Notebook (if enabled): http://localhost:8888

These Dockerfiles provide a convenient way to set up and run the project's components in isolated environments, ensuring consistency across different development and production setups. 