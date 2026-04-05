import redis
import time


class RedisClient:

    def __init__(self):
        self.client = redis.Redis(
            host="redis",
            port=6379,
            decode_responses=True
        )

    def heartbeat(self, user_id: int):
        key = f"user:{user_id}"
        # we have used to save the hash set
        self.client.hset(
            key,
            mapping={
                "online": 1,
                "last_seen": int(time.time())
            }
        )

        # expire after 6 seconds
        self.client.expire(key, 20)

    def get_user_status(self, user_id: int):
        key = f"user:{user_id}"

        data = self.client.hgetall(key) # using HGETALL to retrieving the all the fields

        if not data:
            return {
                "status": "offline",
                "last_seen": None
            }

        return {
            "status": "online",
            "last_seen": data.get("last_seen")
        }