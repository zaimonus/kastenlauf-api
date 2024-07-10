from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field


class TeamBase(BaseModel):
    name: str
    member: list[str] = Field(default_factory=list)


class TeamDocument(TeamBase, Document):
    pass


class TeamResponse(TeamBase):
    id: PydanticObjectId
