from beanie import PydanticObjectId
from httpx import AsyncClient
import pytest

from app.models.team import TeamDocument


@pytest.mark.anyio
async def test_get_empty_teams(client: AsyncClient) -> None:
    response = await client.get("/teams")

    assert response.status_code == 200
    json = response.json()
    assert isinstance(json, list)
    assert len(json) == 0


@pytest.mark.anyio
async def test_get_one_team(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    response = await client.get("/teams")

    assert response.status_code == 200
    json = response.json()
    assert isinstance(json, list)
    assert len(json) == 1
    obj = json[0]
    assert obj["id"] == str(create_team.id)
    assert obj["name"] == create_team.name
    assert obj["member"] == create_team.member


@pytest.mark.anyio
async def test_post_new_team(client: AsyncClient, cleanup_teams: None) -> None:
    name = "NewTeam"
    member = "Member1, Member2, Member3"
    data = {"name": name, "member": member}

    response = await client.post("/teams", json=data)

    assert response.status_code == 200
    obj = response.json()
    assert obj["name"] == name
    assert obj["member"] == member
    assert PydanticObjectId.is_valid(obj["id"])
