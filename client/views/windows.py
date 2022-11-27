from .pages import *

from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, MainPage, RegisterPage):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.bind()
        MainPage.show(self)

    def bind(self):
        MainPage.bind(self)
        RegisterPage.bind(self)
