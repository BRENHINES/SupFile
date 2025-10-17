from datetime import datetime

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from .core.settings import settings


engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/health", response_model_by_alias=True)
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"Health Status": "Database is healthy", "timestamp": datetime.now()}
