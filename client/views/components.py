from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QObject

Qt = QtCore.Qt

def open_window(message):
    error_window = QtWidgets.QMessageBox()
    error_window.setText(message)
    error_window.setStyleSheet("QMessageBox QLabel#qt_msgbox_label { min-height: 100px; min-width: 500px; } QMessageBox QLabel#qt_msgboxex_icon_label { min-height: 40px }")
    error_window.setWindowFlag(Qt.WindowStaysOnTopHint)
    error_window.exec_()

def cv2_to_qimage(src):
    h, w, c = src.shape
    p = w * 3
    return QtGui.QImage(src, w, h, p, QtGui.QImage.Format_RGB888).rgbSwapped()

def create_button(text: str, on_click, object_name=None):
    button = QtWidgets.QPushButton(text)
    font = QtGui.QFont("Microsoft JhengHei", 15)
    button.setFont(font)
    button.clicked.connect(on_click)
    if object_name:
        button.setObjectName(object_name)
    return button

def create_label(text: str, object_name=None):
    label = QtWidgets.QLabel(text)
    font = QtGui.QFont("Microsoft JhengHei", 15)
    label.setFont(font)
    if object_name:
        label.setObjectName(object_name)
    return label

def create_list_item(parent:QtWidgets.QListWidget, text: str):
    item = QtWidgets.QListWidgetItem(parent)
    font = QtGui.QFont("Microsoft JhengHei", 15)
    item.setFont(font)
    item.setText(text)
    item.setStatusTip(text)
    item.setTextAlignment(Qt.AlignLeft)
    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    return item

def add_list_item_contain_button(parent:QtWidgets.QListWidget, text: str, on_button_click):
    item = QtWidgets.QListWidgetItem(parent)
    room_id = text.split(" ")[0]
    label = create_label(text, f"label_room_{room_id}_in_room_list")
    label.setStyleSheet("QLabel { color: #fff; }")
    button = create_button("加入", on_button_click, f"button_add_room_{room_id}_in_room_list")
    button.setStyleSheet("QPushButton { color: #fff; }")

    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button)
    item_widget = QtWidgets.QWidget()
    item_widget.setLayout(layout)
    item.setSizeHint(item_widget.sizeHint())
    parent.addItem(item)
    parent.setItemWidget(item, item_widget)

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

class LongTask(QObject):
    def __init__(self, process, args=tuple()):
        super().__init__()
        self.process = process
        self.args = args

    def run(self):
        self.process(*self.args)
