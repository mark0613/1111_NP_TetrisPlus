from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,

    Integer,
    String,
)

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


Base.metadata.create_all(settings.DB_ENGINE)
