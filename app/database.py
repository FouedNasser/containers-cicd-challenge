from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

# Create the SQLAlchemy engine
# pool_pre_ping=True checks if the connection is alive before using it
engine = create_engine(settings.database_url, pool_pre_ping=True)

# Create a SessionLocal class. Each instance is a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our ORM models
Base = declarative_base()

# Dependency to get a DB session for a request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
