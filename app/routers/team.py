from beanie import PydanticObjectId
from fastapi import APIRouter

from app.models.team import TeamBase, TeamResponse

router = APIRouter()


@router.get("/{id}")
async def get(id: PydanticObjectId) -> TeamResponse:
    # TODO implement
    pass


@router.patch("/{id}")
async def update(id: PydanticObjectId, team: TeamBase) -> TeamResponse:
    # TODO implement
    pass


@router.delete("/{id}")
async def delete(id: PydanticObjectId) -> TeamResponse:
    # TODO implement
    pass
