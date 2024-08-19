from unittest.mock import ANY
from beanie import PydanticObjectId
from httpx import AsyncClient
import pytest

from app.models.checkpoint import CheckpointDocument
from app.models.event import EventDocument
from app.models.team import TeamDocument


@pytest.mark.anyio
async def test_get_event(
    client: AsyncClient, create_event: EventDocument
) -> None:
    response = await client.get(f"/events/{create_event.id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_event.id),
        "name": create_event.name,
        "arrivals": create_event.arrivals,
    }


@pytest.mark.anyio
async def test_patch_event_change_name(
    client: AsyncClient, create_event: EventDocument
) -> None:
    new_name = "NewTestName"
    data = {"name": new_name}
    response = await client.patch(f"/events/{create_event.id}", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_event.id),
        "name": new_name,
        "arrivals": create_event.arrivals,
    }


@pytest.mark.anyio
async def test_patch_event_change_arrivals(
    client: AsyncClient,
    create_event: EventDocument,
    create_checkpoint: CheckpointDocument,
    create_team: TeamDocument,
) -> None:
    new_arrival = {
        "team": str(create_team.id),
        "checkpoint": str(create_checkpoint.id),
    }
    data = {"arrivals": [new_arrival]}
    response = await client.patch(f"/events/{create_event.id}", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_event.id),
        "name": create_event.name,
        "arrivals": [
            {
                "team": str(create_team.id),
                "checkpoint": str(create_checkpoint.id),
                "at": ANY,
            }
        ],
    }


@pytest.mark.anyio
async def test_patch_event_delete_arrivals(
    client: AsyncClient, create_event: EventDocument
) -> None:
    data = {"arrivals": []}
    response = await client.patch(f"/events/{create_event.id}", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_event.id),
        "name": create_event.name,
        "arrivals": [],
    }


@pytest.mark.anyio
async def test_delete_event(
    client: AsyncClient, create_event: EventDocument
) -> None:
    response = await client.delete(f"/events/{create_event.id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_event.id),
        "name": create_event.name,
        "arrivals": create_event.arrivals,
    }


@pytest.mark.anyio
async def test_get_nonexisting_event(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/events/{id}")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_patch_nonexisting_event(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/events/{id}")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_delete_nonexisting_event(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/events/{id}")
    assert response.status_code == 404
