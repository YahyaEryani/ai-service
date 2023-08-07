from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = "mysql+pymysql://root:Blablabla%4012345@localhost/student-data"

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# Instantiate the database object globally
database = SessionLocal()

def get_db():
    """
    Dependency function to get a database session.
    This ensures a session is opened and closed for each request.
    """
    try:
        yield database
    finally:
        database.close()
