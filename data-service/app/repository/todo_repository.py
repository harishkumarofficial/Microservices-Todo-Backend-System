from sqlalchemy.orm import Session
from app.models.todo import Todo


class TodoRepository:

    @staticmethod
    def create_todo(db: Session, title: str, description: str):
        todo = Todo(title=title, description=description)
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return todo

    @staticmethod
    def get_todos(db: Session):
        return db.query(Todo).filter(Todo.is_deleted == False).all()

    @staticmethod
    def get_todo_by_id(db: Session, todo_id: int):
        return db.query(Todo).filter(
            Todo.id == todo_id,
            Todo.is_deleted == False
        ).first()

    @staticmethod
    def update_todo(db: Session, todo, title: str, description: str, is_completed: bool):
        todo.title = title
        todo.description = description
        todo.is_completed = is_completed
        db.commit()
        db.refresh(todo)
        return todo

    @staticmethod
    def delete_todo(db: Session, todo):
        todo.is_deleted = True
        db.commit()