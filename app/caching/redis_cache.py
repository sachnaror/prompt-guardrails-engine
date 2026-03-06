import redis
import json
from app.config.settings import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)


def get_cached_response(key: str):
    """
    Retrieve cached response if it exists.
    """
    cached = redis_client.get(key)

    if cached:
        return json.loads(cached)

    return None


def set_cached_response(key: str, value: dict, ttl: int = 3600):
    """
    Store response in cache with expiration.
    """

    redis_client.set(
        key,
        json.dumps(value),
        ex=ttl
    )
