#!/bin/bash

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Run database setup script
echo "Setting up database..."
python scripts/db_setup.py

# Start the application
echo "Starting application..."
exec "$@" 