import os
from time import time

import redis
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from models import HealthResponse
from redis.exceptions import ConnectionError

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

app = FastAPI()


@app.get("/health", response_model=HealthResponse)
def health_check():
    start = time()
    try:
        # Check redis is running
        if redis_client.ping():
            # Redis is working fine
            dt = time() - start
            return {
                "service": "user-service",
                "status": "healthy",
                "dependencies": {
                    "redis": "healthy",
                    "response_time_ms": dt
                }
            }
        else:
            # Manually raise exception to go to except block
            raise ConnectionError
    except ConnectionError:
        dt = time() - start
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "service": "user-service",
                "status": "unhealthy",
                "dependencies": {
                    "redis": "unhealthy",
                    "response_time_ms": dt
                }
            }
        )
