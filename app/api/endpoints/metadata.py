from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Dict, Any

from app.database.connection import get_db
from app.storage.s3_operations import fetch_metadata

router = APIRouter()

@router.get("/metadata/{document_id}", response_model=Dict[str, Any])  # response_model is a placeholder. Adjust it to fit your needs.
def get_metadata(document_id: str, db: Session = Depends(get_db)):
    """
    Given a document ID, this endpoint will fetch its metadata from the blob store.
    """
    try:
        # Placeholder for any pre-processing needed for the document_id.
        
        # Fetch the metadata from the blob store.
        metadata = fetch_metadata(document_id)

        return metadata

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
