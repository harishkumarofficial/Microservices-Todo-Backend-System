import grpc
from app.grpc import todo_pb2
from app.grpc import todo_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051') # Make sure to call the service name when running via the docker
    stub = todo_pb2_grpc.TodoServiceStub(channel)

    response = stub.CreateTodo(
        todo_pb2.CreateTodoRequest(
            title="Learn Microservices",
            description="gRPC + FastAPI + Kafka"
        )
    )

    print("CreateTodo Response:")
    print(response)

    todos = stub.GetTodos(todo_pb2.Empty())
    print("GetTodos Response:")
    print(todos)


if __name__ == "__main__":
    run()