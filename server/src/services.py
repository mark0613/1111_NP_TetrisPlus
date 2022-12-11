from .daos import *
from .models import *
from .exceptions import *


class UserService:
    user_dao = UserDao()
    password_encoder = PasswordEncoder()

    def get_user_by_id(self, id: int) -> UserModel:
        return self.user_dao.find_by_id(id)

    def get_user_by_username(self, username: str) -> UserModel:
        return self.user_dao.find_by_username(username)

    def add_user(self, user: UserModel) -> None:
        if self.get_user_by_username(user.username) == None:
            user.password = self.password_encoder.encode(user.password)
            self.user_dao.save(user)
        else:
            raise DuplicateUsername("duplicate username")

    def login(self, user: UserModel) -> bool:
        user_data = self.get_user_by_username(user.username)
        if user_data == None:
            return False
        hash = user_data.password
        return self.password_encoder.verify(user.password, hash)

class RankService:
    rank_dao = RankDao()

    def update_score(self, user: UserModel, mode: str, score: int):
        record = self.get_user_record(user, mode)
        if record is None:
            record = RankModel(user, mode)
            self.rank_dao.save(record)
        
        if mode == "single":
            if score > record.score:
                self.rank_dao.update_score(record, score)
        if mode == "connection":
            self.rank_dao.add_score(record, score)

    def get_user_record(self, user: UserModel, mode: str=None):
        if mode:
            return self.rank_dao.find_by_user_and_mode(user, mode)
        return self.rank_dao.find_by_user(user)
    
    def get_all_records(self, mode: str=None):
        if mode:
            return self.rank_dao.find_all_by_mode(mode)
        return self.rank_dao.find_all()

class RoomListService:
    room_list_dao = RoomListDao()

    def create_room(self, user):
        if self.user_in_room(user):
            return (False, None)
        room_id = self.room_list_dao.create(user)
        return (True, room_id)
    
    def destroy_room(self, room_id):
        if self.room_is_exist(room_id):
            self.room_list_dao.destroy(room_id)
            return True
        return False
    
    def add_room(self, room_id, user):
        if self.user_in_room(user):
            return False
        if not self.room_is_exist(room_id):
            return False
        self.room_list_dao.add(room_id, user)
        return True
    
    def quit_room(self, user):
        room_id = self.user_in_room(user)
        if room_id:
            self.room_list_dao.quit(user)
            members = self.get_room_members(room_id)
            if len(members) == 0:
                self.destroy_room(room_id)
            return True
        return False
    
    def room_is_exist(self, room_id):
        return self.room_list_dao.room_is_exist(room_id)
    
    def user_in_room(self, user):
        return self.room_list_dao.user_in_room(user)

    def get_room_members(self, room_id):
        if self.room_is_exist(room_id):
            return self.room_list_dao.get_room_members(room_id)
        return None
    
    def get_all_rooms(self):
        return self.room_list_dao.get_all()
