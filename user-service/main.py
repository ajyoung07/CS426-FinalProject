from fastapi import FastAPI
from models import HealthResponse

app = FastAPI()


@app.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "service": "user-service",
        "status": "healthy"
    }
