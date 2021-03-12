from typing import List
from fastapi import APIRouter, status
import src.schemas.hero as schema

router = APIRouter(prefix="/hero", tags=["Heros"])

mock_hero = {"id": 1, "name": "sravan", "alter_ego": "Ravan"}


@router.get("/", response_model=List[schema.Hero], status_code=status.HTTP_200_OK)
def list():
    return [mock_hero]


@router.get("/{id}", response_model=schema.Hero, status_code=status.HTTP_200_OK)
def show(id: int):
    return mock_hero


@router.post("/", response_model=schema.Hero, status_code=status.HTTP_201_CREATED)
def create(request: schema.CreateHero):
    return mock_hero


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
):
    return {"success": True, "message": "Deleted"}


@router.put("/{id}", response_model=schema.Hero, status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Hero):
    return mock_hero
