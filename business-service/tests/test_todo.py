import pytest


@pytest.mark.asyncio
async def test_create_todo(client):
    response = await client.post(
        "/todo/create",
        json={
            "title": "Test Todo",
            "description": "Testing create"
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Test Todo"
    assert data["description"] == "Testing create"

@pytest.mark.asyncio
async def test_get_todos(client):
    response = await client.get("/todos")

    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_todo(client):
    # create first
    create = await client.post(
        "/todo/create",
        json={"title": "Old", "description": "Old desc"}
    )

    todo_id = create.json()["id"]

    # update
    update = await client.put(
        f"/todo/update",
        json={
            "id": todo_id,
            "title": "New",
            "description": "New desc",
            "is_completed": True
        }
    )

    assert update.status_code == 200
    assert update.json()["title"] == "New"

@pytest.mark.asyncio
async def test_delete_todo(client):
    create = await client.post(
        "/todo/create",
        json={"title": "Delete", "description": "Delete me"}
    )

    todo_id = create.json()["id"]

    delete = await client.delete(f"/todo/{todo_id}")

    assert delete.status_code == 200