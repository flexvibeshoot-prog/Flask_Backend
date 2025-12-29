# redis_client.py
import redis

redis_client = redis.Redis(
    host="localhost",   # or render redis host
    port=6379,
    decode_responses=True
)
