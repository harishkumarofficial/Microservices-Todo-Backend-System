# Business Service (FastAPI)

## Overview

The Business Service is responsible for handling REST APIs, Redis online/offline tracking, and Kafka event publishing.

This service communicates with the Data Service using gRPC.

---

## Responsibilities

* Expose REST APIs using FastAPI
* Call Data Service via gRPC
* Publish Kafka events when a Todo is created
* Store user online/offline status in Redis
* Handle business logic

---

## Architecture Flow

```
Client → FastAPI → gRPC → Data Service → PostgreSQL
                 ↓
               Redis
                 ↓
               Kafka
```

---

## API Endpoints

| Method | Endpoint               | Description    |
| ------ | ---------------------- | -------------- |
| POST   | /todo/create           | Create todo    |
| GET    | /todos                 | Get all todos  |
| GET    | /todo/{id}             | Get todo       |
| PUT    | /todo/{id}             | Update todo    |
| DELETE | /todo/{id}             | Delete todo    |
| POST   | /heartbeat/{user_id}   | User heartbeat |
| GET    | /user/{user_id}/status | Online/offline |

---

## Redis Online/Offline Logic

Heartbeat API is called every 3 seconds.

Redis Keys:

```
user:{id}:online
user:{id}:last_seen
```

If online key expires → user offline.

---

## Kafka Producer

When a Todo is created:

* Event is published to Kafka topic `todo-events`.

Example Event:

```
{
  "event": "todo_created",
  "todo_id": 10,
  "title": "Test Todo"
}
```

---

## Run Service Locally

```
uvicorn app.main:app --reload
```

---

## Run Tests

```
pytest
```
