from fastapi import FastAPI, Response
from time import perf_counter
from product import search_products, get_product
from cache.pubsub import publish_invalidation, start_pubsub_listener

app = FastAPI(title="Multi-Layer Cache E-Commerce API")

@app.on_event("startup")
async def startup():
    start_pubsub_listener()
    # Warm popular categories
    await search_products("men")
    await search_products("accessory")

@app.get("/search")
async def search(category: str, response: Response):
    t0 = perf_counter()
    data, source, status, backend_start = await search_products(category)

    backend_time = (perf_counter() - backend_start) * 1000
    total_time = (perf_counter() - t0) * 1000

    # CDN-aware headers
    response.headers["Cache-Control"] = "public, max-age=60, s-maxage=300"
    response.headers["X-Cache-Source"] = source
    response.headers["X-Cache-Status"] = status

    return {
        "data": data,
        "cache_metadata": {
            "cache_source": source,
            "cache_status": status,
            "backend_time_ms": round(backend_time, 2),
            "total_time_ms": round(total_time, 2)
        }
    }

@app.get("/product/{slug}")
async def product(slug: str, response: Response):
    t0 = perf_counter()
    data, source, status, backend_start = await get_product(slug)

    backend_time = (perf_counter() - backend_start) * 1000
    total_time = (perf_counter() - t0) * 1000

    response.headers["Cache-Control"] = "public, max-age=120, s-maxage=600"
    response.headers["X-Cache-Source"] = source
    response.headers["X-Cache-Status"] = status

    return {
        "data": data,
        "cache_metadata": {
            "cache_source": source,
            "cache_status": status,
            "backend_time_ms": round(backend_time, 2),
            "total_time_ms": round(total_time, 2)
        }
    }

@app.post("/invalidate")
async def invalidate(prefix: str):
    publish_invalidation(prefix)
    return {"status": "invalidated", "key_prefix": prefix}

@app.post("/warm-cache")
async def warm(category: str):
    await search_products(category)
    return {"status": "warmed", "category": category}
