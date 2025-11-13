from datetime import timedelta
from typing import Dict, Literal

from pydantic import BaseModel


class Dependency(BaseModel):
    status: Literal["healthy", "unhealthy"]
    response_time_ms: timedelta


class HealthResponse(BaseModel):
    service: str
    status: Literal["healthy", "unhealthy"]
    dependencies: Dict[str, Dependency] | None = None
