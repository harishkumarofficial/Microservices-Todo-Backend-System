import grpc
from concurrent import futures

from app.grpc import todo_pb2
from app.grpc import todo_pb2_grpc

from app.db.session import SessionLocal
from app.services.todo_service import TodoService


class TodoGrpcService(todo_pb2_grpc.TodoServiceServicer):

    def CreateTodo(self, request, context):
        db = SessionLocal()
        try:
            todo = TodoService.create_todo(
                db,
                title=request.title,
                description=request.description
            )

            return todo_pb2.TodoResponse(
                id=todo.id,
                title=todo.title,
                description=todo.description,
                is_completed=todo.is_completed
            )
        finally:
            db.close()

    def GetTodos(self, request, context):
        db = SessionLocal()
        try:
            todos = TodoService.get_todos(db)

            todo_list = []
            for todo in todos:
                todo_list.append(
                    todo_pb2.TodoResponse(
                        id=todo.id,
                        title=todo.title,
                        description=todo.description,
                        is_completed=todo.is_completed
                    )
                )

            return todo_pb2.TodoListResponse(todos=todo_list)
        finally:
            db.close()


    def GetTodo(self, request, context):
        db = SessionLocal()
        try:
            todo = TodoService.get_todo(db, request.id)
            if not todo:
                return todo_pb2.TodoResponse()

            return todo_pb2.TodoResponse(
                id=todo.id,
                title=todo.title,
                description=todo.description,
                is_completed=todo.is_completed
            )
        finally:
            db.close()


    def UpdateTodo(self, request, context):
        db = SessionLocal()
        try:
            todo = TodoService.update_todo(
                db,
                request.id,
                request.title,
                request.description,
                request.is_completed
            )

            return todo_pb2.TodoResponse(
                id=todo.id,
                title=todo.title,
                description=todo.description,
                is_completed=todo.is_completed
            )
        finally:
            db.close()


    def DeleteTodo(self, request, context):
        db = SessionLocal()
        try:
            TodoService.delete_todo(db, request.id)
            return todo_pb2.Empty()
        finally:
            db.close()
            