from .pages import *

from PyQt5 import QtWidgets


PAGE_CLASSES = [
    MainPage,
    RegisterPage,
    LoginPage, 
    MenuPage,
    SingleGamePage,
]

class MainWindow(QtWidgets.QMainWindow, *PAGE_CLASSES):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.bind()
        MainPage.show(self)

    def bind(self):
        MainPage.bind(self)
        RegisterPage.bind(self)
        LoginPage.bind(self)
        MenuPage.bind(self)

    def keyPressEvent(self, event) -> None:
        key = event.text()
        try:
            key = ord(key)
        except TypeError:
            key = -1
        self.key_buffer.put(key)
        with self.condition:
            self.condition.notifyAll()
