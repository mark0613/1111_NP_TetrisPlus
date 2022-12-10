from .pages import *

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
import settings

PAGE_CLASSES = [
    MainPage,
    RegisterPage,
    LoginPage, 
    MenuPage,
    SinglePage,
    SettingsPage,
    SingleGamePage,
    RoomPage,
    ConnectionGamePage,
    EndPage,
    RankPage,
    RulePage,
    RoomListPage,
]
GAMING_PAGE = [
    "page_single_game",
]

class MainWindow(QtWidgets.QMainWindow, *PAGE_CLASSES):
    roomlist_signal = pyqtSignal(list)
    tcp_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.bind()
        self.img1.setPixmap(QtGui.QPixmap(f"{settings.STATIC_DIR}/block1.png"))
        self.img2.setPixmap(QtGui.QPixmap(f"{settings.STATIC_DIR}/block2.png"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{settings.STATIC_DIR}/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back_to_menu_in_room.setIcon(icon)
        self.button_back_to_menu_in_rank.setIcon(icon)
        MainPage.show(self)

    def bind(self):
        MainPage.bind(self)
        RegisterPage.bind(self)
        LoginPage.bind(self)
        MenuPage.bind(self)
        SinglePage.bind(self)
        SettingsPage.bind(self)
        RoomPage.bind(self)
        EndPage.bind(self)
        RankPage.bind(self)
        RulePage.bind(self)
        RoomListPage.bind(self)

    def start_daemon(self):
        def show_tcp_data(data: dict):
            print(data)
            if data["type"] == "room_info":
                self.show_room_info(data["room_info"])
            if data["type"] == "game_winner":
                print(data["game_winner"])
        if not hasattr(self, "daemon"):
            self.daemon = GameDaemon(self.username)
            self.roomlist_signal.connect(self.show_room_list)
            self.task_multicast = LongTask(self.daemon.receive_from_mulicast, (self.roomlist_signal.emit, ))
            self.thread_multicast = QThread()
            self.task_multicast.moveToThread(self.thread_multicast)
            self.thread_multicast.started.connect(self.task_multicast.run)
            self.thread_multicast.start()

            self.tcp_signal.connect(show_tcp_data)
            self.task_tcp = LongTask(self.daemon.receive_from_tcp, (self.tcp_signal.emit, ))
            self.thread_tcp = QThread()
            self.task_tcp.moveToThread(self.thread_tcp)
            self.thread_tcp.started.connect(self.task_tcp.run)
            self.thread_tcp.start()

    def keyPressEvent(self, event) -> None:
        key = event.text()
        if self.pages.currentWidget().objectName() not in GAMING_PAGE:
            return
        try:
            key = ord(key)
        except TypeError:
            key = -1
        self.key_buffer.put(key)
        with self.condition:
            self.condition.notifyAll()
        
    def closeEvent(self, event):
        self.daemon.close()
