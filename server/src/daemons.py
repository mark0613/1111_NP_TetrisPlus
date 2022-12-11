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
        self.score_data = {}
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

    def send_game_winner(self, room_id: str, data: dict):
        members = self.room_list_service.get_room_members(room_id)
        for m in members:
            connection = self.username_connection_map[m]
            msg = json.dumps(data)
            connection.send(msg.encode("utf-8"))

    def receive_msg(self, socket):
        msg = None
        while not msg:
            msg = socket.recv(self.buf_size)
        return msg.decode("utf-8")

    def handle_end_game(self, data):
        def is_duplicate(info1: dict, info2: dict):
            same_players = False
            same_time = False
            set1 = set(info1["players"].keys())
            set2 = set(info2["players"].keys())
            print(set1, set2)
            if len(set1 | set2) == 2:
                same_players = True
            if info1["timestamp"] - info2["timestamp"] <= 30 * 1000:
                same_time = True
            return same_players and same_time
        
        def compare(p1: list, p2: list):
            if p1[1] > p2[1]:
                return -1
            if p1[1] == p2[1]:
                return 0
            return 1

        room_id = data["room_id"]
        info = data["info"]
        if room_id in self.score_data:
            old_info = self.score_data[room_id]
            if is_duplicate(info, old_info):
                self.score_data.pop(room_id, None)
                return
        self.score_data[room_id] = info
        p1 = []
        p2 = []
        idx = 0
        for p, s in info["players"].items():
            if idx == 0:
                p1 = [p, s]
            else:
                p2 = [p, s]
            idx += 1

        winner = None
        if compare(p1, p2) == 1:
            winner = p2[0]
        if compare(p1, p2) == -1:
            winner = p1[0]
        data = {
            "type" : "game_winner",
            "info" : {
                "players" : info["players"],
                "winner" : winner,
            },
        }
        self.send_game_winner(room_id, data)
        
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
                        if request["type"] == "end_game":
                            self.handle_end_game(request)
                    except ConnectionResetError:
                        for user, con in self.username_connection_map.items():
                            if con == connection:
                                self.username_connection_map.pop(user, None)
                                self.room_list_service.quit_room(user)
                                break
                        self.connections.remove(connection)
                        break
