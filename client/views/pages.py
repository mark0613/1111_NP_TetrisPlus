from .components import *
from .ui_tetris import Ui_TetrisWindow
from src.game.daemon import *
from src.game.keyboard import KeyBuffer
from src.game.my_tetris import MyTetris
from src.utils.config import *
from src.utils.file import *
from src.utils.record import *
from src.utils.sockets import *
from src.utils.tasks import Task

from datetime import datetime
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QThread
import xmlrpc.client
import threading
import time


IP = "127.0.0.1"
PORT = 8888
SERVER = xmlrpc.client.ServerProxy(f"http://{IP}:{PORT}")

page_map = {
    "page_main" : 0,
    "page_register" : 1,
    "page_login" : 2,
    "page_menu" : 3,
    "page_single" : 4,
    "page_settings" : 5,
    "page_single_game" : 6,
    "page_connection_room" : 7,
    "page_connection_game" : 8,
    "page_connection_end" : 9,
    "page_rank" : 10,
    "page_rule" : 11,
    "page_room_list" : 12,
}
def change_page(pages: QtWidgets.QStackedWidget, page_name: str):
    index = page_map[page_name]
    pages.setCurrentIndex(index)


class MainPage(Ui_TetrisWindow):
    def bind(self):
        self.button_to_register.mousePressEvent = self.on_button_to_register_click
        self.button_to_login.mousePressEvent = self.on_button_to_login_click

    def on_button_to_register_click(self, event):
        change_page(self.pages, "page_register")

    def on_button_to_login_click(self, event):
        change_page(self.pages, "page_login")
    
    def show(self):
        change_page(self.pages, "page_main")

class RegisterPage(Ui_TetrisWindow):
    def bind(self):
        self.button_register.mousePressEvent = self.on_button_register_click
        self.link_to_login.mousePressEvent = self.on_link_to_login_click
    
    def on_button_register_click(self, event):
        username = self.input_username_in_register.text()
        password = self.input_password_in_register.text()
        if SERVER.register(username, password):
            open_window("註冊成功\n前往登入!")
            change_page(self.pages, "page_login")
        else:
            open_window("註冊失敗\n帳號已經有人使用，請換一組!")

    def on_link_to_login_click(self, event):
        change_page(self.pages, "page_login")

class LoginPage(Ui_TetrisWindow):
    def bind(self):
        self.button_login.mousePressEvent = self.on_button_login_click
        self.link_to_register.mousePressEvent = self.on_link_to_register_click

    def on_button_login_click(self, event):
        username = self.input_username_in_login.text()
        password = self.input_password_in_login.text()
        if SERVER.login(username, password):
            self.username = username
            change_page(self.pages, "page_menu")
        else:
            open_window("帳號或密碼錯誤!")

    def on_link_to_register_click(self, event):
        change_page(self.pages, "page_register")

class MenuPage(Ui_TetrisWindow):
    def bind(self):
        self.button_single_mode.mousePressEvent = self.on_button_single_mode_click
        self.button_connection_mode.mousePressEvent = self.on_button_connection_mode_click
        self.button_rank.mousePressEvent = self.on_button_rank_click
        self.button_rule.mousePressEvent = self.on_button_rule_click

    def on_button_single_mode_click(self, event):
        change_page(self.pages, "page_single")

    def on_button_connection_mode_click(self, event):
        self.start_daemon()
        change_page(self.pages, "page_room_list")
    
    def on_button_rank_click(self, event):
        change_page(self.pages, "page_rank")
        self.show_all_rank()

    def on_button_rule_click(self, event):
        change_page(self.pages, "page_rule")
    
class SinglePage(Ui_TetrisWindow):
    def bind(self):
        self.button_start.mousePressEvent = self.on_button_start_click
        self.button_settings.mousePressEvent = self.on_button_settings_click
        self.button_back_to_menu_in_single.mousePressEvent = self.on_button_back_to_menu_click

    def on_button_start_click(self, event):
        change_page(self.pages, "page_single_game")
        self.play_game()

    def on_button_settings_click(self, event):
        change_page(self.pages, "page_settings")

    def on_button_back_to_menu_click(self, event):
        change_page(self.pages, "page_menu")

class SettingsPage(Ui_TetrisWindow):
    def bind(self):
        self.button_save_settings.mousePressEvent = self.on_button_save_settings_click
        self.button_back_to_single.mousePressEvent = self.on_button_back_to_single_click
        mode = [(False, "  計時(120s)"), (True, "  Zen")]
        speed = [(1, "  簡 單"), (2, "  正 常"), (3, "  困 難"), (4, "  專 家")]
        self.select_mode = MySelect(self.select_mode, mode)
        self.select_speed = MySelect(self.select_speed, speed)

    def on_button_save_settings_click(self, event):
        isZen = self.select_mode.get_options()
        speed = self.select_speed.get_options()
        config = {
            "isZen" : isZen,
            "speed" : speed,
        }
        save_config(config)
        open_window("儲存成功!")
        self.load_data()
        change_page(self.pages, "page_single")
    
    def on_button_back_to_single_click(self, event):
        change_page(self.pages, "page_single")

