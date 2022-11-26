from src.models import *
from src.services import *


class UserInstance:
    user_service = UserService()

    def register(self, username, password):
        user = UserModel(username, password)
        self.user_service.add_user(user)

    def login(self, username, password):
        user = UserModel(username, password)
        return self.user_service.login(user)
