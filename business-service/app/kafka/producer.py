from kafka import KafkaProducer
import json
import time


class KafkaProducerService:

    def __init__(self):
        self.producer = None
        self.connect()

    def connect(self):
        while self.producer is None:
            try:
                print("Connecting to Kafka...")
                self.producer = KafkaProducer(
                    bootstrap_servers="kafka:9092",
                    value_serializer=lambda v: json.dumps(v).encode("utf-8")
                )
                print("Connected to Kafka!")
            except Exception as e:
                print("Kafka not ready, retrying in 5 seconds...")
                time.sleep(5)

    def send_todo_created(self, todo):
        event = {
            "event": "todo_created",
            "todo_id": todo.get("id", None),
            "title": todo.get("title", None)
        }

        self.producer.send("todo-events", event)
        self.producer.flush()