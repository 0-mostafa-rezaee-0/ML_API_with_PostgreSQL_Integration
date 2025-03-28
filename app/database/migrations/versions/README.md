# Migration Versions Directory

This directory is intended to store Alembic migration version scripts. Currently, it's empty because this project uses direct table creation methods rather than migration scripts.

## Why This Directory Is Empty

In this project, database tables are created through two mechanisms:

1. **Direct SQLAlchemy Table Creation**: In `app/main.py`, tables are created at application startup using:
   ```python
   Base.metadata.create_all(bind=engine)
   ```
   This automatically creates all tables defined in the SQLAlchemy models if they don't exist.

2. **Custom Database Setup Script**: The `scripts/db_setup.py` script manually checks for the existence of tables and creates them if needed. This script is run as part of the Docker container startup process.

## When Migration Scripts Would Be Useful

Alembic migration scripts would be necessary in scenarios such as:

1. **Schema Evolution**: When you need to track changes to your database schema over time
2. **Complex Migrations**: For complex operations like adding columns with constraints, modifying data, or renaming tables
3. **Multiple Environments**: To ensure consistent database updates across development, staging, and production environments
4. **Team Collaboration**: When multiple developers need to synchronize database changes

## How To Generate Migration Scripts

If you decide to switch to a migration-based approach, you would:

1. Install Alembic in your environment:
   ```bash
   pip install alembic
   ```

2. Generate a migration script based on the current models:
   ```bash
   alembic revision --autogenerate -m "Create IrisPrediction table"
   ```
   This would create a new Python file in this directory with `upgrade()` and `downgrade()` functions.

3. Apply the migration:
   ```bash
   alembic upgrade head
   ```

4. Update the Docker entrypoint script to run migrations instead of direct table creation.

## Current Approach Benefits

The current direct table creation approach was chosen for simplicity and reliability, especially in a containerized environment where the database is often recreated from scratch. This approach ensures that the application always has the tables it needs without maintaining migration history. 