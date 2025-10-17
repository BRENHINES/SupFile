from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    storage_used = Column(Integer, default=0)
    storage_quota = Column(Integer, default=32212254720)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())