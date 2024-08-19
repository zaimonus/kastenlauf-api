from fastapi import APIRouter

from app.models.checkpoint import (
    CheckpointBase,
    CheckpointDocument,
    CheckpointResponse,
)


router = APIRouter()


@router.get("")
async def get() -> list[CheckpointResponse]:
    checkpoints = await CheckpointDocument.find().to_list()
    return checkpoints


@router.post("")
async def post(checkpoint: CheckpointBase) -> CheckpointResponse:
    doc = CheckpointDocument(name=checkpoint.name, guards=checkpoint.guards)
    await doc.insert()
    return doc
