from beanie import PydanticObjectId
from beanie.operators import Set
from fastapi import APIRouter, HTTPException

from app.models.team import TeamBase, TeamDocument, TeamResponse

router = APIRouter()


@router.get("/{id}")
async def get(id: PydanticObjectId) -> TeamResponse:
    team = await TeamDocument.get(id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.patch("/{id}")
async def update(id: PydanticObjectId, team: TeamBase) -> TeamResponse:
    doc = await TeamDocument.get(id)
    if doc is None:
        raise HTTPException(status_code=404, detail="Team not found")
    await doc.update(Set(team.model_dump(exclude_unset=True)))
    return doc


@router.delete("/{id}")
async def delete(id: PydanticObjectId) -> TeamResponse:
    team = await TeamDocument.get(id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    await team.delete()
    return team
