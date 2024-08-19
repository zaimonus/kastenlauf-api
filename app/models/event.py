from datetime import datetime
from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field


class Arrival(BaseModel):
    team: PydanticObjectId
    checkpoint: PydanticObjectId
    at: datetime = Field(default_factory=datetime.now)


class EventBase(BaseModel):
    name: str = Field(default="")
    arrivals: list[Arrival] = Field(default_factory=list)


class EventDocument(EventBase, Document):
    pass


class EventResponse(EventBase):
    id: PydanticObjectId
