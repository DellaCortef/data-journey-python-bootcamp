# Importing necessary libs and modules
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL for SQLite, using 'pokemon.db' file
SQLALCHEMY_DATABASE_URL = "sqlite:///./pokemon.db"

# Create the database engine to manage connections
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for defining ORM models that map to database tables
Base = declarative_base()
