from .models import *
import settings


session = settings.DB_SESSION()

class UserDao:
    def find_by_id(self, id: int):
        return session.query(UserModel).get(id)

    def find_by_username(self, username: str):
        return session.query(UserModel).filter(UserModel.username == username).first()

    def save(self, user: UserModel):
        session.add(user)
        session.commit()
