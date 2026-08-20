from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.schemas.user import UserResponse


class ProjectBase(BaseModel):
    name: str
    description: str | None = None


class ProjectCreate(ProjectBase):
    owner_id: int


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class ProjectResponse(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime
    owner: UserResponse | None = None

    model_config = ConfigDict(from_attributes=True)