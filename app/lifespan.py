from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from urllib.parse import quote_plus
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from fastapi import FastAPI

from app.models.checkpoint import CheckpointDocument
from app.models.event import EventDocument
from app.models.team import TeamDocument
from app.settings import Settings


def get_database_uri(settings: Settings) -> str:
    return "mongodb://{}:{}@{}:{}".format(
        quote_plus(settings.USERNAME),
        quote_plus(settings.PASSWORD),
        settings.HOST,
        settings.PORT
    )


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, Any]:
    settings = Settings()
    uri = get_database_uri(settings)
    client = AsyncIOMotorClient(uri)
    models = [EventDocument, TeamDocument, CheckpointDocument]

    print("DATABASE URI:", uri)

    try:
        await init_beanie(database=client.db_name, document_models=models)
        yield
    finally:
        pass
