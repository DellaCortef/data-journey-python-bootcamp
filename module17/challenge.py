from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

# Create a base class for ORM models
Base = declarative_base()

# Define the Supplier class (table)
class Supplier(Base):
    # Name of the table in the database
    __tablename__ = 'supliers'

    # Columns in the table
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mobile = Column(String(20))
    email = Column(String(50))
    address = Column(String(100))

# Define the Product class (table)
class product(Base):
    # Name of the table in the database
    __tablename__ = 'products'
    
    # Columns in the table
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    # Establish the relationship between suppliers and Products
    suplier = relationship("Suplier")

# Create an SQLite database (file: challenge_db.db) and enable SQL query logging
engine = create_engine('sqlite:///challenge_db.db', echo=True)

# Create all tables defined in the Base class (e.g., Supplier, Product)
Base.metadata.create_all(engine)

# Bind the engine to a session factory for generating database sessions
Session = sessionmaker(bind=engine)

# Create a session instance to interact with the database
session = Session()

