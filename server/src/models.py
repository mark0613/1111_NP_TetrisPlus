from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import settings


Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password = Column(String(60), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class RankModel(Base):
    __tablename__ = "rank"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    mode = Column(String(10), nullable=False)
    score = Column(Integer, nullable=False)
    
    user = relationship("UserModel")

    def __init__(self, user: UserModel, mode: str):
        self.user = user
        self.mode = mode
        self.score = 0

Base.metadata.drop_all(settings.DB_ENGINE)
Base.metadata.create_all(settings.DB_ENGINE)
