from PyQt5 import QtGui, QtWidgets, QtCore


Qt = QtCore.Qt
QM = QtWidgets.QMessageBox

def open_window(message):
    error_window = QM()
    error_window.setText(message)
    error_window.setStyleSheet("QMessageBox QLabel#qt_msgbox_label { min-height: 100px; min-width: 500px; } QMessageBox QLabel#qt_msgboxex_icon_label { min-height: 40px }")
    error_window.setWindowFlag(Qt.WindowStaysOnTopHint)
    error_window.exec_()
