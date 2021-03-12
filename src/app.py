from fastapi import FastAPI
import src.routers.hero as hero

app = FastAPI()
app.include_router(hero.router)
