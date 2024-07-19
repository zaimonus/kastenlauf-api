from httpx import AsyncClient
import pytest


@pytest.mark.anyio
async def test_get_checkpoints(client: AsyncClient) -> None:
    response = await client.get("/checkpoints")
    assert response.status_code == 200
    assert response.json() == "[]"
