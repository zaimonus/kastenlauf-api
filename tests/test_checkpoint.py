from beanie import PydanticObjectId
from httpx import AsyncClient
import pytest

from app.models.checkpoint import CheckpointDocument


@pytest.mark.anyio
async def test_get_checkpoint(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    response = await client.get(f"/checkpoints/{create_checkpoint.id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_checkpoint.id),
        "name": create_checkpoint.name,
        "guards": create_checkpoint.guards,
    }


@pytest.mark.anyio
async def test_patch_checkpoint_change_name(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    new_name = "NewTestName"
    data = {"name": new_name}
    response = await client.patch(
        f"/checkpoints/{create_checkpoint.id}", json=data
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_checkpoint.id),
        "name": new_name,
        "guards": create_checkpoint.guards,
    }


@pytest.mark.anyio
async def test_patch_checkpoint_change_guards(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    new_guards = "Guard2, Guard4"
    data = {"guards": new_guards}
    response = await client.patch(
        f"/checkpoints/{create_checkpoint.id}", json=data
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_checkpoint.id),
        "name": create_checkpoint.name,
        "guards": new_guards,
    }


@pytest.mark.anyio
async def test_delete_checkpoint(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    response = await client.delete(f"/checkpoints/{create_checkpoint.id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_checkpoint.id),
        "name": create_checkpoint.name,
        "guards": create_checkpoint.guards,
    }


@pytest.mark.anyio
async def test_get_nonexisting_checkpoint(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/checkpoints/{id}")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_patch_nonexisting_checkpoint(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/checkpoints/{id}")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_delete_nonexisting_checkpoint(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/checkpoints/{id}")
    assert response.status_code == 404
