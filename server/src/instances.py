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

class RankInstance:
    user_service = UserService()
    rank_service = RankService()

    def update_score(self, username, mode, score):
        user = self.user_service.get_user_by_username(username)
        self.rank_service.update_score(user, mode, score)
    
    def get_all_records(self, mode):
        records = self.rank_service.get_all_records(mode)
        result = []
        for record in records:
            result.append({
                "user" : record.user.username,
                "score" : record.score,
            })
        result.sort(key=lambda r: r["score"])
        return result

class RoomListInstance:
    room_list_service = RoomListService()

    def create_room(self, user):
        return self.room_list_service.create_room(user)

    def destroy_room(self, room_id):
        return self.room_list_service.destroy_room(room_id)

    def add_room(self, room_id, user):
        return self.room_list_service.add_room(room_id, user)

    def quit_room(self, user):
        return self.room_list_service.quit_room(user)

    def room_is_exist(self, room_id):
        return self.room_list_service.room_is_exist(room_id)

    def user_in_room(self, user):
        return self.room_list_service.user_in_room(user)

    def get_room_members(self, room_id):
        return self.room_list_service.get_room_members(room_id)
    
    def get_all_rooms(self):
        return self.room_list_service.get_all_rooms()
