from sqlalchemy import create_engine, Column, Integer, String, Float, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.transformers.nlp_utils import extract_keywords
from .models import StudentData
import os
from dotenv import load_dotenv

# Load environment variables from the .env file.
load_dotenv()

# Retrieve database URL from environment variables.
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an engine connected to the database.
engine = create_engine(DATABASE_URL)
# Create a local session factory bound to the engine.
SessionLocal = sessionmaker(bind=engine)

def fetch_data_based_on_keywords(keywords):
    """
    Fetch data records based on given keywords. 
    The function looks for the occurrence of keywords in various columns of the StudentData model.

    Args:
    - keywords (list): A list of keywords to search in the database.

    Returns:
    - list: A sorted list of StudentData records. Records that match more keywords are prioritized.
    """
    # Create a new session.
    session = SessionLocal()

    # Create conditions for each keyword for every column in the StudentData model.
    all_conditions = []
    for keyword in keywords:
        keyword_conditions = [
            StudentData.Timestamp.contains(keyword),
            StudentData.Gender.contains(keyword),
            StudentData.StudyYear.contains(keyword),
            StudentData.Department.contains(keyword),
            StudentData.RecentCGPA.contains(keyword),
            StudentData.CGPAIncrease.contains(keyword),
            StudentData.AvgDeviceUsage.contains(keyword),
            StudentData.PurposeOfDevice.contains(keyword)
        ]
        # If the keyword is numeric, also check it against the NumDevices column.
        if keyword.isdigit():
            keyword_conditions.append(StudentData.NumDevices == int(keyword))
        all_conditions.extend(keyword_conditions)

    # Execute the query that fetches records matching any of the keyword conditions.
    query = session.query(StudentData).filter(or_(*all_conditions))
    results = query.all()

    # Sort the results to prioritize records that match more keywords.
    results.sort(key=lambda record: sum([1 for keyword in keywords if keyword in str(record)]), reverse=True)

    # Close the session to release resources.
    session.close()

    return results