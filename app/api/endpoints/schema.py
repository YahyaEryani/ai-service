from fastapi import APIRouter
from app.models.json_schema_models import Question  # assuming you moved your Pydantic model to app/models/schema.py

router = APIRouter()

@router.get("/schema", response_model=Question)
def get_schema():
    # FastAPI will automatically generate and serve the JSON Schema for the Question model.
    pass  # This function doesn't need to do anything.
