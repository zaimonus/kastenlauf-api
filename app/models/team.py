from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field


class TeamBase(BaseModel):
    name: str = Field(default="")
    member: str = Field(default="")


class TeamDocument(TeamBase, Document):
    pass


class TeamResponse(TeamBase):
    id: PydanticObjectId
