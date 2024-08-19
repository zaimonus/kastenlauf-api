from beanie import PydanticObjectId
from beanie.operators import Set
from fastapi import APIRouter, HTTPException

from app.models.checkpoint import (
    CheckpointBase,
    CheckpointDocument,
    CheckpointResponse,
)

router = APIRouter()


@router.get("/{id}")
async def get(id: PydanticObjectId) -> CheckpointResponse:
    checkpoint = await CheckpointDocument.get(id)
    if checkpoint is None:
        raise HTTPException(status_code=404, detail="Checkpoint not found")
    return checkpoint


@router.patch("/{id}")
async def update(
    id: PydanticObjectId, checkpoint: CheckpointBase
) -> CheckpointResponse:
    doc = await CheckpointDocument.get(id)
    if doc is None:
        raise HTTPException(status_code=404, detail="Checkpoint not found")
    await doc.update(Set(checkpoint.model_dump(exclude_unset=True)))
    return doc


@router.delete("/{id}")
async def delete(id: PydanticObjectId) -> CheckpointResponse:
    checkpoint = await CheckpointDocument.get(id)
    if checkpoint is None:
        raise HTTPException(status_code=404, detail="Checkpoint not found")
    await checkpoint.delete()
    return checkpoint
