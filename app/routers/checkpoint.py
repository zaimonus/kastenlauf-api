from beanie import PydanticObjectId
from fastapi import APIRouter

from app.models.checkpoint import CheckpointBase, CheckpointResponse

router = APIRouter()


@router.get("/{id}")
async def get(id: PydanticObjectId) -> CheckpointResponse:
    # TODO implement
    pass


@router.patch("/{id}")
async def update(
    id: PydanticObjectId, checkpoint: CheckpointBase
) -> CheckpointResponse:
    # TODO implement
    pass


@router.delete("/{id}")
async def delete(id: PydanticObjectId) -> CheckpointResponse:
    # TODO implement
    pass
