from .pages import *

from PyQt5 import QtWidgets

PAGE_CLASSES = [
    MainPage,
    RegisterPage,
    LoginPage, 
    MenuPage,
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
