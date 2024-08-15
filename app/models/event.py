from datetime import datetime
from beanie import Document, Link, PydanticObjectId
from pydantic import BaseModel, Field

from app.models.checkpoint import CheckpointDocument
from app.models.team import TeamDocument


class Arrival(BaseModel):
    team: Link[TeamDocument]
    checkpoint: Link[CheckpointDocument]
    at: datetime = Field(default_factory=datetime.now)


class EventBase(BaseModel):
    name: str = Field(default="")
    arrivals: list[Arrival] = Field(default_factory=list)


class EventDocument(EventBase, Document):
    pass


class EventResponse(EventBase):
    id: PydanticObjectId
