from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field


class CheckpointBase(BaseModel):
    name: str = Field(default="")
    guards: str = Field(default="")


class CheckpointDocument(CheckpointBase, Document):
    pass


class CheckpointResponse(CheckpointBase):
    id: PydanticObjectId
