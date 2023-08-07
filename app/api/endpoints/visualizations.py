from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.visualization.charts import generate_bar_chart, generate_pie_chart

router = APIRouter()

@router.post("/bar-chart", response_model=str)  # Placeholder response_model, adjust according to your needs.
def get_bar_chart(question: str, db: Session = Depends(get_db)):
    """
    Given a question or data query, this endpoint will process it,
    fetch relevant data from the database, and generate a bar chart.
    """
    try:
        # Placeholder for any pre-processing needed for the question/query.
        
        # Fetch or generate the data for the bar chart.
        # For example:
        # data = db.query(...)

        # Generate the bar chart.
        # Assuming the function returns a string representation of the chart or a URL to it.
        chart = generate_bar_chart(data)

        return chart

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/pie-chart", response_model=str)  # Placeholder response_model, adjust according to your needs.
def get_pie_chart(question: str, db: Session = Depends(get_db)):
    """
    Given a question or data query, this endpoint will process it,
    fetch relevant data from the database, and generate a pie chart.
    """
    try:
        # Placeholder for any pre-processing needed for the question/query.

        # Fetch or generate the data for the pie chart.
        # This is a simplistic example, your actual query will likely be more complex.
        data = db.query(MyDataModel).filter(MyDataModel.question == question).all()

        # Generate the pie chart.
        # Assuming the function returns a string representation of the chart or a URL to it.
        chart = generate_pie_chart(data)

        return chart
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
