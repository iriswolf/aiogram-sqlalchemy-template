from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=False)
    user_name = Column(String, nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now())
