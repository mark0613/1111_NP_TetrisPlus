from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *


Qt = QtCore.Qt
QM = QtWidgets.QMessageBox

def open_window(message):
    error_window = QM()
    error_window.setText(message)
    error_window.setStyleSheet("QMessageBox QLabel#qt_msgbox_label { min-height: 100px; min-width: 500px; } QMessageBox QLabel#qt_msgboxex_icon_label { min-height: 40px }")
    error_window.setWindowFlag(Qt.WindowStaysOnTopHint)
    error_window.exec_()

def cv2_to_qimage(src):
    h, w, c = src.shape
    p = w * 3
    return QImage(src, w, h, p, QImage.Format_RGB888).rgbSwapped()

class MySelect:
    def __init__(self, parent, options):
        self.model = QtGui.QStandardItemModel()
        self.parent = parent
        self.options = options
        parent.currentIndexChanged[int].connect(self.on_current_index_changed)
        parent.setModel(self.model)

        self.parent.clear()
        for value, text in self.options:
            vt = QtGui.QStandardItem(text)
            vt.setData(value)
            self.model.appendRow(vt)

    def on_current_index_changed(self, row):
        vt = self.model.item(row)
        self.value = vt.data()
        self.text = vt.text()

    def get_options(self):
        return self.value
