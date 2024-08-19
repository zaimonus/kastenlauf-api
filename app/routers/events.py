from fastapi import APIRouter

from app.models.event import EventBase, EventDocument, EventResponse


router = APIRouter()


@router.get("")
async def get() -> list[EventResponse]:
    teams = await EventDocument.find().to_list()
    return teams


@router.post("")
async def post(event: EventBase) -> EventResponse:
    doc = EventDocument(name=event.name, arrivals=event.arrivals)
    await doc.insert()
    return doc
