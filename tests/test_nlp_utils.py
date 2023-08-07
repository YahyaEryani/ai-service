import sys
sys.path.append('C:\\Users\\Yahya Al-Eryani\\Documents\\ai-service')
from app.database import crud, connection
from sqlalchemy.orm import Session

def test_get_data_by_keywords():
    # Assuming the get_db function is how you get your DB session
    db: Session = next(connection.get_db())
    
    # Define the keywords
    keywords = ['device', 'usage', 'students']
    
    # Fetch data using your crud function
    results = crud.fetch_data_based_on_keywords(keywords)
    
    # Print the results for review
    for result in results:
        print(result)

# Run the test
test_get_data_by_keywords()

