from collections.abc import AsyncGenerator
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
import pytest

from dotenv import load_dotenv

from app.main import app


@pytest.fixture(scope="module", autouse=True)
async def test_env() -> None:
    load_dotenv(".dev.env", override=True)


@pytest.fixture()
async def lifespan_app() -> AsyncGenerator[FastAPI]:
    async with LifespanManager(app) as m:
        yield m.app


@pytest.fixture()
async def client(lifespan_app: FastAPI) -> AsyncGenerator[AsyncClient]:
    transport = ASGITransport(app=lifespan_app)
    async with AsyncClient(transport=transport, base_url="http://test") as a:
        yield a
