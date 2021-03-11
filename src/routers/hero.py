from fastapi import APIRouter
import src.schemas.hero as hero_schemas

hero_router = APIRouter(prefix="/hero", tags=["Heros"])


@hero_router.post("/")
def create_user(request: hero_schemas.CreateHero):
    return {"data": "success", "message": "Create Hero"}
