from .daos import *
from .models import *
from .exceptions import *


class UserService:
    user_dao = UserDao()

    def get_user_by_id(self, id: int) -> UserModel:
        return self.user_dao.find_by_id(id)

    def get_user_by_username(self, username: str) -> UserModel:
        return self.user_dao.find_by_username(username)

    def add_user(self, user: UserModel) -> None:
        if self.get_user_by_username(user.username) == None:
            self.user_dao.save(user)
        else:
            raise DuplicateUsername("duplicate username")

    def login(self, user: UserModel) -> bool:
        user_data = self.get_user_by_username(user.username)
        if user_data == None:
            return False
        return user_data.password == user.password
