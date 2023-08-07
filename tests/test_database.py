from app.database.connection import get_db

def test_database_connection():
    db = get_db()
    assert db is not None
    # Add more assertions or tests related to database operations