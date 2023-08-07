from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

# Import database connection utilities.
from app.database.connection import get_db
# Import HuggingFace model interactions.
from app.transformers.model_interaction import HuggingFaceModel 
# Import Pydantic and SQLAlchemy ORM models.
from app.models.json_schema_models import Question  
from app.database.models import StudentData  
# Import NLP utilities and CRUD operations.
from app.transformers.nlp_utils import extract_keywords
from app.database.crud import fetch_data_based_on_keywords

router = APIRouter()

# Initialize the HuggingFace model.
model = HuggingFaceModel() 

@router.post("/ask", response_model=str)
def get_response(question: Question, db: Session = Depends(get_db)):
    """
    Given a question about data, this endpoint processes the question,
    interacts with relevant databases or data sources, and generates an insightful response.
    """
    try:
        # 1. Extract keywords from the input question.
        keywords = extract_keywords(question.question_text)
        # 2. Retrieve relevant data based on the extracted keywords.
        relevant_data = fetch_data_based_on_keywords(keywords)

        # 3. Format the retrieved data to provide it as context to the model.
        formatted_data = format_data_for_question(relevant_data)

        # 4. Combine the input question with the formatted data for context.
        enhanced_question = f"{question.question_text} Based on the data: {formatted_data}"

        # 5. Generate a response using the Hugging Face model.
        response = model.generate_response(enhanced_question)

        return response

    except Exception as e:
        # Handle any unexpected exceptions and return a 500 status code.
        raise HTTPException(status_code=500, detail=str(e))


def format_data_for_question(data: list) -> str:
    """
    Format the extracted data into a string to provide as context to the model.
    This function needs customization based on the structure of the 'StudentData' model.
    """
    formatted_data = ""
    # Loop through each record and format it for easy readability and context.
    for record in data:
        formatted_data += f"Timestamp: {record.Timestamp}, Gender: {record.Gender}, Study Year: {record.StudyYear}, Department: {record.Department}, Devices Used: {record.NumDevices}, CGPA: {record.RecentCGPA}, CGPA Trend: {record.CGPAIncrease}, Average Device Usage for Academic Purposes: {record.AvgDeviceUsage}, Purpose of Device Purchase: {record.PurposeOfDevice};\n"
    return formatted_data
