from httpx import AsyncClient
import pytest

from app.models.team import TeamDocument


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_empty_teams(client: AsyncClient) -> None:
    response = await client.get("/teams")
    assert response.status_code == 200
    assert response.json() == "[]"


@pytest.mark.xfail
@pytest.mark.anyio
async def test_get_one_team(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    response = await client.get("/teams")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_post_new_team(client: AsyncClient) -> None:
    # TODO create request content
    response = await client.get("/teams")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_post_existing_teams(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    # TODO create request content
    response = await client.get("/teams")
    assert response.status_code == 409
    # TODO assert response json
