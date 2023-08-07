from pydantic import BaseModel, Field
from typing import Optional

# Define a Pydantic model for a 'Question'.
class Question(BaseModel):
    """
    Pydantic model representing a data analyst's question.

    This model captures the main question text, its context, and the author. 
    The context and author fields are optional.

    Attributes:
    - question_text (str): The main content of the question.
    - question_context (Optional[str]): Additional context accompanying the main question.
    - question_author (Optional[str]): The individual who posed the question.

    Note: Pydantic's Field is used here to add constraints and metadata to the fields.
    """

    # Main content of the question. This field is required.
    question_text: str = Field(
        ...,  # Indicates that the field is required.
        title="Question Text",
        max_length=300,
        description="The text of the question from the data analyst",
    )

    # Optional field for any accompanying context to the main question.
    question_context: Optional[str] = Field(
        None,
        title="Question Context",
        max_length=1000,
        description="Any context that goes along with the question",
    )

    # Optional field indicating who posed the question.
    question_author: Optional[str] = Field(
        None,
        title="Question Author",
        max_length=50,
        description="The author of the question",
    )
