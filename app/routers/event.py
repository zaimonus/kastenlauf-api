from beanie import PydanticObjectId
from beanie.operators import Set
from fastapi import APIRouter, HTTPException

from app.models.event import EventBase, EventDocument, EventResponse

router = APIRouter()


@router.get("/{id}")
async def get(id: PydanticObjectId) -> EventResponse:
    event = await EventDocument.get(id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.patch("/{id}")
async def update(id: PydanticObjectId, event: EventBase) -> EventResponse:
    doc = await EventDocument.get(id)
    if doc is None:
        raise HTTPException(status_code=404, detail="Event not found")
    await doc.update(Set(event.model_dump(exclude_unset=True)))
    return doc


@router.delete("/{id}")
async def delete(id: PydanticObjectId) -> EventResponse:
    event = await EventDocument.get(id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    await event.delete()
    return event