class SingleGamePage(Ui_TetrisWindow):
    def play_game(self):

        self.key_buffer = KeyBuffer()
        self.condition = threading.Condition()
        game = MyTetris()
        game.level = self.config["speed"]
        game.set_key_buffer(self.key_buffer)
        game.set_condition(self.condition)
        game.set_display_method(self.display_next_block, self.display_held_block, self.display_board_block)
        game.set_show_score_method(self.show_score_in_single)

        if self.config["isZen"]:
            self.show_time_in_single("--:--")
        else:
            timer = TimerDaemon(120)
            self.thread_timer = QThread()
            self.task_timer = LongTask(timer.run, (self.show_time_in_single, ))
            self.task_timer.moveToThread(self.thread_timer)
            self.thread_timer.started.connect(self.task_timer.run)
            timer.wait([
                Task(self.thread_timer.terminate),
                Task(self.end_game_in_single),
            ])
            self.thread_timer.start()

        self.task_single_game = LongTask(game.play)
        self.thread_single_game = QThread()
        self.task_single_game.moveToThread(self.thread_single_game)
        self.thread_single_game.started.connect(self.task_single_game.run)
        game.set_end_game_tasks([
            Task(self.end_game_in_single),
        ])
        self.thread_single_game.start()

    def display_next_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_next_in_single.setPixmap(QtGui.QPixmap.fromImage(qimg))

    def display_held_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_held_in_single.setPixmap(QtGui.QPixmap.fromImage(qimg))

    def display_board_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_board_in_single.setPixmap(QtGui.QPixmap.fromImage(qimg))

    def show_score_in_single(self, score: int):
        score = str(score)
        self.label_my_score_in_single.setText(score)

    def show_time_in_single(self, time: str):
        self.label_time_in_single.setText(time)

    def end_game_in_single(self):
        change_page(self.pages, "page_rank")
        self.thread_single_game.terminate()
        self.record = load_record()
        new_record = {
            "score": int(self.label_my_score_in_single.text()),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.record.append(new_record)
        save_record(self.record)
        self.ranks.setCurrentIndex(0)

class RoomPage(Ui_TetrisWindow):
    def bind(self):
        self.button_back_to_menu_in_room.mousePressEvent = self.quit_room
    
    def show_room_info(self, data: dict):
        room_id = data["room_id"]
        members = data["members"]
        room_is_full = False
        for idx, name in enumerate(members):
            if idx == 0:
                self.label_player1_in_room.setText(name)
            else:
                self.label_player2_in_room.setText(name)
            
            if name == self.username:
                self.my_connection_info = members[name]
            else:
                self.peer_name = name
                self.peer_connection_info = members[name]
                room_is_full = True
        if room_is_full:
            change_page(self.pages, "page_connection_game")
            self.play_connection_game()
    
    def quit_room(self, event):
        SERVER.quit_room(self.username)
        self.on_button_back_to_menu_click(event)

class ConnectionGamePage(Ui_TetrisWindow):
    def play_connection_game(self):
        self.label_player1_in_game.setText(self.username)
        self.label_player2_in_game.setText(self.peer_name)

        my_port = int(self.my_connection_info.split(":")[1])
        p_ip, p_port = self.peer_connection_info.split(":")
        p_port = int(p_port)
        self.daemon.start_game(my_port, (p_ip, p_port))

        self.key_buffer = KeyBuffer()
        self.condition = threading.Condition()
        self.my_game = MyTetris(20, self.daemon.send_game_board)
        self.my_game.set_key_buffer(self.key_buffer)
        self.my_game.set_condition(self.condition)
        self.my_game.set_display_method(self.display_p1_next_block, self.display_p1_held_block, self.display_p1_board_block)
        self.my_game.set_show_score_method(self.show_my_score_in_connection)
        self.my_game.set_end_game_tasks([
            Task(self.end_game_in_connection),
        ])
        
        peer_game = MyTetris(15)
        peer_game.set_display_method(self.display_p2_next_block, self.display_p2_held_block, self.display_p2_board_block)
        peer_game.set_show_score_method(self.show_peer_score_in_connection)

        self.task_udp = LongTask(self.daemon.receive_from_udp, (peer_game.display_with, ))
        self.thread_udp = QThread()
        self.task_udp.moveToThread(self.thread_udp)
        self.thread_udp.started.connect(self.task_udp.run)
        self.thread_udp.start()

        timer = TimerDaemon(120)
        self.thread_timer = QThread()
        self.task_timer = LongTask(timer.run, (self.show_time_in_connection, ))
        self.task_timer.moveToThread(self.thread_timer)
        self.thread_timer.started.connect(self.task_timer.run)
        timer.wait([
            Task(self.thread_timer.terminate),
            Task(self.end_game_in_connection),
        ])
        
        self.task_connection_game = LongTask(self.my_game.play)
        self.thread_connection_game = QThread()
        self.task_connection_game.moveToThread(self.thread_connection_game)
        self.thread_connection_game.started.connect(self.task_connection_game.run)
        self.thread_timer.start()
        self.thread_connection_game.start()
    
    def display_p1_next_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_my_next_in_connection.setPixmap(QtGui.QPixmap.fromImage(qimg))

    def display_p1_held_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_my_held_in_connection.setPixmap(QtGui.QPixmap.fromImage(qimg))

    def display_p1_board_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_my_board_in_connention.setPixmap(QtGui.QPixmap.fromImage(qimg))
        
    def display_p2_next_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_peer_next_in_connection.setPixmap(QtGui.QPixmap.fromImage(qimg))

    def display_p2_held_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_peer_held_in_connection.setPixmap(QtGui.QPixmap.fromImage(qimg))

    def display_p2_board_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_peer_board_in_connection.setPixmap(QtGui.QPixmap.fromImage(qimg))
    
    def show_my_score_in_connection(self, score: int):
        self.label_my_score_in_game.setText(str(score))

    def show_peer_score_in_connection(self, score: int):
        self.label_peer_score_in_game.setText(str(score))

    def show_time_in_connection(self, time: str):
        self.label_time_in_connection.setText(time)

    def stop_all(self):
        self.thread_connection_game.terminate()
        self.thread_timer.terminate()
        self.thread_udp.terminate()
        self.my_game.is_gaming = False

    def end_game_in_connection(self):
        data = {
            "type" : "end_game",
            "room_id" : self.room_id,
            "info" : {
                "players" : {
                    self.username : int(self.label_my_score_in_game.text()),
                    self.peer_name : int(self.label_peer_score_in_game.text()),
                },
                "timestamp" : int(time.time())
            }
        }
        self.daemon.send_end_game(data)
        self.stop_all()

class EndPage(Ui_TetrisWindow):
    def bind(self):
        self.button_to_rank_in_end.mousePressEvent = self.on_button_rank_click

    def show_winner(self, data: dict):
        change_page(self.pages, "page_connection_end")
        self.stop_all()
        winner = data["winner"]
        if not winner:
            winner = "--平手--"
        self.label_winner_player.setText(winner)
        s1 = data["players"][self.username]
        s2 = data["players"][self.peer_name]
        self.label_score_in_end.setText(f"{s1} vs {s2}")
        self.ranks.setCurrentIndex(1)

class RankPage(Ui_TetrisWindow):
    def bind(self):
        self.button_back_to_menu_in_rank.mousePressEvent = self.on_button_back_to_menu_click
        
    def show_all_rank(self):
        self.show_single_record()
        self.show_single_rank()
        self.show_connection_rank()

    def show_single_record(self):
        self.records = load_record()
        self.list_record.clear()
        data = self.records
        for row in data[-1::-1]:
            add_list_item_multitext(self.list_record, [str(row["score"]), row["time"]])

    def show_single_rank(self):
        data = SERVER.get_all_records("single")
        self.list_single_rank.clear()
        for row in data[-1::-1]:
            add_list_item_multitext(self.list_single_rank, [row["user"], str(row["score"])])

    def show_connection_rank(self):
        data = SERVER.get_all_records("connection")
        self.list_connection_rank.clear()
        for row in data[-1::-1]:
            add_list_item_multitext(self.list_connection_rank, [row["user"], str(row["score"])])

class RulePage(Ui_TetrisWindow):
    def bind(self):
        self.button_back_to_menu_in_rule.mousePressEvent = self.on_button_back_to_menu_click

class RoomListPage(Ui_TetrisWindow):
    def bind(self):
        self.button_create_room.mousePressEvent = self.on_button_create_room
    
    def on_button_create_room(self, event):
        (result, room_id) = SERVER.create_room(self.username)
        if result:
            change_page(self.pages, "page_connection_room")
            self.label_player1_in_room.setText(self.username)
            self.room_id = room_id
    
    def join_room(self, room_id):
        self.room_id = room_id
        result = SERVER.add_room(room_id, self.username)
        if result:
            change_page(self.pages, "page_connection_room")
        else:
            open_window("滿人了!")

    def show_room_list(self, data):
        self.list_room_list.clear()
        for room in data:
            room_id = room["room_id"]
            count = room["count"]
            add_list_item_contain_button(
                self.list_room_list,
                f"{room_id} [{count}/2]",
                lambda : self.join_room(room_id)
            )
