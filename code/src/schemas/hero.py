from pydantic import BaseModel


class CreateHero(BaseModel):
    name: str
    alter_ego: str

    class Config:
        orm_mode = True


class Hero(CreateHero):
    id: int

    class Config:
        orm_mode = True
