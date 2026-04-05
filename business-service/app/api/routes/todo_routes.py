from fastapi import APIRouter
from app.services.todo_service import TodoService

from app.schemas.todo_schema import TodoCreateRequest, TodoUpdateRequest

router = APIRouter()
service = TodoService()


@router.post("/todo/create")
def create_todo(request: TodoCreateRequest ):
    return service.create_todo(request.title, request.description)


@router.get("/todos")
def get_todos():
    return service.get_todos()

# @router.get("/todo/{todo_id}")
# def get_todo(todo_id: int):
#     return service.get_todo(todo_id)


@router.put("/todo/update")
def update_todo(request: TodoUpdateRequest):
    return service.update_todo(
        request.id,
        request.title,
        request.description,
        # request.is_completed
    )


@router.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    return service.delete_todo(todo_id)