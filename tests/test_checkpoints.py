from unittest.mock import ANY
from beanie import PydanticObjectId
from httpx import AsyncClient
import pytest

from app.models.checkpoint import CheckpointDocument


@pytest.mark.anyio
async def test_get_empty_checkpoints(client: AsyncClient) -> None:
    response = await client.get("/checkpoints")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.anyio
async def test_get_one_checkpoint(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    response = await client.get("/checkpoints")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": str(create_checkpoint.id),
            "name": create_checkpoint.name,
            "guards": create_checkpoint.guards,
        }
    ]


@pytest.mark.anyio
async def test_post_new_checkpoint(
    client: AsyncClient, cleanup_checkpoints: None
) -> None:
    name = "NewCheckpoint"
    guards = "Guard1, Guard2"
    data = {"name": name, "guards": guards}
    response = await client.post("/checkpoints", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "id": ANY,
        "name": name,
        "guards": guards,
    }
    assert PydanticObjectId.is_valid(response.json()["id"])
