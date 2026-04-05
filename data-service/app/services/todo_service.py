from sqlalchemy.orm import Session
from app.repository.todo_repository import TodoRepository


class TodoService:

    @staticmethod
    def create_todo(db: Session, title: str, description: str):
        return TodoRepository.create_todo(db, title, description)

    @staticmethod
    def get_todos(db: Session):
        return TodoRepository.get_todos(db)

    @staticmethod
    def update_todo(db: Session, todo_id: int, title: str, description: str, is_completed: bool):
        todo = TodoRepository.get_todo_by_id(db, todo_id)
        if not todo:
            return None
        return TodoRepository.update_todo(db, todo, title, description, is_completed)

    @staticmethod
    def delete_todo(db: Session, todo_id: int):
        todo = TodoRepository.get_todo_by_id(db, todo_id)
        if not todo:
            return None
        TodoRepository.delete_todo(db, todo)
        return True