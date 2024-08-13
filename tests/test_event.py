from beanie import PydanticObjectId
from httpx import AsyncClient
import pytest

from app.models.checkpoint import CheckpointDocument
from app.models.event import Arrival, EventDocument
from app.models.team import TeamDocument


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_event(
    client: AsyncClient, create_event: EventDocument
) -> None:
    response = await client.get(f"/events/{create_event.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_event_change_name(
    client: AsyncClient, create_event: EventDocument
) -> None:
    # TODO add request content
    response = await client.patch(f"/events/{create_event.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_event_add_arrivals(
    client: AsyncClient,
    create_event: EventDocument,
    create_checkpoint: CheckpointDocument,
    create_team: TeamDocument,
    create_arrival: Arrival,
) -> None:
    # TODO add request content
    response = await client.patch(f"/events/{create_event.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_event_remove_arrivals(
    client: AsyncClient,
    create_event: EventDocument,
    create_checkpoint: CheckpointDocument,
    create_team: TeamDocument,
    create_arrival: Arrival,
) -> None:
    # TODO add request content
    response = await client.patch(f"/events/{create_event.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_delete_event(
    client: AsyncClient, create_event: EventDocument
) -> None:
    # TODO add request content
    response = await client.delete(f"/events/{create_event.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_nonexisting_event(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/events/{id}")
    assert response.status_code == 404


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_nonexisting_event(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/events/{id}")
    assert response.status_code == 404


@pytest.mark.xfail
@pytest.mark.anyio
async def test_delete_nonexisting_event(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/events/{id}")
    assert response.status_code == 404
