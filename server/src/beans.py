from .utils import *

import threading


class RoomList:
    room_list = {}
    lock = threading.Lock()

    @classmethod
    def create(cls, user):
        room_id = get_random_string(8)
        cls.lock.acquire()
        while room_id in cls.room_list:
            room_id = get_random_string(8)
        cls.room_list[room_id] = [user, ]
        cls.lock.release()
        return room_id

    @classmethod
    def destroy(cls, room_id):
        cls.lock.acquire()
        cls.room_list.pop(room_id, None)
        cls.lock.release()

    @classmethod
    def add(cls, room_id, user):
        cls.lock.acquire()
        cls.room_list[room_id].append(user)
        cls.lock.release()

    @classmethod
    def quit(cls, user):
        cls.lock.acquire()
        for room_id in cls.room_list:
            if user in cls.room_list[room_id]:
                cls.room_list[room_id].remove(user)
        cls.lock.release()

    @classmethod
    def room_is_exist(cls, room_id):
        result = False
        cls.lock.acquire()
        result = room_id in cls.room_list
        cls.lock.release()
        return result

    @classmethod
    def user_in_room(cls, user):
        result = False
        cls.lock.acquire()
        for room_id in cls.room_list:
            if user in cls.room_list[room_id]:
                result = True
                break
        cls.lock.release()
        return result

    @classmethod
    def get_room_members(cls, room_id):
        data = None
        cls.lock.acquire()
        data = cls.room_list[room_id]
        cls.lock.release()
        return data
    
    @classmethod
    def get_all(cls):
        data = {}
        cls.lock.acquire()
        data = cls.room_list
        cls.lock.release()
        return data
