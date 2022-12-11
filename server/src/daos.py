from .models import *
from .beans import *
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

class RankDao:
    def save(self, rank_record: RankModel):
        session.add(rank_record)
        session.commit()

    def update_score(self, rank_record: RankModel, score: int):
        session.query(RankModel).filter(
            RankModel.id == rank_record.id
        ).update({
            "score" : score
        })
        session.commit()

    def add_score(self, rank_record: RankModel, score: int):
        session.query(RankModel).filter(
            RankModel.id == rank_record.id
        ).update({
            "score" : RankModel.score + score
        })
        session.commit()
    
    def find_by_user(self, user: UserModel):
        return session.query(RankModel).filter(RankModel.user_id==user.id).all()
    
    def find_by_user_and_mode(self, user: UserModel, mode: str):
        return session.query(RankModel).filter(
            RankModel.user_id == user.id,
            RankModel.mode == mode
        ).first()

    def find_all(self):
        return session.query(RankModel).all()
    
    def find_all_by_mode(self, mode: str):
        return session.query(RankModel).filter(RankModel.mode==mode).all()

class RoomListDao:
    def create(self, user):
        return RoomList.create(user)
    
    def destroy(self, room_id):
        RoomList.destroy(room_id)

    def add(self, room_id, user):
        RoomList.add(room_id, user)
    
    def quit(self, user):
        RoomList.quit(user)

    def room_is_exist(self, room_id):
        return RoomList.room_is_exist(room_id)

    def user_in_room(self, user):
        return RoomList.user_in_room(user)
    
    def get_room_members(self, room_id):
        return RoomList.get_room_members(room_id)
    
    def get_all(self):
        return RoomList.get_all()
