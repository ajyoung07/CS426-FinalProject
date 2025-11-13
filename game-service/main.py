import os
from time import time

import httpx
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

USER_HOST = os.getenv("USER_HOST", "user-service")
USER_PORT = os.getenv("USER_PORT", 8001)
USER_URL = f'http://{USER_HOST}:{USER_PORT}'

app = FastAPI()


@app.get("/health", response_model=HealthResponse)
def health_check():

    dependencies = {}
    isHealthy = True
    try:
        # Check redis is running
        start = time()
        pong = redis_client.ping()
        if pong:
            # Redis is working fine
            redis_time = time()
            dependencies["redis"] = {"status": "healthy",
                                     "response_time_ms": redis_time - start
                                     }
        else:
            # Redis not working
            raise ConnectionError
    except ConnectionError:
        redis_time = time()
        isHealthy = False
        dependencies["redis"] = {"status": "unhealthy",
                                 "response_time_ms": redis_time - start
                                 }
    # Check users is running
    try:
        start = time()
        resp = httpx.get(USER_URL + "/health")
        resp.raise_for_status()  # Returns HTTPError on status codes 4xx and 5xx
        user_time = time()
        dependencies["user-service"] = {
            "status": "healthy",
            "response_time_ms": user_time - start
        }

    except httpx.HTTPStatusError:
        # Redis not working
        user_time = time()
        isHealthy = False
        dependencies["user-service"] = {
            "status": "unhealthy",
            "response_time_ms": user_time - start
        }

    return {
        "service": "chat-service",
        "status": "healthy" if isHealthy else "unhealthy",
        "dependencies": dependencies
    }
