from src.models import *
from src.services import *
from src.exceptions import *


class UserInstance:
    user_service = UserService()

    def register(self, username, password):
        user = UserModel(username, password)
        try:
            self.user_service.add_user(user)
        except DuplicateUsername:
            return False
        return True

    def login(self, username, password):
        user = UserModel(username, password)
        return self.user_service.login(user)
