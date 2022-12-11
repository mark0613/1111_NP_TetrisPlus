from src.game.data_format import TetrisData
from src.utils.sockets import *
from src.utils.tasks import Task

import json
import time


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
    
    def start_game(self, my_port: int, peer_address: tuple):
        self.udp = UdpSocket()
        self.udp.buf_size = 1024 * 3
        self.udp.bind(my_port)
        self.peer = peer_address
    
    def send_game_board(self, data: str):
        self.udp.send_to(data, self.peer)

    def receive_from_udp(self, signal):
        while self.is_running:
            msg, address = self.udp.receive_from()
            data = TetrisData.load_by_string(msg)
            signal(data)
    
    def show_game_winner(self, data: dict):
        print(data)

    def send_score(self, score):
        pass
        # TODO: RPC
    
    def close(self):
        self.client.close()

class TimerDaemon:
    def __init__(self, seconds: int):
        self.seconds = seconds - 1
    
    def run(self, show=print):
        while self.seconds >= 0:
            mm = str(self.seconds // 60).zfill(2)
            ss = str(self.seconds % 60).zfill(2)
            text = f"{mm}:{ss}"
            show(text)
            self.seconds -= 1
            time.sleep(1)
        if hasattr(self, "tasks"):
            for task in self.tasks:
                task.run()
    
    def wait(self, tasks: list):
        self.tasks = tasks
