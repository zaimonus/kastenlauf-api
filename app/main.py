from contextlib import asynccontextmanager
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.checkpoint import CheckpointDocument
from app.models.event import EventDocument
from app.models.team import TeamDocument
from app.routers import event, events, team, teams, checkpoint, checkpoints


# TODO add settings
# https://fastapi.tiangolo.com/advanced/settings/

# TODO make connection depend on env variables
@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient("mongodb://root:example@localhost:27017")
    models = [EventDocument, TeamDocument, CheckpointDocument]
    await init_beanie(database=client.db_name, document_models=models)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(event.router, prefix="/events", tags=["events"])
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(team.router, prefix="/teams", tags=["teams"])
app.include_router(teams.router, prefix="/teams", tags=["teams"])
app.include_router(
    checkpoint.router, prefix="/checkpoints", tags=["checkpoints"]
)
app.include_router(
    checkpoints.router, prefix="/checkpoints", tags=["checkpoints"]
)
