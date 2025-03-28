# Database Migrations

This directory contains the database migration configuration and scripts for the ML API with PostgreSQL integration. It uses [Alembic](https://alembic.sqlalchemy.org/), a lightweight database migration tool for SQLAlchemy.

## Directory Structure

```
migrations/
├── env.py           # Migration environment configuration
├── README.md        # This file
├── script.py.mako   # Template for migration scripts
└── versions/        # Migration version scripts
```

## Components

- **`env.py`**: Configures the migration environment, including:
  - Database connection settings
  - Target metadata (SQLAlchemy models)
  - Context configuration for online and offline migrations

- **`script.py.mako`**: A template used by Alembic to generate new migration scripts with consistent structure.

- **`versions/`**: Contains the actual migration scripts that define how to upgrade or downgrade the database schema. Each migration file includes:
  - Unique revision identifier
  - Dependencies on previous migrations
  - `upgrade()` function to apply changes
  - `downgrade()` function to revert changes

## Migration Workflow

The typical Alembic migration workflow is:

1. Make changes to your SQLAlchemy models in `app/database/models.py`

2. Generate a migration script:
   ```bash
   alembic revision --autogenerate -m "Description of changes"
   ```
   This will create a new file in the `versions/` directory with automatically generated upgrade and downgrade operations.

3. Review the generated migration script to ensure it accurately reflects your intended changes.

4. Apply the migration:
   ```bash
   alembic upgrade head
   ```
   This will run all pending migrations to bring your database schema up to date.

## Automatic Migrations

In this project, database setup and migrations are typically handled automatically through:

1. The Docker entrypoint script, which runs database setup on container start
2. The FastAPI application's startup sequence, which ensures tables exist

## Common Commands

```bash
# Generate a new migration
alembic revision --autogenerate -m "Add user table"

# Apply all pending migrations
alembic upgrade head

# Downgrade to a specific version
alembic downgrade <revision_id>

# Downgrade one version
alembic downgrade -1

# Get current version info
alembic current

# List migration history
alembic history --verbose
```

## Configuration

Alembic is configured through:
- `alembic.ini` in the project root
- `env.py` in this directory

The database URL is set from the application's configuration settings in `app/config.py`. 