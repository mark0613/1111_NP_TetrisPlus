from src.instances import *
from src.daemons import *
import settings

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import threading

daemon = GameDaemon()

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
	pass

class AllInstances(UserInstance, RoomListInstance):
    def create_room(self, user):
        (result, room_id) = super().create_room(user)
        daemon.send_room_list()
        if room_id:
            daemon.send_room_info(room_id)
        return (result, room_id)
    
    def add_room(self, room_id, user):
        result =  super().add_room(room_id, user)
        daemon.send_room_list()
        if result:
            daemon.send_room_info(room_id)
        return result
    
    def quit_room(self, user):
        room_id = self.user_in_room(user)
        daemon.send_room_list()
        if room_id:
            daemon.send_room_info(room_id)
        result = super().quit_room(user)
        return result


if __name__ == "__main__":
    server = ThreadXMLRPCServer(('127.0.0.1', settings.SERVER_PORT), allow_none=True)
    server.register_instance(AllInstances())

    t1 = threading.Thread(target=daemon.run)
    print("Running...")
    try:
        t1.start()
        server.serve_forever()
    except KeyboardInterrupt:
        daemon.is_running = False
        print("Exit")
