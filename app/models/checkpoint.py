from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field


class CheckpointBase(BaseModel):
    name: str
    guards: list[str] = Field(default_factory=list)


class CheckpointDocument(CheckpointBase, Document):
    pass


class CheckpointResponse(CheckpointBase):
    id: PydanticObjectId
