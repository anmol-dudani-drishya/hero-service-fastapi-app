from sqlalchemy import Column, Integer, String
from src.database import Base


class Hero(Base):
    __tablename__ = "heros"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    alter_ego = Column(String)
