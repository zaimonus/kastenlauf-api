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
    assert response.json() == {
        "id": str(create_team.id),
        "name": create_team.name,
        "member": create_team.member,
    }


@pytest.mark.anyio
async def test_patch_team_change_name(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    new_name = "NewTestName"
    data = {"name": new_name}
    response = await client.patch(f"/teams/{create_team.id}", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_team.id),
        "name": new_name,
        "member": create_team.member,
    }


@pytest.mark.anyio
async def test_patch_team_change_members(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    new_members = "NewMember1, NewMember2"
    data = {"member": new_members}
    response = await client.patch(f"/teams/{create_team.id}", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_team.id),
        "name": create_team.name,
        "member": new_members,
    }


@pytest.mark.anyio
async def test_delete_team(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    response = await client.delete(f"/teams/{create_team.id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": str(create_team.id),
        "name": create_team.name,
        "member": create_team.member,
    }


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
