from sqlalchemy import Column, Integer, DateTime, Boolean
from app.db.session import Base
from sqlalchemy.sql import func


class BaseModel(Base):
    __abstract__ = True  

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)