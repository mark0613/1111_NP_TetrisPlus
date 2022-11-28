from src.instances import *
import settings

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn


class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
	pass

class AllInstances(UserInstance, RoomListInstance):
    pass


if __name__ == "__main__":
    server = ThreadXMLRPCServer(('localhost', int(settings.SERVER_PORT)))
    server.register_instance(AllInstances())

    print("Running...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exit")
