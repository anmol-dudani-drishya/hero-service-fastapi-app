from sqlalchemy.orm import Session
import src.schemas.hero as schema
import src.models.hero as model
from fastapi import HTTPException, status


def get_all(db: Session):
    heros = db.query(model.Hero).all()
    return heros


def show(id: int, db: Session):
    hero = db.query(model.Hero).filter(model.Hero.id == id).first()
    if not hero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hero with the id {id} is not available",
        )
    return hero


def create(request: schema.Hero, db: Session):
    new_hero = model.Hero(name=request.name, alter_ego=request.alter_ego)
    db.add(new_hero)
    db.commit()
    db.refresh(new_hero)
    return new_hero


def destroy(id: int, db: Session):
    hero = db.query(model.Hero).filter(model.Hero.id == id)

    if not hero.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Hero with id {id} not found"
        )

    hero.delete(synchronize_session=False)
    db.commit()
    return "Destroyed"


def update(id: int, request: schema.Hero, db: Session):
    hero = db.query(model.Hero).filter(model.Hero.id == id)

    if not hero.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Hero with id {id} not found"
        )

    hero.update(request)
    db.commit()
    return show(id, db)
