from fastapi import APIRouter

from app.models.checkpoint import CheckpointBase, CheckpointResponse


router = APIRouter()


@router.get("")
async def get() -> list[CheckpointResponse]:
    # TODO implement
    pass


@router.post("")
async def post(checkpoint: CheckpointBase) -> CheckpointResponse:
    # TODO implement
    pass
