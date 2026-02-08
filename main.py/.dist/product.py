import time
from motor.motor_asyncio import AsyncIOMotorClient
from cache.redis_cache import get_redis, set_redis
from cache.lru_cache import LRUCache  

mongo = AsyncIOMotorClient("mongodb://localhost:27017")
db = mongo["e-commerce"]
collection = db["product_details"]

# Application-level cache (LRU)
app_cache = LRUCache(capacity=500)

async def search_products(category: str):
    start = time.perf_counter()
    key = f"search:{category}"

    # 1️⃣ Application-level LRU cache
    data = app_cache.get(key)
    if data is not None:
        return data, "application-lru", "HIT", start

    # 2️⃣ Redis distributed cache
    data = get_redis(key)
    if data is not None:
        app_cache.put(key, data)
        return data, "redis", "HIT", start

    # 3️⃣ MongoDB (source of truth)
    cursor = collection.find({"category": category, "isActive": True})
    data = [doc async for doc in cursor]

    set_redis(key, data)
    app_cache.put(key, data)

    return data, "database", "MISS", start


async def get_product(slug: str):
    start = time.perf_counter()
    key = f"product:{slug}"

    # 1️⃣ Application-level LRU cache
    data = app_cache.get(key)
    if data is not None:
        return data, "application-lru", "HIT", start

    # 2️⃣ Redis distributed cache
    data = get_redis(key)
    if data is not None:
        app_cache.put(key, data)
        return data, "redis", "HIT", start

    # 3️⃣ MongoDB
    data = await collection.find_one({"slug": slug})
    if data is not None:
        set_redis(key, data)
        app_cache.put(key, data)

    return data, "database", "MISS", start
