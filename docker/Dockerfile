FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create necessary directories if they don't exist
RUN mkdir -p /app/models

# Create an entrypoint script to handle database setup and app startup
RUN echo '#!/bin/bash\n\
# Wait for PostgreSQL to be ready\n\
echo "Waiting for PostgreSQL..."\n\
while ! nc -z db 5432; do\n\
  sleep 0.1\n\
done\n\
echo "PostgreSQL started"\n\
\n\
# Run database setup script\n\
echo "Setting up database..."\n\
python scripts/db_setup.py\n\
\n\
# Start the application\n\
echo "Starting application..."\n\
exec "$@"\n\
' > /app/docker-entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/docker-entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 