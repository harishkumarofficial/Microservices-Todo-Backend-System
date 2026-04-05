import grpc
from app.grpc_clients import todo_pb2
from app.grpc_clients import todo_pb2_grpc
from google.protobuf.json_format import MessageToDict


class TodoGrpcClient:

    def __init__(self):
        # self.channel = grpc.insecure_channel("localhost:50051")
        self.channel = grpc.insecure_channel("data-service:50051")
        self.stub = todo_pb2_grpc.TodoServiceStub(self.channel)

    def create_todo(self, title: str, description: str):
        print("title:------------------->", title)
        print("description:----------------------->", description)
        response = self.stub.CreateTodo(
            todo_pb2.CreateTodoRequest(
                title=title,
                description=description
            )
        )
        # return response
        return MessageToDict(
            response,
            preserving_proto_field_name=True
            )

    def get_todos(self):
        response = self.stub.GetTodos(todo_pb2.Empty())
        return MessageToDict(
            response,
            preserving_proto_field_name=True
            )
        # return response


    # def get_todo(self, todo_id):
    #     return self.stub.GetTodo(
    #         todo_pb2.GetTodoRequest(id=todo_id)
    #     )

    # def update_todo(self, todo_id, title, description, is_completed):
    #     return self.stub.UpdateTodo(
    #         todo_pb2.UpdateTodoRequest(
    #             id=todo_id,
    #             title=title,
    #             description=description,
    #             is_completed=is_completed
    #         )
    #     )

    def update_todo(self, id: int, title: str, description: str):
        response = self.stub.UpdateTodo(
            todo_pb2.UpdateTodoRequest(
                id=id,
                title=title,
                description=description
            )
        )
        return MessageToDict(response)

    def delete_todo(self, todo_id):
        response = self.stub.DeleteTodo(
            todo_pb2.DeleteTodoRequest(id=todo_id)
        )
        return {"message": "Todo deleted successfully"}