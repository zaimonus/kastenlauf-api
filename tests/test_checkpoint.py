from beanie import PydanticObjectId
from httpx import AsyncClient
import pytest

from app.models.checkpoint import CheckpointDocument


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_checkpoint(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    response = await client.get(f"/checkpoints/{create_checkpoint.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_checkpoint_change_name(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    # TODO add request content
    response = await client.patch(f"/checkpoints/{create_checkpoint.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_checkpoint_add_guards(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    # TODO add request content
    response = await client.patch(f"/checkpoints/{create_checkpoint.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_checkpoint_remove_guards(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    # TODO add request content
    response = await client.patch(f"/checkpoints/{create_checkpoint.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_delete_checkpoint(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    # TODO add request content
    response = await client.delete(f"/checkpoints/{create_checkpoint.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_nonexisting_checkpoint(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/checkpoints/{id}")
    assert response.status_code == 404


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_nonexisting_checkpoint(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/checkpoints/{id}")
    assert response.status_code == 404


@pytest.mark.xfail
@pytest.mark.anyio
async def test_delete_nonexisting_checkpoint(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/checkpoints/{id}")
    assert response.status_code == 404
