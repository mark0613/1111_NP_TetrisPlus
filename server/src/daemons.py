from src.services import *
from src.utils import *

import json


class GameDaemon:
    room_list_service = RoomListService()

    def __init__(self):
        self.is_running = True
        self.buf_size = 1024
        self.ports = [6666]
        self.servers = []
        self.connections = []
        self.group_address = "225.1.2.3"
        self.multicase_sender = MulticastSender()
        self.username_connection_map = {}
        self.bind_ports()
    
    def bind_ports(self):
        for port in self.ports:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('', port))
            server.setblocking(False)
            server.listen(5)
            self.servers.append(server)
            self.connections.append(server)

    def send_room_list(self):
        room_list = self.room_list_service.get_all_rooms()
        data = {
            "type" : "room_list",
            "room_list" : []
        }
        for room_id, members in room_list.items():
            data["room_list"].append({
                "room_id" : room_id,
                "count" : len(members),
            })

        data = json.dumps(data)
        self.multicase_sender.send_to(data, (self.group_address, 7777))

    def send_room_info(self, room_id):
        members = self.room_list_service.get_room_members(room_id)
        members_address = {}
        for member in members:
            connection = self.username_connection_map[member]
            ip, port = connection.getpeername()
            members_address[member] = f"{ip}:{port}"
        data = {
            "type" : "room_info",
            "room_info" : {
                "room_id" : room_id,
                "members" : members_address,
            }
        }
        data = json.dumps(data)
        for username in members:
            try:
                connection = self.username_connection_map[username]
                connection.send(data.encode("utf-8"))
            except:
                pass

    def send_game_winner(self, room_id):
        """
        data = {
            "type" : "game_winner",
            "info" : {
                "p1" : {
                    "username" : "",
                    "score" : 100
                },
                "p2" : {
                    # 同上
                },
                "winner" : "p1"
            }
        }
        """
        pass

    def receive_msg(self, socket):
        msg = None
        while not msg:
            msg = socket.recv(self.buf_size)
        return msg.decode("utf-8")

    def run(self):
        output = []
        while self.is_running:
            readable, writable, exceptional = select.select(self.connections, output, self.connections)
            for connection in readable:
                if connection in self.servers:
                    client, (rip, rport) = connection.accept()
                    client.setblocking(False)
                    self.connections.append(client)
                    local_address = client.getsockname()
                    msg = f"Connection on {local_address[1]} from {rip}:{rport}"
                    print(msg)
                    self.send_room_list()
                else:
                    try:
                        request = self.receive_msg(connection)
                        request = json.loads(request)
                        if request["type"] == "my_username":
                            username = request["username"]
                            self.username_connection_map[username] = connection
                        r_addr = connection.getpeername()
                        l_addr = connection.getsockname()
                    except ConnectionResetError:
                        self.connections.remove(connection)
                        break
