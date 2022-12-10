from src.utils.sockets import *

import json


def is_valid_format(data: str):
    try:
        data = json.loads(data)
    except json.decoder.JSONDecodeError:
        return False
    if "type" not in data:
        False
    return True

class GameDaemon:
    def __init__(self, username):
        self.is_running = True
        self.client = TcpClient()
        self.client.connect(("127.0.0.1", 6666))
        data = {
            "type" : "my_username",
            "username" : username
        }
        self.client.send(json.dumps(data))
        self.receiver = MulticastReceiver(7777)
        self.receiver.join_group("225.1.2.3")
    
    def receive_from_tcp(self, signal):
        while self.is_running:
            msg = self.client.receive()
            if not is_valid_format(msg):
                continue
            data = json.loads(msg)
            if data["type"] in ["room_info", "game_winner"]:
                signal(data)

    def receive_from_mulicast(self, signal):
        while self.is_running:
            msg, address = self.receiver.receive_from()
            if not is_valid_format(msg):
                continue
            data = json.loads(msg)
            if data["type"] == "room_list":
                signal(data["room_list"])
    
    def show_room_info(self, data: dict):
        print(data)
    
    def show_game_winner(self, data: dict):
        print(data)

    def send_score(self, score):
        pass
        # TODO: RPC
    
    def close(self):
        self.client.close()
