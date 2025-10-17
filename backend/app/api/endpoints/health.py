from datetime import datetime

from fastapi import Depends, APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.app.core.database import get_db


router = APIRouter()

@router.get("/health", response_model_by_alias=True)
def health_db_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"Health Status": "Database is healthy", "timestamp": datetime.now()}