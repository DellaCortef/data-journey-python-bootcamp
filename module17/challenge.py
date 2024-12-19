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
    __tablename__ = 'suppliers'

    # Columns in the table
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mobile = Column(String(20))
    email = Column(String(50))
    address = Column(String(100))

# Define the Product class (table)
class Product(Base):
    # Name of the table in the database
    __tablename__ = 'products'
    
    # Columns in the table
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    price = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    # Establish the relationship between suppliers and Products
    supplier = relationship("Supplier")

# Create an SQLite database (file: challenge_db.db) and enable SQL query logging
engine = create_engine('sqlite:///challenge_db.db', echo=True)

# Create all tables defined in the Base class (e.g., Supplier, Product)
Base.metadata.create_all(engine)

# Bind the engine to a session factory for generating database sessions
Session = sessionmaker(bind=engine)

# Create a session instance to interact with the database
session = Session()

# Inserting suppliers
try:
    with Session() as session: # Using session correctly with context manager
        suppliers = [
            Supplier(name="Supplier A", mobile="12345678", email="contato@a.com", address="Address A"),
            Supplier(name="Supplier B", mobile="87654321", email="contato@b.com", address="Address B"),
            Supplier(name="Supplier C", mobile="12348765", email="contato@c.com", address="Address C"),
            Supplier(name="Supplier D", mobile="56781234", email="contato@d.com", address="Address D"),
            Supplier(name="Supplier E", mobile="43217865", email="contato@e.com", address="Address E")
        ]
        session.add_all(suppliers)
        session.commit()
except SQLAlchemyError as e: # Catching SQLAlchemy exceptions
    print(f"Error when inserting suppliers: {e}")

# Inserting products
try:
    with Session() as session:
        products = [
            Product(name="Product 1", description="Product Description 1", price=100, supplier_id=1),
            Product(name="Product 2", description="Product Description 2", price=200, supplier_id=2),
            Product(name="Product 3", description="Product Description 3", price=300, supplier_id=3),
            Product(name="Product 4", description="Product Description 4", price=400, supplier_id=4),
            Product(name="Product 5", description="Product Description 5", price=500, supplier_id=5)
        ]
        session.add_all(products)
        session.commit()
except SQLAlchemyError as e: # Catching SQLAlchemy exceptions
    print(f"Error when inserting products: {e}")