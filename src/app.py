from fastapi import FastAPI
from src.routers.hero import hero_router

app = FastAPI()
app.include_router(hero_router)
