from sqlalchemy.orm import Session
import src.schemas.assignment as schema
import src.models.assignment as model
from fastapi import HTTPException, status


def get_all(db: Session):
    assignments = db.query(model.Assignment).all()
    return assignments


def show(id: int, db: Session):
    assignment = db.query(model.Assignment).filter(model.Assignment.id == id).first()
    if not assignment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Assignment with the id {id} is not available",
        )
    return assignment


def create(request: schema.Assignment, db: Session):
    print("=================Before", request.name)
    new_assignment = model.Assignment(
        name=request.name,
        start_time=request.start_time,
        end_time=request.end_time,
        details=request.details,
    )
    print("=================After")
    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)
    return new_assignment


def destroy(id: int, db: Session):
    assignment = db.query(model.Assignment).filter(model.Assignment.id == id)

    if not assignment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Assignment with id {id} not found",
        )

    assignment.delete(synchronize_session=False)
    db.commit()
    return "Destroyed"


def update(id: int, request: schema.Assignment, db: Session):
    assignment = db.query(model.Assignment).filter(model.Assignment.id == id)

    if not assignment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Assignment with id {id} not found",
        )

    assignment.update(request)
    db.commit()
    return show(id, db)
