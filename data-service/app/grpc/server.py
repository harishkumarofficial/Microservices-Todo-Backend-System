import grpc
from concurrent import futures

from app.grpc.todo_grpc_service import TodoGrpcService
from app.grpc import todo_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    todo_pb2_grpc.add_TodoServiceServicer_to_server(
        TodoGrpcService(),
        server
    )

    server.add_insecure_port('[::]:50051')
    server.start()

    print("gRPC server running on port 50051...")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()