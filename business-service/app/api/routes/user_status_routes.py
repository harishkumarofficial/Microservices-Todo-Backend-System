from fastapi import APIRouter
from app.redis.redis_client import RedisClient

redis_client = RedisClient()
router = APIRouter()


@router.post("/heartbeat/{user_id}")
def heartbeat(user_id: int):
    redis_client.heartbeat(user_id)
    return {"message": "heartbeat received"}

@router.get("/user/{user_id}/status")
def user_status(user_id: int):
    return redis_client.get_user_status(user_id)