from datetime import datetime

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from .core.database import get_db
from .core.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    summary=settings.APP_SUMMARY,
    description=settings.APP_DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/health", response_model_by_alias=True)
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"Health Status": "Database is healthy", "timestamp": datetime.now()}
