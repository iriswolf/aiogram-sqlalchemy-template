from sqlalchemy import Column, Integer, String

from src.database import Base


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    test = Column(String, nullable=False)
