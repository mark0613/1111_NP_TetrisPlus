from src.models import *
from src.services import *
from src.instances import *


# user_service = UserService()
# print(user_service.get_user_by_id(1))
# print(user_service.get_user_by_id(3).username)


user_instance = UserInstance()
# user_instance.register("Demo", "aabbcc123")
# print(user_instance.login("Mark", "aabbcc123"))  # T
# print(user_instance.login("Mark", "dededeefe"))  # F
# print(user_instance.login("aaaa", "aabbcc123"))  # F
