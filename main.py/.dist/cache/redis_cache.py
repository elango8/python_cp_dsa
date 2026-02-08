import json
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

DEFAULT_TTL = 300  # 5 minutes

def get_redis(key):
    val = redis_client.get(key)
    return json.loads(val) if val else None

def set_redis(key, value, ttl=DEFAULT_TTL):
    redis_client.setex(key, ttl, json.dumps(value))

def delete_redis(key_prefix):
    for key in redis_client.scan_iter(f"{key_prefix}*"):
        redis_client.delete(key)
