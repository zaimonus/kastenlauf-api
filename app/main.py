from fastapi import FastAPI

from app.lifespan import lifespan
from app.routers import event, events, team, teams, checkpoint, checkpoints


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
