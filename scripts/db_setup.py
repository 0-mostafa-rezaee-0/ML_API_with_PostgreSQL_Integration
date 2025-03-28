import logging
import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Database connection settings
def get_db_url():
    """Get database URL from environment or use default"""
    return os.environ.get("DATABASE_URL", "postgresql://user:password@localhost:5432/ml_api_db")

def setup_database():
    """Create database and tables if they don't exist"""
    db_url = get_db_url()
    logger.info(f"Connecting to database: {db_url}")
    
    try:
        # Create engine 
        engine = create_engine(db_url)
        
        # Test connection
        with engine.connect() as conn:
            logger.info("Database connection successful")
            
            # Check if table exists and create if it doesn't
            table_exists = conn.execute(text(
                "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'iris_predictions')"
            )).scalar()
            
            if not table_exists:
                logger.info("Creating iris_predictions table")
                conn.execute(text("""
                CREATE TABLE iris_predictions (
                    id SERIAL PRIMARY KEY,
                    sepal_length FLOAT NOT NULL,
                    sepal_width FLOAT NOT NULL,
                    petal_length FLOAT NOT NULL,
                    petal_width FLOAT NOT NULL,
                    prediction INTEGER NOT NULL,
                    prediction_label VARCHAR NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """))
                conn.commit()
                logger.info("Table created successfully")
            else:
                logger.info("Table iris_predictions already exists")
        
        return True
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        return False

if __name__ == "__main__":
    logger.info("Starting database setup")
    result = setup_database()
    if result:
        logger.info("Database setup completed successfully")
    else:
        logger.error("Database setup failed")
        sys.exit(1) 