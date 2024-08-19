from unittest.mock import ANY
from beanie import PydanticObjectId
from httpx import AsyncClient
import pytest

from app.models.team import TeamDocument


@pytest.mark.anyio
async def test_get_empty_teams(client: AsyncClient) -> None:
    response = await client.get("/teams")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.anyio
async def test_get_one_team(
    client: AsyncClient, create_team: TeamDocument
) -> None:
    response = await client.get("/teams")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": str(create_team.id),
            "name": create_team.name,
            "member": create_team.member,
        }
    ]


@pytest.mark.anyio
async def test_post_new_team(client: AsyncClient, cleanup_teams: None) -> None:
    name = "NewTeam"
    member = "Member1, Member2, Member3"
    data = {"name": name, "member": member}
    response = await client.post("/teams", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "id": ANY,
        "name": name,
        "member": member,
    }
    assert PydanticObjectId.is_valid(response.json()["id"])
