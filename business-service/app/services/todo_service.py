from app.grpc_clients.todo_client import TodoGrpcClient
from app.kafka.producer import KafkaProducerService

class TodoService:

    def __init__(self):
        self.client = TodoGrpcClient()
        self.kafka = KafkaProducerService()

    def create_todo(self, title: str, description: str):
        todo = self.client.create_todo(title, description)

        # publish kafka event
        self.kafka.send_todo_created(todo)
        
        # return self.client.create_todo(title, description)
        return todo

    def get_todos(self):
        return self.client.get_todos()
    
    def get_todo(self, todo_id):
        return self.client.get_todo(todo_id)

    def update_todo(self, todo_id, title, description):
        return self.client.update_todo(todo_id, title, description)

    def delete_todo(self, todo_id):
        return self.client.delete_todo(todo_id)