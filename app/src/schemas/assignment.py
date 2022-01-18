from typing import Optional
from pydantic import BaseModel


class CreateAssignment(BaseModel):
    name: str
    start_time: Optional[str] = ""
    end_time: Optional[str] = ""
    details: Optional[str] = ""

    class Config:
        orm_mode = True


class Assignment(CreateAssignment):
    id: int

    class Config:
        orm_mode = True
