from src.database import Base
from sqlalchemy import Column, Integer, String


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    details = Column(String)
