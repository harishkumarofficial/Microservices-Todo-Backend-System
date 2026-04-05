# Data Service (gRPC + PostgreSQL)

## Overview

The Data Service is responsible for handling database operations using PostgreSQL.

This service exposes gRPC endpoints which are consumed by the Business Service.

---

## Responsibilities

* gRPC server
* Database CRUD operations
* PostgreSQL connection
* SQLAlchemy ORM
* Alembic migrations

---

## Architecture Flow

```
Business Service → gRPC → Data Service → PostgreSQL
```

---

## Database

PostgreSQL is used as the primary database.

Tables:

* todos

Fields:

* id
* title
* description
* is_completed
* created_at
* updated_at
* is_deleted
* deleted_at

Soft delete is implemented using `is_deleted`.

---

## Alembic Migrations

Migrations are handled using Alembic.

Commands:

```
alembic revision --autogenerate -m "message"
alembic upgrade head
```

---

## gRPC Methods

| Method     | Description      |
| ---------- | ---------------- |
| CreateTodo | Create new todo  |
| GetTodos   | Get all todos    |
| GetTodo    | Get single todo  |
| UpdateTodo | Update todo      |
| DeleteTodo | Soft delete todo |

---

## Run gRPC Server

```
python -m app.grpc.server
```

---

## Database Connection

The service reads DATABASE_URL from environment variables.

Example:

```
postgresql+psycopg2://postgres:postgres@postgres:5432/todo_db
```
