from typing import List
from fastapi import APIRouter, status, Depends
import src.schemas.assignment as schema
from src.database import get_db
from sqlalchemy.orm import Session
from src.repositories import assignment

router = APIRouter(prefix="/assignment", tags=["Assignments"])


@router.get("/", response_model=List[schema.Assignment], status_code=status.HTTP_200_OK)
def list(
    db: Session = Depends(get_db),
):
    return assignment.get_all(db)


@router.get("/{id}", status_code=200, response_model=schema.Assignment)
def show(id: int, db: Session = Depends(get_db)):
    return assignment.show(id, db)


@router.post("/", response_model=schema.Assignment, status_code=status.HTTP_201_CREATED)
def create(request: schema.CreateAssignment, db: Session = Depends(get_db)):
    return assignment.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return assignment.destroy(id, db)


@router.put(
    "/{id}", response_model=schema.Assignment, status_code=status.HTTP_202_ACCEPTED
)
def update(id: int, request: schema.Assignment, db: Session = Depends(get_db)):
    return assignment.update(id, request, db)
