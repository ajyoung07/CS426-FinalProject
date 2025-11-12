from datetime import datetime
from typing import Dict, Literal

from pydantic import BaseModel, EmailStr


class Dependency(BaseModel):
    status: Literal["healthy", "unhealthy"]
    response_time_ms: datetime


class HealthResponse(BaseModel):
    service: str
    status: Literal["healthy", "unhealthy"]
    dependencies: Dict[str, Dependency] | None = None


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    created_at: str
