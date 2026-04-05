from sqlalchemy import Column, String, Boolean
from app.models.base import BaseModel


class Todo(BaseModel):
    __tablename__ = "todos"

    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)