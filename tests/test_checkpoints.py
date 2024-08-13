from httpx import AsyncClient
import pytest

from app.models.checkpoint import CheckpointDocument


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_empty_checkpoints(client: AsyncClient) -> None:
    response = await client.get("/checkpoints")
    assert response.status_code == 200
    assert response.json() == "[]"


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_one_checkpoint(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    response = await client.get("/checkpoints")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_post_new_checkpoint(client: AsyncClient) -> None:
    # TODO create request content
    response = await client.get("/checkpoints")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_post_existing_checkpoints(
    client: AsyncClient, create_checkpoint: CheckpointDocument
) -> None:
    # TODO create request content
    response = await client.get("/checkpoints")
    assert response.status_code == 409
    # TODO assert response json
