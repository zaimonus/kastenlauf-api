from fastapi import APIRouter

from app.models.event import EventBase, EventResponse


router = APIRouter()


@router.get("")
async def get() -> list[EventResponse]:
    # TODO implement
    pass


@router.post("")
async def post(event: EventBase) -> EventResponse:
    # TODO implement
    pass
