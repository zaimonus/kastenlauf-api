from fastapi import APIRouter

from app.models.team import TeamBase, TeamDocument, TeamResponse


router = APIRouter()


@router.get("")
async def get() -> list[TeamResponse]:
    teams = await TeamDocument.find().to_list()
    return teams


@router.post("")
async def post(team: TeamBase) -> TeamResponse:
    doc = TeamDocument(name=team.name, member=team.member)
    await doc.insert()
    return doc
