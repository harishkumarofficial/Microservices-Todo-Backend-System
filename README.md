# Todo Microservices Backend System

## Project Overview

This project is a microservices-based Todo backend system built using FastAPI, gRPC, PostgreSQL, Redis, Kafka, and Docker.

The system is divided into two main services:

1. Business Service (FastAPI REST APIs)
2. Data Service (gRPC + PostgreSQL)

Redis is used for online/offline user tracking.
Kafka is used for event streaming when a Todo is created.
All services run using Docker Compose.

---

## Architecture

```
Client
   |
Business Service (FastAPI)
   |      |       |
   |      |       |
 Redis   Kafka    gRPC
                   |
              Data Service
                   |
               PostgreSQL
```

---

## Tech Stack

| Layer             | Technology |
| ----------------- | ---------- |
| API               | FastAPI    |
| RPC Communication | gRPC       |
| Database          | PostgreSQL |
| Cache             | Redis      |
| Event Streaming   | Kafka      |
| Containerization  | Docker     |
| ORM               | SQLAlchemy |
| Migration         | Alembic    |
| Testing           | Pytest     |

---

## Services

### Business Service

* FastAPI REST APIs
* Calls Data Service via gRPC
* Publishes Kafka events
* Stores user online/offline in Redis

### Data Service

* gRPC server
* Handles database operations
* Uses PostgreSQL
* SQLAlchemy ORM
* Alembic migrations

---

## System Flow

1. Client calls REST API
2. Business Service handles request
3. Business Service calls Data Service via gRPC
4. Data Service stores data in PostgreSQL
5. Business Service publishes Kafka event
6. Redis tracks user online/offline

---

## How to Run the Project

```bash
docker-compose up --build
```

After running:

```
http://localhost:8000/docs
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

## Redis Online/Offline Flow

Client sends heartbeat every 3 seconds.

Redis stores:

```
user:{id}:online (expires in 6 seconds)
user:{id}:last_seen (timestamp)
```

If online key expires → user is offline.

---

## Kafka Event Flow

When a todo is created:
Business Service publishes event to Kafka topic **todo-events**.

Example event:

```
{
  "event": "todo_created",
  "todo_id": 1,
  "title": "Learn Kafka"
}
```

---

## gRPC Communication

Business Service communicates with Data Service using gRPC for database operations.

This improves performance compared to REST between services.

---

## Unit Testing

Unit tests are written using pytest for:

* Create Todo
* Get Todos
* Update Todo
* Delete Todo
* Heartbeat API
* User Status API

Run tests:

```bash
pytest
```

---

## Docker Services

Docker Compose runs the following services:

* PostgreSQL
* Redis
* Kafka
* Zookeeper
* Data Service
* Business Service

Run:

```bash
docker-compose up --build
```

---

## Future Improvements

* Authentication
* API Gateway
* Kafka Consumer Service
* Logging & Monitoring
* Rate Limiting



