from sqlalchemy import Column, Integer, String, Float, DateTime
from .connection import Base

# Define the ORM model for the 'student_data' table.
class StudentData(Base):
    """
    SQLAlchemy ORM model for the 'student_data' table in the database.

    This table stores various data attributes related to students, such as 
    gender, study year, department, devices used, CGPA details, and more.

    Attributes:
    - id (Integer): A unique autoincremented identifier for the student record.
    - Timestamp (DateTime): The date and time when the record was added.
    - Gender (String): The gender of the student.
    - StudyYear (String): The year of study of the student.
    - Department (String): The department in which the student is enrolled.
    - NumDevices (Integer): Number of devices owned by the student.
    - RecentCGPA (String): The most recent CGPA of the student.
    - CGPAIncrease (String): Indicates if the student's CGPA has increased or not.
    - AvgDeviceUsage (String): The average number of devices used by the student for academic purposes.
    - PurposeOfDevice (String): The main purpose for which the student purchased the device(s).
    """
    
    # Define the table name.
    __tablename__ = "student_data"
    
    # Define the columns of the table.
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier
    Timestamp = Column(DateTime, primary_key=True, index=True)  # Date and time of data entry
    Gender = Column(String(10))  # Gender of the student
    StudyYear = Column(String(100))  # Year of study of the student
    Department = Column(String(100))  # Department of the student
    NumDevices = Column(Integer)  # Number of devices owned by the student
    RecentCGPA = Column(String(100))  # Most recent CGPA of the student
    CGPAIncrease = Column(String(10))  # Indicates if CGPA has increased or not
    AvgDeviceUsage = Column(String(100))  # Average device usage for academic purposes
    PurposeOfDevice = Column(String(255))  # Main purpose for purchasing the device
