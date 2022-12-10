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
