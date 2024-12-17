from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Connect to in-memory SQLite
engine = create_engine("sqlite:///database_db", echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Creating tables in Database
Base.metadata.create_all(engine)


# assuming that engine has already been created
Session = sessionmaker(bind=engine)
session = Session()

with Session() as session:
    # Commit is automatically done here if there are no exceptions
    # Rollback is automatically called if an exception occurs
    # The session is automatically closed when leaving the with block
    new_user = User(name='Ana', age=25)
    session.add(new_user)