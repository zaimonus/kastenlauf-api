from collections.abc import AsyncGenerator
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
import subprocess
import pytest

from dotenv import load_dotenv

from app.main import app
from app.models.checkpoint import CheckpointDocument
from app.models.event import Arrival, EventDocument
from app.models.team import TeamDocument


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
async def test_env() -> AsyncGenerator[None]:
    load_dotenv(".dev.env", override=True)
    subprocess.call(
        "docker compose -f docker-compose.dev.yaml up -d", shell=True
    )
    yield
    subprocess.call(
        "docker compose -f docker-compose.dev.yaml down", shell=True
    )


@pytest.fixture
async def lifespan_app() -> AsyncGenerator[FastAPI]:
    async with LifespanManager(app) as m:
        yield m.app


@pytest.fixture
async def client(lifespan_app: FastAPI) -> AsyncGenerator[AsyncClient]:
    transport = ASGITransport(app=lifespan_app)
    async with AsyncClient(transport=transport, base_url="http://test") as a:
        yield a


@pytest.fixture
async def create_team() -> AsyncGenerator[TeamDocument]:
    team = TeamDocument(name="TestTeam", members="Mem1, Mem2")
    await team.save()
    yield team
    await team.delete()


@pytest.fixture
async def create_checkpoint() -> AsyncGenerator[CheckpointDocument]:
    checkpoint = CheckpointDocument(
        name="TestCheckpoint", guards="G1, G2"
    )
    await checkpoint.save()
    yield checkpoint
    await checkpoint.delete()


@pytest.fixture
async def create_event() -> AsyncGenerator[EventDocument]:
    event = EventDocument(name="TestEvent")
    await event.save()
    yield event
    await event.delete()


@pytest.fixture
async def create_arrival(
    create_event: EventDocument,
    create_team: TeamDocument,
    create_checkpoint: CheckpointDocument,
) -> AsyncGenerator[Arrival]:
    arrival = Arrival(team=create_team.id, checkpoint=create_checkpoint.id)
    event = create_event
    event.arrivals.append(arrival)
    await event.save()
    yield arrival
    await event.delete()
