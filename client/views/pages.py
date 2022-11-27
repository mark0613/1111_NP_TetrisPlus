from .components import *
from .ui_tetris import Ui_TetrisWindow
from src.game.tetris import Tetris
from src.game.keyboard import KeyBuffer
from src.utils.file import *

from PyQt5 import QtWidgets
import xmlrpc.client
import threading


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
            open_window("登入成功!")
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
        change_page(self.pages, "page_connection_room")
        # TODO: pair
    
    def on_button_rank_click(self, event):
        change_page(self.pages, "page_rank")

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

    def on_button_save_settings_click(self, event):
        mode = self.select_mode.currentText()
        speed = self.select_speed.currentText()
        config = {
            "mode" : mode,
            "speed" : speed,
        }
        dumpJsonFile(config, "client/.local/config.json")
        open_window("儲存成功!")
        change_page(self.pages, "page_single")
    
    def on_button_back_to_single_click(self, event):
        change_page(self.pages, "page_single")

class SingleGamePage(Ui_TetrisWindow):
    def play_game(self):
        self.key_buffer = KeyBuffer()
        self.condition = threading.Condition()
        Tetris.set_key_buffer(self.key_buffer)
        Tetris.set_condition(self.condition)
        tetris = Tetris()
        tetris.next_display_method = self.display_next_block
        tetris.held_display_method = self.display_held_block
        tetris.board_display_method = self.display_board_block
        t = threading.Thread(target=tetris.play)
        t.start()

    def display_next_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_next_in_single.setPixmap(QPixmap.fromImage(qimg))

    def display_held_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_held_in_single.setPixmap(QPixmap.fromImage(qimg))

    def display_board_block(self, title, img):
        qimg = cv2_to_qimage(img)
        self.img_board_in_single.setPixmap(QPixmap.fromImage(qimg))

class RoomPage(Ui_TetrisWindow):
    def bind(self):
        self.button_back_to_menu_in_room.mousePressEvent = self.on_button_back_to_menu_click

class ConnectionGamePage(Ui_TetrisWindow):
    # TODO: socket connect two player and show board
    pass

class EndPage(Ui_TetrisWindow):
    def bind(self):
        self.button_to_rank_in_end.mousePressEvent = self.on_button_rank_click

class RankPage(Ui_TetrisWindow):
    def bind(self):
        self.button_back_to_menu_in_rank.mousePressEvent = self.on_button_back_to_menu_click
        # TODO: show rank info

class RulePage(Ui_TetrisWindow):
    def bind(self):
        self.button_back_to_menu_in_rule.mousePressEvent = self.on_button_back_to_menu_click
        # TODO: show rule
