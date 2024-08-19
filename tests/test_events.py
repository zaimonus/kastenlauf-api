from unittest.mock import ANY
from beanie import PydanticObjectId
from httpx import AsyncClient
import pytest

from app.models.event import EventDocument


@pytest.mark.anyio
async def test_get_empty_events(client: AsyncClient) -> None:
    response = await client.get("/events")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.anyio
async def test_get_one_event(
    client: AsyncClient, create_event: EventDocument
) -> None:
    response = await client.get("/events")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": str(create_event.id),
            "name": create_event.name,
            "arrivals": [],
        }
    ]


@pytest.mark.anyio
async def test_post_new_event(
    client: AsyncClient, cleanup_events: None
) -> None:
    name = "NewEvent"
    arrivals = []
    data = {"name": name, "arrivals": arrivals}
    response = await client.post("/events", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "id": ANY,
        "name": name,
        "arrivals": arrivals,
    }
    assert PydanticObjectId.is_valid(response.json()["id"])
