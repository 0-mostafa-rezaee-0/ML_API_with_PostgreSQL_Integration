#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Configure trap to handle signals
trap 'echo "Received SIGINT/SIGTERM, shutting down..."; exit 0' SIGINT SIGTERM

echo "Starting entrypoint script..."

# Function to check if PostgreSQL is ready
function wait_for_postgres() {
    # Check if we need to connect to PostgreSQL
    if [[ "$*" == *"jupyter"* ]] || [[ "$*" == *"notebook"* ]]; then
        echo "Jupyter detected, skipping PostgreSQL connection check"
        return 0
    fi
    
    echo "Waiting for PostgreSQL..."
    local retries=30
    local wait_time=2
    
    while ! nc -z db 5432; do
        if [ $retries -le 0 ]; then
            echo "Error: Failed to connect to PostgreSQL after multiple attempts" >&2
            exit 1
        fi
        
        echo "PostgreSQL not available yet, waiting ${wait_time}s... ($retries attempts left)"
        sleep $wait_time
        retries=$((retries-1))
    done
    
    echo "PostgreSQL started successfully"
}

# Wait for PostgreSQL to be available
wait_for_postgres "$@"

# Run database setup script for web container only
if [[ "$*" != *"jupyter"* ]] && [[ "$*" != *"notebook"* ]]; then
    echo "Setting up database..."
    if python scripts/db_setup.py; then
        echo "Database setup completed successfully"
    else
        echo "Error: Database setup failed" >&2
        exit 1
    fi
fi

# Start the application
echo "Starting application with command: $@"
exec "$@" 