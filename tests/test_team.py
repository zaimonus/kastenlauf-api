from beanie import PydanticObjectId
from httpx import AsyncClient
import pytest

from app.models.team import TeamDocument


@pytest.mark.anyio
async def test_get_team(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    response = await client.get(f"/teams/{create_team.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_team_change_name(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    # TODO add request content
    response = await client.patch(f"/teams/{create_team.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_team_add_members(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    # TODO add request content
    response = await client.patch(f"/teams/{create_team.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.xfail
@pytest.mark.anyio
async def test_patch_team_remove_members(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    # TODO add request content
    response = await client.patch(f"/teams/{create_team.id}")
    assert response.status_code == 200
    # TODO assert response json


@pytest.mark.anyio
async def test_delete_team(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    response = await client.delete(f"/teams/{create_team.id}")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_nonexisting_team(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/teams/{id}")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_patch_nonexisting_team(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/teams/{id}")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_delete_nonexisting_team(client: AsyncClient) -> None:
    id = PydanticObjectId()
    response = await client.get(f"/teams/{id}")
    assert response.status_code == 404
