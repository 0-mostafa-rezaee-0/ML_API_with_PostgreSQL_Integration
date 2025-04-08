#!/usr/bin/env python3
"""
Database setup script for ML API with PostgreSQL Integration.

This script creates the necessary database tables for the application.
It can be run directly or imported by other scripts.
"""

import os
import sys
import logging

# Add the parent directory to the path so we can import from app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import engine, Base
from app.config import settings

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_database():
    """Create all tables in the database."""
    try:
        logger.info(f"Setting up database with URL: {settings.DATABASE_URL}")
        
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
        
        return True
    except Exception as e:
        logger.error(f"Error setting up database: {str(e)}")
        return False

if __name__ == "__main__":
    # Run the setup if executed directly
    success = setup_database()
    sys.exit(0 if success else 1) 