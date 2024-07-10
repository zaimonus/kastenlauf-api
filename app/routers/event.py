from beanie import PydanticObjectId
from fastapi import APIRouter

from app.models.event import EventBase, EventResponse

router = APIRouter()


@router.get("/{id}")
async def get(id: PydanticObjectId) -> EventResponse:
    # TODO implement
    pass


@router.patch("/{id}")
async def update(id: PydanticObjectId, event: EventBase) -> EventResponse:
    # TODO implement
    pass


@router.delete("/{id}")
async def delete(id: PydanticObjectId) -> EventResponse:
    # TODO implement
    pass
