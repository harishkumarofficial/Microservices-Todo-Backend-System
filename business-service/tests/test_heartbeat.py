import pytest


@pytest.mark.asyncio
async def test_heartbeat(client):
    response = await client.post("/heartbeat/1")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_user_status(client):
    await client.post("/heartbeat/1")
    response = await client.get("/user/1/status")

    assert response.status_code == 200
    assert response.json()["status"] in ["online", "offline"]