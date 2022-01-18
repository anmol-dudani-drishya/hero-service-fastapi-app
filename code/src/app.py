from fastapi import FastAPI
import src.routers.assignment as assignment

import src.routers.hero as hero
from src.database import engine
from src.database import Base

app = FastAPI()

Base.metadata.create_all(engine)

# Routes
app.include_router(hero.router)
app.include_router(assignment.router)
