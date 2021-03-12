from typing import List
from fastapi import APIRouter, status, Depends
import src.schemas.hero as schema
from src.database import get_db
from sqlalchemy.orm import Session
from src.repositories import hero

router = APIRouter(prefix="/hero", tags=["Heros"])


@router.get("/", response_model=List[schema.Hero], status_code=status.HTTP_200_OK)
def list(
    db: Session = Depends(get_db),
):
    return hero.get_all(db)


@router.get("/{id}", status_code=200, response_model=schema.Hero)
def show(id: int, db: Session = Depends(get_db)):
    return hero.show(id, db)


@router.post("/", response_model=schema.Hero, status_code=status.HTTP_201_CREATED)
def create(request: schema.CreateHero, db: Session = Depends(get_db)):
    return hero.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return hero.destroy(id, db)


@router.put("/{id}", response_model=schema.Hero, status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Hero, db: Session = Depends(get_db)):
    return hero.update(id, request, db)
