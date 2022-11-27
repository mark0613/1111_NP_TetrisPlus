# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tetris.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TetrisWindow(object):
    def setupUi(self, TetrisWindow):
        TetrisWindow.setObjectName("TetrisWindow")
        TetrisWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TetrisWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.pages.setGeometry(QtCore.QRect(-1, -1, 801, 551))
        self.pages.setObjectName("pages")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.title_trteis_plus_1 = QtWidgets.QLabel(self.page_main)
        self.title_trteis_plus_1.setGeometry(QtCore.QRect(160, 50, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_trteis_plus_1.setFont(font)
        self.title_trteis_plus_1.setAlignment(QtCore.Qt.AlignCenter)
        self.title_trteis_plus_1.setObjectName("title_trteis_plus_1")
        self.button_to_login = QtWidgets.QPushButton(self.page_main)
        self.button_to_login.setGeometry(QtCore.QRect(270, 340, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_to_login.setFont(font)
        self.button_to_login.setObjectName("button_to_login")
        self.button_to_register = QtWidgets.QPushButton(self.page_main)
        self.button_to_register.setGeometry(QtCore.QRect(270, 230, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_to_register.setFont(font)
        self.button_to_register.setObjectName("button_to_register")
        self.pages.addWidget(self.page_main)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.title_register = QtWidgets.QLabel(self.page_register)
        self.title_register.setGeometry(QtCore.QRect(150, 50, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_register.setFont(font)
        self.title_register.setAlignment(QtCore.Qt.AlignCenter)
        self.title_register.setObjectName("title_register")
        self.input_username_in_register = QtWidgets.QLineEdit(self.page_register)
        self.input_username_in_register.setGeometry(QtCore.QRect(340, 210, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.input_username_in_register.setFont(font)
        self.input_username_in_register.setText("")
        self.input_username_in_register.setObjectName("input_username_in_register")
        self.label_username_in_register = QtWidgets.QLabel(self.page_register)
        self.label_username_in_register.setGeometry(QtCore.QRect(120, 210, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_username_in_register.setFont(font)
        self.label_username_in_register.setObjectName("label_username_in_register")
        self.label_password_in_register = QtWidgets.QLabel(self.page_register)
        self.label_password_in_register.setGeometry(QtCore.QRect(120, 300, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_password_in_register.setFont(font)
        self.label_password_in_register.setObjectName("label_password_in_register")
        self.input_password_in_register = QtWidgets.QLineEdit(self.page_register)
        self.input_password_in_register.setGeometry(QtCore.QRect(340, 300, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.input_password_in_register.setFont(font)
        self.input_password_in_register.setText("")
        self.input_password_in_register.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password_in_register.setObjectName("input_password_in_register")
        self.button_register = QtWidgets.QPushButton(self.page_register)
        self.button_register.setGeometry(QtCore.QRect(270, 410, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_register.setFont(font)
        self.button_register.setObjectName("button_register")
        self.link_to_login = QtWidgets.QPushButton(self.page_register)
        self.link_to_login.setGeometry(QtCore.QRect(230, 490, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(15)
        font.setUnderline(True)
        self.link_to_login.setFont(font)
        self.link_to_login.setObjectName("link_to_login")
        self.pages.addWidget(self.page_register)
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.title_login = QtWidgets.QLabel(self.page_login)
        self.title_login.setGeometry(QtCore.QRect(150, 40, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_login.setFont(font)
        self.title_login.setAlignment(QtCore.Qt.AlignCenter)
        self.title_login.setObjectName("title_login")
        self.button_login = QtWidgets.QPushButton(self.page_login)
        self.button_login.setGeometry(QtCore.QRect(280, 430, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.label_password_in_login = QtWidgets.QLabel(self.page_login)
        self.label_password_in_login.setGeometry(QtCore.QRect(130, 320, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_password_in_login.setFont(font)
        self.label_password_in_login.setObjectName("label_password_in_login")
        self.label_username_in_login = QtWidgets.QLabel(self.page_login)
        self.label_username_in_login.setGeometry(QtCore.QRect(130, 230, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_username_in_login.setFont(font)
        self.label_username_in_login.setObjectName("label_username_in_login")
        self.input_username_in_login = QtWidgets.QLineEdit(self.page_login)
        self.input_username_in_login.setGeometry(QtCore.QRect(350, 230, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.input_username_in_login.setFont(font)
        self.input_username_in_login.setText("")
        self.input_username_in_login.setObjectName("input_username_in_login")
        self.input_password_in_login = QtWidgets.QLineEdit(self.page_login)
        self.input_password_in_login.setGeometry(QtCore.QRect(350, 320, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.input_password_in_login.setFont(font)
        self.input_password_in_login.setText("")
        self.input_password_in_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password_in_login.setObjectName("input_password_in_login")
        self.link_to_register = QtWidgets.QPushButton(self.page_login)
        self.link_to_register.setGeometry(QtCore.QRect(240, 500, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(15)
        font.setUnderline(True)
        self.link_to_register.setFont(font)
        self.link_to_register.setObjectName("link_to_register")
        self.pages.addWidget(self.page_login)
        self.page_menu = QtWidgets.QWidget()
        self.page_menu.setObjectName("page_menu")
        self.button_single_mode = QtWidgets.QPushButton(self.page_menu)
        self.button_single_mode.setGeometry(QtCore.QRect(250, 210, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_single_mode.setFont(font)
        self.button_single_mode.setObjectName("button_single_mode")
        self.title_trteis_plus = QtWidgets.QLabel(self.page_menu)
        self.title_trteis_plus.setGeometry(QtCore.QRect(140, 50, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_trteis_plus.setFont(font)
        self.title_trteis_plus.setAlignment(QtCore.Qt.AlignCenter)
        self.title_trteis_plus.setObjectName("title_trteis_plus")
        self.button_connection_mode = QtWidgets.QPushButton(self.page_menu)
        self.button_connection_mode.setGeometry(QtCore.QRect(250, 290, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_connection_mode.setFont(font)
        self.button_connection_mode.setObjectName("button_connection_mode")
        self.button_rank = QtWidgets.QPushButton(self.page_menu)
        self.button_rank.setGeometry(QtCore.QRect(250, 370, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_rank.setFont(font)
        self.button_rank.setObjectName("button_rank")
        self.button_rule = QtWidgets.QPushButton(self.page_menu)
        self.button_rule.setGeometry(QtCore.QRect(250, 450, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_rule.setFont(font)
        self.button_rule.setObjectName("button_rule")
        self.pages.addWidget(self.page_menu)
        self.page_single = QtWidgets.QWidget()
        self.page_single.setObjectName("page_single")
        self.title_single = QtWidgets.QLabel(self.page_single)
        self.title_single.setGeometry(QtCore.QRect(150, 60, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_single.setFont(font)
        self.title_single.setAlignment(QtCore.Qt.AlignCenter)
        self.title_single.setObjectName("title_single")
        self.button_start = QtWidgets.QPushButton(self.page_single)
        self.button_start.setGeometry(QtCore.QRect(260, 270, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_start.setFont(font)
        self.button_start.setObjectName("button_start")
        self.button_settings = QtWidgets.QPushButton(self.page_single)
        self.button_settings.setGeometry(QtCore.QRect(260, 370, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_settings.setFont(font)
        self.button_settings.setObjectName("button_settings")
        self.button_back_to_menu_in_single = QtWidgets.QPushButton(self.page_single)
        self.button_back_to_menu_in_single.setGeometry(QtCore.QRect(0, 490, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_back_to_menu_in_single.setFont(font)
        self.button_back_to_menu_in_single.setObjectName("button_back_to_menu_in_single")
        self.pages.addWidget(self.page_single)
        self.page_settings = QtWidgets.QWidget()
        self.page_settings.setObjectName("page_settings")
        self.title_settings = QtWidgets.QLabel(self.page_settings)
        self.title_settings.setGeometry(QtCore.QRect(140, 30, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_settings.setFont(font)
        self.title_settings.setAlignment(QtCore.Qt.AlignCenter)
        self.title_settings.setObjectName("title_settings")
        self.select_mode = QtWidgets.QComboBox(self.page_settings)
        self.select_mode.setGeometry(QtCore.QRect(110, 250, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.select_mode.setFont(font)
        self.select_mode.setObjectName("select_mode")
        self.select_mode.addItem("")
        self.select_mode.addItem("")
        self.select_speed = QtWidgets.QComboBox(self.page_settings)
        self.select_speed.setGeometry(QtCore.QRect(400, 250, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.select_speed.setFont(font)
        self.select_speed.setObjectName("select_speed")
        self.select_speed.addItem("")
        self.select_speed.addItem("")
        self.select_speed.addItem("")
        self.select_speed.addItem("")
        self.button_save_settings = QtWidgets.QPushButton(self.page_settings)
        self.button_save_settings.setGeometry(QtCore.QRect(250, 370, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_save_settings.setFont(font)
        self.button_save_settings.setObjectName("button_save_settings")
        self.button_back_to_single = QtWidgets.QPushButton(self.page_settings)
        self.button_back_to_single.setGeometry(QtCore.QRect(0, 490, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_back_to_single.setFont(font)
        self.button_back_to_single.setObjectName("button_back_to_single")
        self.pages.addWidget(self.page_settings)
        self.page_single_game = QtWidgets.QWidget()
        self.page_single_game.setObjectName("page_single_game")
        self.img_board_in_single = QtWidgets.QLabel(self.page_single_game)
        self.img_board_in_single.setGeometry(QtCore.QRect(270, 80, 200, 400))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img_board_in_single.setFont(font)
        self.img_board_in_single.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img_board_in_single.setText("")
        self.img_board_in_single.setObjectName("img_board_in_single")
        self.img_next_in_single = QtWidgets.QLabel(self.page_single_game)
        self.img_next_in_single.setGeometry(QtCore.QRect(130, 80, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img_next_in_single.setFont(font)
        self.img_next_in_single.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img_next_in_single.setText("")
        self.img_next_in_single.setObjectName("img_next_in_single")
        self.img_held_in_single = QtWidgets.QLabel(self.page_single_game)
        self.img_held_in_single.setGeometry(QtCore.QRect(130, 230, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img_held_in_single.setFont(font)
        self.img_held_in_single.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img_held_in_single.setText("")
        self.img_held_in_single.setObjectName("img_held_in_single")
        self.label_time_in_single = QtWidgets.QLabel(self.page_single_game)
        self.label_time_in_single.setGeometry(QtCore.QRect(530, 80, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_in_single.setFont(font)
        self.label_time_in_single.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_in_single.setObjectName("label_time_in_single")
        self.label_score_in_single = QtWidgets.QLabel(self.page_single_game)
        self.label_score_in_single.setGeometry(QtCore.QRect(530, 360, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_score_in_single.setFont(font)
        self.label_score_in_single.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score_in_single.setObjectName("label_score_in_single")
        self.label_my_score_in_single = QtWidgets.QLabel(self.page_single_game)
        self.label_my_score_in_single.setGeometry(QtCore.QRect(530, 430, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_my_score_in_single.setFont(font)
        self.label_my_score_in_single.setAlignment(QtCore.Qt.AlignCenter)
        self.label_my_score_in_single.setObjectName("label_my_score_in_single")
        self.pages.addWidget(self.page_single_game)
        self.page_connection_room = QtWidgets.QWidget()
        self.page_connection_room.setObjectName("page_connection_room")
        self.label_player2_in_room = QtWidgets.QLabel(self.page_connection_room)
        self.label_player2_in_room.setGeometry(QtCore.QRect(180, 220, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_player2_in_room.setFont(font)
        self.label_player2_in_room.setAlignment(QtCore.Qt.AlignCenter)
        self.label_player2_in_room.setObjectName("label_player2_in_room")
        self.label_player1_in_room = QtWidgets.QLabel(self.page_connection_room)
        self.label_player1_in_room.setGeometry(QtCore.QRect(310, 70, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_player1_in_room.setFont(font)
        self.label_player1_in_room.setAlignment(QtCore.Qt.AlignCenter)
        self.label_player1_in_room.setObjectName("label_player1_in_room")
        self.label_single_rank_4 = QtWidgets.QLabel(self.page_connection_room)
        self.label_single_rank_4.setGeometry(QtCore.QRect(110, 390, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_single_rank_4.setFont(font)
        self.label_single_rank_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_single_rank_4.setObjectName("label_single_rank_4")
        self.img1 = QtWidgets.QLabel(self.page_connection_room)
        self.img1.setGeometry(QtCore.QRect(110, 50, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img1.setFont(font)
        self.img1.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img1.setText("")
        self.img1.setObjectName("img1")
        self.img2 = QtWidgets.QLabel(self.page_connection_room)
        self.img2.setGeometry(QtCore.QRect(580, 360, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img2.setFont(font)
        self.img2.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img2.setText("")
        self.img2.setObjectName("img2")
        self.button_back_to_menu_in_room = QtWidgets.QPushButton(self.page_connection_room)
        self.button_back_to_menu_in_room.setGeometry(QtCore.QRect(730, 10, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_back_to_menu_in_room.setFont(font)
        self.button_back_to_menu_in_room.setObjectName("button_back_to_menu_in_room")
        self.pages.addWidget(self.page_connection_room)
        self.page_connection_game = QtWidgets.QWidget()
        self.page_connection_game.setObjectName("page_connection_game")
        self.img_my_next_in_connection = QtWidgets.QLabel(self.page_connection_game)
        self.img_my_next_in_connection.setGeometry(QtCore.QRect(30, 80, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img_my_next_in_connection.setFont(font)
        self.img_my_next_in_connection.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img_my_next_in_connection.setText("")
        self.img_my_next_in_connection.setObjectName("img_my_next_in_connection")
        self.img_my_board_in_connention = QtWidgets.QLabel(self.page_connection_game)
        self.img_my_board_in_connention.setGeometry(QtCore.QRect(170, 80, 200, 400))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img_my_board_in_connention.setFont(font)
        self.img_my_board_in_connention.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img_my_board_in_connention.setText("")
        self.img_my_board_in_connention.setObjectName("img_my_board_in_connention")
        self.img_my_held_in_connection = QtWidgets.QLabel(self.page_connection_game)
        self.img_my_held_in_connection.setGeometry(QtCore.QRect(30, 230, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img_my_held_in_connection.setFont(font)
        self.img_my_held_in_connection.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img_my_held_in_connection.setText("")
        self.img_my_held_in_connection.setObjectName("img_my_held_in_connection")
        self.label_time_in_connection = QtWidgets.QLabel(self.page_connection_game)
        self.label_time_in_connection.setGeometry(QtCore.QRect(290, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_in_connection.setFont(font)
        self.label_time_in_connection.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_in_connection.setObjectName("label_time_in_connection")
        self.img_peer_held_in_connection = QtWidgets.QLabel(self.page_connection_game)
        self.img_peer_held_in_connection.setGeometry(QtCore.QRect(470, 180, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img_peer_held_in_connection.setFont(font)
        self.img_peer_held_in_connection.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img_peer_held_in_connection.setText("")
        self.img_peer_held_in_connection.setObjectName("img_peer_held_in_connection")
        self.img_peer_board_in_connection = QtWidgets.QLabel(self.page_connection_game)
        self.img_peer_board_in_connection.setGeometry(QtCore.QRect(570, 80, 150, 300))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img_peer_board_in_connection.setFont(font)
        self.img_peer_board_in_connection.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img_peer_board_in_connection.setText("")
        self.img_peer_board_in_connection.setObjectName("img_peer_board_in_connection")
        self.img_peer_next_in_connection = QtWidgets.QLabel(self.page_connection_game)
        self.img_peer_next_in_connection.setGeometry(QtCore.QRect(470, 80, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.img_peer_next_in_connection.setFont(font)
        self.img_peer_next_in_connection.setStyleSheet("QLabel {\n"
"    border: 1px solid #000;\n"
"}")
        self.img_peer_next_in_connection.setText("")
        self.img_peer_next_in_connection.setObjectName("img_peer_next_in_connection")
        self.label_player1_in_game = QtWidgets.QLabel(self.page_connection_game)
        self.label_player1_in_game.setGeometry(QtCore.QRect(40, 490, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_player1_in_game.setFont(font)
        self.label_player1_in_game.setAlignment(QtCore.Qt.AlignCenter)
        self.label_player1_in_game.setObjectName("label_player1_in_game")
        self.label_player2_in_game = QtWidgets.QLabel(self.page_connection_game)
        self.label_player2_in_game.setGeometry(QtCore.QRect(450, 490, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_player2_in_game.setFont(font)
        self.label_player2_in_game.setAlignment(QtCore.Qt.AlignCenter)
        self.label_player2_in_game.setObjectName("label_player2_in_game")
        self.pages.addWidget(self.page_connection_game)
        self.page_connection_end = QtWidgets.QWidget()
        self.page_connection_end.setObjectName("page_connection_end")
        self.label_winner = QtWidgets.QLabel(self.page_connection_end)
        self.label_winner.setGeometry(QtCore.QRect(260, 80, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_winner.setFont(font)
        self.label_winner.setAlignment(QtCore.Qt.AlignCenter)
        self.label_winner.setObjectName("label_winner")
        self.label_winner_player = QtWidgets.QLabel(self.page_connection_end)
        self.label_winner_player.setGeometry(QtCore.QRect(90, 130, 591, 121))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.label_winner_player.setFont(font)
        self.label_winner_player.setAlignment(QtCore.Qt.AlignCenter)
        self.label_winner_player.setObjectName("label_winner_player")
        self.label_score_in_end = QtWidgets.QLabel(self.page_connection_end)
        self.label_score_in_end.setGeometry(QtCore.QRect(260, 290, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_score_in_end.setFont(font)
        self.label_score_in_end.setText("")
        self.label_score_in_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score_in_end.setObjectName("label_score_in_end")
        self.button_to_rank_in_end = QtWidgets.QPushButton(self.page_connection_end)
        self.button_to_rank_in_end.setGeometry(QtCore.QRect(240, 420, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_to_rank_in_end.setFont(font)
        self.button_to_rank_in_end.setObjectName("button_to_rank_in_end")
        self.pages.addWidget(self.page_connection_end)
        self.page_rank = QtWidgets.QWidget()
        self.page_rank.setObjectName("page_rank")
        self.ranks = QtWidgets.QTabWidget(self.page_rank)
        self.ranks.setGeometry(QtCore.QRect(4, 49, 791, 501))
        self.ranks.setObjectName("ranks")
        self.tab_single_rank = QtWidgets.QWidget()
        self.tab_single_rank.setObjectName("tab_single_rank")
        self.label_single_rank = QtWidgets.QLabel(self.tab_single_rank)
        self.label_single_rank.setGeometry(QtCore.QRect(200, 20, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_single_rank.setFont(font)
        self.label_single_rank.setAlignment(QtCore.Qt.AlignCenter)
        self.label_single_rank.setObjectName("label_single_rank")
        self.ranks.addTab(self.tab_single_rank, "")
        self.tab_connection_rank = QtWidgets.QWidget()
        self.tab_connection_rank.setObjectName("tab_connection_rank")
        self.label_connection_rank = QtWidgets.QLabel(self.tab_connection_rank)
        self.label_connection_rank.setGeometry(QtCore.QRect(210, 20, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_connection_rank.setFont(font)
        self.label_connection_rank.setAlignment(QtCore.Qt.AlignCenter)
        self.label_connection_rank.setObjectName("label_connection_rank")
        self.ranks.addTab(self.tab_connection_rank, "")
        self.button_back_to_menu_in_rank = QtWidgets.QPushButton(self.page_rank)
        self.button_back_to_menu_in_rank.setGeometry(QtCore.QRect(720, 10, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_back_to_menu_in_rank.setFont(font)
        self.button_back_to_menu_in_rank.setObjectName("button_back_to_menu_in_rank")
        self.pages.addWidget(self.page_rank)
        self.page_rule = QtWidgets.QWidget()
        self.page_rule.setObjectName("page_rule")
        self.title_rule = QtWidgets.QLabel(self.page_rule)
        self.title_rule.setGeometry(QtCore.QRect(150, 30, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_rule.setFont(font)
        self.title_rule.setAlignment(QtCore.Qt.AlignCenter)
        self.title_rule.setObjectName("title_rule")
        self.button_back_to_menu_in_rule = QtWidgets.QPushButton(self.page_rule)
        self.button_back_to_menu_in_rule.setGeometry(QtCore.QRect(0, 490, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        self.button_back_to_menu_in_rule.setFont(font)
        self.button_back_to_menu_in_rule.setObjectName("button_back_to_menu_in_rule")
        self.pages.addWidget(self.page_rule)
        TetrisWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TetrisWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        TetrisWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TetrisWindow)
        self.statusbar.setObjectName("statusbar")
        TetrisWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TetrisWindow)
        self.pages.setCurrentIndex(0)
        self.ranks.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TetrisWindow)

    def retranslateUi(self, TetrisWindow):
        _translate = QtCore.QCoreApplication.translate
        TetrisWindow.setWindowTitle(_translate("TetrisWindow", "TetrisWindow"))
        self.title_trteis_plus_1.setText(_translate("TetrisWindow", "Tetris Plus"))
        self.button_to_login.setText(_translate("TetrisWindow", "登入"))
        self.button_to_register.setText(_translate("TetrisWindow", "註冊"))
        self.title_register.setText(_translate("TetrisWindow", "註冊"))
        self.label_username_in_register.setText(_translate("TetrisWindow", "Username :"))
        self.label_password_in_register.setText(_translate("TetrisWindow", "Password :"))
        self.button_register.setText(_translate("TetrisWindow", "註冊"))
        self.link_to_login.setText(_translate("TetrisWindow", "已經有帳號? 登入"))
        self.title_login.setText(_translate("TetrisWindow", "登入"))
        self.button_login.setText(_translate("TetrisWindow", "登入"))
        self.label_password_in_login.setText(_translate("TetrisWindow", "Password :"))
        self.label_username_in_login.setText(_translate("TetrisWindow", "Username :"))
        self.link_to_register.setText(_translate("TetrisWindow", "還沒註冊? 註冊"))
        self.button_single_mode.setText(_translate("TetrisWindow", "單人模式"))
        self.title_trteis_plus.setText(_translate("TetrisWindow", "Tetris Plus"))
        self.button_connection_mode.setText(_translate("TetrisWindow", "雙人連線"))
        self.button_rank.setText(_translate("TetrisWindow", "排行榜"))
        self.button_rule.setText(_translate("TetrisWindow", "遊戲規則"))
        self.title_single.setText(_translate("TetrisWindow", "單人"))
        self.button_start.setText(_translate("TetrisWindow", "開始遊戲"))
        self.button_settings.setText(_translate("TetrisWindow", "遊戲設置"))
        self.button_back_to_menu_in_single.setText(_translate("TetrisWindow", "<"))
        self.title_settings.setText(_translate("TetrisWindow", "遊戲設置"))
        self.select_mode.setItemText(0, _translate("TetrisWindow", "計時(120s)"))
        self.select_mode.setItemText(1, _translate("TetrisWindow", "Zen"))
        self.select_speed.setItemText(0, _translate("TetrisWindow", "簡單"))
        self.select_speed.setItemText(1, _translate("TetrisWindow", "正常"))
        self.select_speed.setItemText(2, _translate("TetrisWindow", "困難"))
        self.select_speed.setItemText(3, _translate("TetrisWindow", "專家"))
        self.button_save_settings.setText(_translate("TetrisWindow", "儲存"))
        self.button_back_to_single.setText(_translate("TetrisWindow", "<"))
        self.label_time_in_single.setText(_translate("TetrisWindow", "MM : SS"))
        self.label_score_in_single.setText(_translate("TetrisWindow", "score"))
        self.label_my_score_in_single.setText(_translate("TetrisWindow", "150"))
        self.label_player2_in_room.setText(_translate("TetrisWindow", "VS"))
        self.label_player1_in_room.setText(_translate("TetrisWindow", "P1 :"))
        self.label_single_rank_4.setText(_translate("TetrisWindow", "P2 :"))
        self.button_back_to_menu_in_room.setText(_translate("TetrisWindow", "H"))
        self.label_time_in_connection.setText(_translate("TetrisWindow", "MM : SS"))
        self.label_player1_in_game.setText(_translate("TetrisWindow", "P1 :"))
        self.label_player2_in_game.setText(_translate("TetrisWindow", "P2 :"))
        self.label_winner.setText(_translate("TetrisWindow", "WINNER"))
        self.label_winner_player.setText(_translate("TetrisWindow", "Player\'s Name"))
        self.button_to_rank_in_end.setText(_translate("TetrisWindow", "排行榜"))
        self.label_single_rank.setText(_translate("TetrisWindow", "個人排行榜"))
        self.ranks.setTabText(self.ranks.indexOf(self.tab_single_rank), _translate("TetrisWindow", "個人"))
        self.label_connection_rank.setText(_translate("TetrisWindow", "對戰排行榜"))
        self.ranks.setTabText(self.ranks.indexOf(self.tab_connection_rank), _translate("TetrisWindow", "對戰"))
        self.button_back_to_menu_in_rank.setText(_translate("TetrisWindow", "M"))
        self.title_rule.setText(_translate("TetrisWindow", "遊戲規則"))
        self.button_back_to_menu_in_rule.setText(_translate("TetrisWindow", "<"))
