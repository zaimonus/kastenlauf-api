from httpx import AsyncClient
import pytest

from app.models.event import EventDocument


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_empty_events(client: AsyncClient) -> None:
    response = await client.get("/events")
    assert response.status_code == 200
    assert response.json() == "[]"


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_one_event(
    client: AsyncClient, create_event: EventDocument
) -> None:
    response = await client.get("/events")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_post_new_event(client: AsyncClient) -> None:
    # TODO create request content
    response = await client.get("/events")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_post_existing_events(
    client: AsyncClient, create_event: EventDocument
) -> None:
    # TODO create request content
    response = await client.get("/events")
    assert response.status_code == 409
    # TODO assert response json
