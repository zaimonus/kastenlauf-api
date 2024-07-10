from fastapi import APIRouter

from app.models.team import TeamBase, TeamResponse


router = APIRouter()


@router.get("/")
async def get() -> list[TeamResponse]:
    # TODO implement
    pass


@router.post("/")
async def post(team: TeamBase) -> TeamResponse:
    # TODO implement
    pass
