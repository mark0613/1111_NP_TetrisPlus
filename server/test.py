from src.models import *
from src.services import *
from src.instances import *


user_service = UserService()
# print(user_service.get_user_by_id(1))
# print(user_service.get_user_by_id(3).username)

user_instance = UserInstance()
# user_instance.register("Demo", "aabbcc123")
# print(user_instance.login("Mark", "aabbcc123"))  # T
# print(user_instance.login("Mark", "dededeefe"))  # F
# print(user_instance.login("aaaa", "aabbcc123"))  # F

room_list_instance = RoomListInstance()
print("create")
result, room_id = room_list_instance.create_room("Mark")
print(result, room_id)
print(room_list_instance.get_room_members(room_id))
print(room_list_instance.get_all_rooms())
print("------")
print("add")
result = room_list_instance.add_room("Eating", room_id)
print(result)
print(room_list_instance.get_room_members(room_id))
print(room_list_instance.get_all_rooms())
print("------")
print("quit 1")
result = room_list_instance.quit_room("Mark")
print(result)
print(room_list_instance.get_room_members(room_id))
print(room_list_instance.get_all_rooms())
print("quit 2")
result = room_list_instance.quit_room("Eating")
print(result)
print(room_list_instance.get_room_members(room_id))
print(room_list_instance.get_all_rooms())
