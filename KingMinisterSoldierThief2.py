#################### Works with PyQt6 version 6.0.3 ####################

from PyQt6 import QtWidgets, QtCore, QtGui, QtTest
from PIL import Image, ImageDraw, ImageFilter
import random
from playsound import playsound


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QtGui.QIcon("WindowIcon.ico"))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 18))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 9))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 121, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 18))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 9))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 121, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 18))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 9))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 121, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(182, 182, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label = QtWidgets.QLabel("Set the Players\' Names", self.groupBox)
        self.label.setGeometry(470, 50, 500, 50)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:blue")

        self.player1 = QtWidgets.QLabel("Player 1", self.groupBox)
        self.player1.setGeometry(200, 150, 300, 50)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.player1.setFont(font)

        self.player2 = QtWidgets.QLabel("Player 2", self.groupBox)
        self.player2.setGeometry(1000, 150, 300, 50)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.player2.setFont(font)
        
        self.player3 = QtWidgets.QLabel("Player 3", self.groupBox)
        self.player3.setGeometry(200, 400, 300, 50)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.player3.setFont(font)
        
        self.player4 = QtWidgets.QLabel("Player 4", self.groupBox)
        self.player4.setGeometry(1000, 400, 300, 50)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.player4.setFont(font)

        self.name_input_1 = QtWidgets.QLineEdit(self.groupBox)
        self.name_input_1.move(140, 220)
        self.name_input_1.setPlaceholderText("Player 1")
        self.name_input_1.setStyleSheet("background-color:red")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.name_input_1.setFont(font)
        self.name_input_1.setMaxLength(15)

        self.name_input_2 = QtWidgets.QLineEdit(self.groupBox)
        self.name_input_2.move(940, 220)
        self.name_input_2.setPlaceholderText("Player 2")
        self.name_input_2.setStyleSheet("background-color:blue")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.name_input_2.setFont(font)
        self.name_input_2.setMaxLength(15)

        self.name_input_3 = QtWidgets.QLineEdit(self.groupBox)
        self.name_input_3.move(140, 470)
        self.name_input_3.setPlaceholderText("Player 3")
        self.name_input_3.setStyleSheet("background-color:yellow")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.name_input_3.setFont(font)
        self.name_input_3.setMaxLength(15)

        self.name_input_4 = QtWidgets.QLineEdit(self.groupBox)
        self.name_input_4.move(940, 470)
        self.name_input_4.setPlaceholderText("Player 4")
        self.name_input_4.setStyleSheet("background-color:green")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.name_input_4.setFont(font)
        self.name_input_4.setMaxLength(15)

        self.submit = QtWidgets.QPushButton("Submit", self.centralwidget)
        self.submit.setStyleSheet("color:blue\n;"
        "background-color:pink;")
        self.submit.setGeometry(600, 600, 150, 50)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.submit.setFont(font)

        self.target = QtWidgets.QSpinBox(self.groupBox)
        self.target.setGeometry(QtCore.QRect(550, 350, 300, 100))
        self.target.setMinimum(2000)
        self.target.setMaximum(100000)
        self.target.setSingleStep(2000)
        self.target.setFont(QtGui.QFont("Arial", 50))
        self.target.setStyleSheet("background-color:yellow")
        self.target.hide()

        self.pic_input_1 = QtWidgets.QPushButton(self.groupBox)
        self.pic_input_1.setGeometry(70, 220, 50, 50)
        self.pic_input_1.setStyleSheet("border-radius:25px")
        self.pic_input_1.setIcon(QtGui.QIcon("userpic.png"))
        self.pic_input_1.setIconSize(QtCore.QSize(50, 50))

        self.pic_input_2 = QtWidgets.QPushButton(self.groupBox)
        self.pic_input_2.setGeometry(870, 220, 50, 50)
        self.pic_input_2.setStyleSheet("border-radius:25px")
        self.pic_input_2.setIcon(QtGui.QIcon("userpic.png"))
        self.pic_input_2.setIconSize(QtCore.QSize(50, 50))

        self.pic_input_3 = QtWidgets.QPushButton(self.groupBox)
        self.pic_input_3.setGeometry(70, 470, 50, 50)
        self.pic_input_3.setStyleSheet("border-radius:25px")
        self.pic_input_3.setIcon(QtGui.QIcon("userpic.png"))
        self.pic_input_3.setIconSize(QtCore.QSize(50, 50))

        self.pic_input_4 = QtWidgets.QPushButton(self.groupBox)
        self.pic_input_4.setGeometry(870, 470, 50, 50)
        self.pic_input_4.setStyleSheet("border-radius:25px")
        self.pic_input_4.setIcon(QtGui.QIcon("userpic.png"))
        self.pic_input_4.setIconSize(QtCore.QSize(50, 50))

        self.start = QtWidgets.QPushButton("Start Game", self.groupBox)
        self.start.setGeometry(QtCore.QRect(550, 600, 250, 70))
        self.start.setStyleSheet("color:blue;"
                                 "background-color:pink")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.start.setFont(font)
        self.start.hide()

        self.player_1_name = QtWidgets.QLabel(self.groupBox)
        self.player_1_name.setGeometry(QtCore.QRect(265, 100, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(1000)
        self.player_1_name.setFont(font)
        self.player_1_name.setStyleSheet("color:red")
        self.player_1_name.hide()

        self.player_2_name = QtWidgets.QLabel(self.groupBox)
        self.player_2_name.setGeometry(QtCore.QRect(900, 100, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(1000)
        self.player_2_name.setFont(font)
        self.player_2_name.setStyleSheet("color:blue")
        self.player_2_name.hide()

        self.player_3_name = QtWidgets.QLabel(self.groupBox)
        self.player_3_name.setGeometry(QtCore.QRect(265, 400, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(1000)
        self.player_3_name.setFont(font)
        self.player_3_name.setStyleSheet("color:brown")
        self.player_3_name.hide()

        self.player_4_name = QtWidgets.QLabel(self.groupBox)
        self.player_4_name.setGeometry(QtCore.QRect(900, 400, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(1000)
        self.player_4_name.setFont(font)
        self.player_4_name.setStyleSheet("color:green")
        self.player_4_name.hide()

        self.score_1 = QtWidgets.QLabel(self.groupBox)
        self.score_1.setGeometry(QtCore.QRect(265, 160, 300, 50))
        self.score_1.setText("Total Score: 0")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.score_1.setFont(font)
        self.score_1.hide()

        self.score_2 = QtWidgets.QLabel(self.groupBox)
        self.score_2.setGeometry(QtCore.QRect(900, 160, 300, 50))
        self.score_2.setText("Total Score: 0")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.score_2.setFont(font)
        self.score_2.hide()

        self.score_3 = QtWidgets.QLabel(self.groupBox)
        self.score_3.setGeometry(QtCore.QRect(265, 460, 300, 50))
        self.score_3.setText("Total Score: 0")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.score_3.setFont(font)
        self.score_3.hide()

        self.score_4 = QtWidgets.QLabel(self.groupBox)
        self.score_4.setGeometry(QtCore.QRect(900, 460, 300, 50))
        self.score_4.setText("Total Score: 0")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.score_4.setFont(font)
        self.score_4.hide()

        self.pic_1_label = QtWidgets.QLabel(self.groupBox)
        self.pic_1_label.setGeometry(105, 110, 150, 150)
        self.pic_1_label.setStyleSheet("border-radius:75px")
        self.pic_1_label.setPixmap(QtGui.QPixmap("userpic.png"))
        self.pic_1_label.setScaledContents(True)
        self.pic_1_label.hide()

        self.pic_2_label = QtWidgets.QLabel(self.groupBox)
        self.pic_2_label.setGeometry(740, 110, 150, 150)
        self.pic_2_label.setStyleSheet("border-radius:75px")
        self.pic_2_label.setPixmap(QtGui.QPixmap("userpic.png"))
        self.pic_2_label.setScaledContents(True)
        self.pic_2_label.hide()

        self.pic_3_label = QtWidgets.QLabel(self.groupBox)
        self.pic_3_label.setGeometry(105, 410, 150, 150)
        self.pic_3_label.setStyleSheet("border-radius:75px")
        self.pic_3_label.setPixmap(QtGui.QPixmap("userpic.png"))
        self.pic_3_label.setScaledContents(True)
        self.pic_3_label.hide()

        self.pic_4_label = QtWidgets.QLabel(self.groupBox)
        self.pic_4_label.setGeometry(740, 410, 150, 150)
        self.pic_4_label.setStyleSheet("border-radius:75px")
        self.pic_4_label.setPixmap(QtGui.QPixmap("userpic.png"))
        self.pic_4_label.setScaledContents(True)
        self.pic_4_label.hide()

        self.you_got_1 = QtWidgets.QLabel(self.groupBox)
        self.you_got_1.setGeometry(265, 200, 400, 50)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.you_got_1.setFont(font)
        self.you_got_1.hide()

        self.you_got_2 = QtWidgets.QLabel(self.groupBox)
        self.you_got_2.setGeometry(900, 200, 400, 50)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.you_got_2.setFont(font)
        self.you_got_2.hide()
        
        self.you_got_3 = QtWidgets.QLabel(self.groupBox)
        self.you_got_3.setGeometry(265, 500, 400, 50)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.you_got_3.setFont(font)
        self.you_got_3.hide()
        
        self.you_got_4 = QtWidgets.QLabel(self.groupBox)
        self.you_got_4.setGeometry(900, 500, 400, 50)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.you_got_4.setFont(font)
        self.you_got_4.hide()

        self.shuffle = QtWidgets.QPushButton("Shuffle", self.groupBox)
        self.shuffle.setGeometry(550, 600, 200, 70)
        self.shuffle.setStyleSheet("background-color:red;\n"
                                   "color:blue;\n"
                                   "border-style:outset;\n"
                                   "border-width:2px;\n"
                                   "font:bold")
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.shuffle.setFont(font)
        self.shuffle.close()

        self.label1 = QtWidgets.QLabel(self.groupBox)
        self.label1.setGeometry(QtCore.QRect(450, 280, 371, 41))
        self.label1.setStyleSheet("color:pink")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.Alignment.AlignVCenter)
        self.label1.setAlignment(QtCore.Qt.Alignment.AlignHCenter)
        self.label1.hide()

        self.show_king = QtWidgets.QPushButton("Show the King", self.groupBox)
        self.show_king.setGeometry(QtCore.QRect(550, 600, 220, 70))
        self.show_king.setStyleSheet("background-color:yellow;\n"
                                     "color:green;\n"
                                     "border-style:outset;\n"
                                     "border-width:2px;\n"
                                     "font:bold 30px")
        self.show_king.setObjectName("show_king")
        self.show_king.close()

        self.show_minister = QtWidgets.QPushButton("Show Minister", self.groupBox)
        self.show_minister.setGeometry(QtCore.QRect(550, 600, 220, 70))
        self.show_minister.setStyleSheet("background-color:yellow;\n"
                                         "color:green;\n"
                                         "border-style:outset;\n"
                                         "border-width:2px;\n"
                                         "font:bold 30px")
        self.show_minister.close()

        self.king_pic_1 = QtWidgets.QLabel(self.groupBox)
        self.king_pic_1.setGeometry(QtCore.QRect(0, 15, 220, 170))
        self.king_pic_1.setPixmap(QtGui.QPixmap("king_rot.png"))
        self.king_pic_1.setScaledContents(True)
        self.king_pic_1.hide()

        self.king_pic_2 = QtWidgets.QLabel(self.groupBox)
        self.king_pic_2.setGeometry(QtCore.QRect(635, 15, 220, 170))
        self.king_pic_2.setPixmap(QtGui.QPixmap("king_rot.png"))
        self.king_pic_2.setScaledContents(True)
        self.king_pic_2.hide()

        self.king_pic_3 = QtWidgets.QLabel(self.groupBox)
        self.king_pic_3.setGeometry(QtCore.QRect(0, 315, 220, 170))
        self.king_pic_3.setPixmap(QtGui.QPixmap("king_rot.png"))
        self.king_pic_3.setScaledContents(True)
        self.king_pic_3.hide()

        self.king_pic_4 = QtWidgets.QLabel(self.groupBox)
        self.king_pic_4.setGeometry(QtCore.QRect(635, 315, 220, 170))
        self.king_pic_4.setPixmap(QtGui.QPixmap("king_rot.png"))
        self.king_pic_4.setScaledContents(True)
        self.king_pic_4.hide()

        self.minister_pic_1 = QtWidgets.QLabel(self.groupBox)
        self.minister_pic_1.setGeometry(QtCore.QRect(83, 70, 191, 80))
        self.minister_pic_1.setPixmap(QtGui.QPixmap("minister.png"))
        self.minister_pic_1.setScaledContents(True)
        self.minister_pic_1.hide()

        self.minister_pic_2 = QtWidgets.QLabel(self.groupBox)
        self.minister_pic_2.setGeometry(QtCore.QRect(718, 70, 191, 80))
        self.minister_pic_2.setPixmap(QtGui.QPixmap("minister.png"))
        self.minister_pic_2.setScaledContents(True)
        self.minister_pic_2.hide()

        self.minister_pic_3 = QtWidgets.QLabel(self.groupBox)
        self.minister_pic_3.setGeometry(QtCore.QRect(83, 370, 191, 80))
        self.minister_pic_3.setPixmap(QtGui.QPixmap("minister.png"))
        self.minister_pic_3.setScaledContents(True)
        self.minister_pic_3.hide()

        self.minister_pic_4 = QtWidgets.QLabel(self.groupBox)
        self.minister_pic_4.setGeometry(QtCore.QRect(718, 370, 191, 80))
        self.minister_pic_4.setPixmap(QtGui.QPixmap("minister.png"))
        self.minister_pic_4.setScaledContents(True)
        self.minister_pic_4.hide()

        self.its_thief_1 = QtWidgets.QPushButton(self.groupBox)
        self.its_thief_1.setGeometry(QtCore.QRect(265, 200, 100, 100))
        self.its_thief_1.setStyleSheet("background-color:green")
        self.its_thief_1.setEnabled(False)
        self.its_thief_1.hide()
        
        self.its_thief_2 = QtWidgets.QPushButton(self.groupBox)
        self.its_thief_2.setGeometry(QtCore.QRect(900, 200, 100, 100))
        self.its_thief_2.setStyleSheet("background-color:green")
        self.its_thief_2.setEnabled(False)
        self.its_thief_2.hide()
        
        self.its_thief_3 = QtWidgets.QPushButton(self.groupBox)
        self.its_thief_3.setGeometry(QtCore.QRect(265, 500, 100, 100))
        self.its_thief_3.setStyleSheet("background-color:green")
        self.its_thief_3.setEnabled(False)
        self.its_thief_3.hide()
        
        self.its_thief_4 = QtWidgets.QPushButton(self.groupBox)
        self.its_thief_4.setGeometry(QtCore.QRect(900, 500, 100, 100))
        self.its_thief_4.setStyleSheet("background-color:green")
        self.its_thief_4.setEnabled(False)
        self.its_thief_4.hide()

        self.winner_pic = QtWidgets.QLabel(self.groupBox)
        self.winner_pic.setGeometry(500, 150, 400, 400)
        self.winner_pic.close()

        self.next = QtWidgets.QPushButton("Next", self.groupBox)
        self.next.setGeometry(QtCore.QRect(550, 600, 200, 80))
        self.next.setStyleSheet("background-color:orange;\n"
                                "color:blue;\n"
                                "border-style:outset;\n"
                                "border-width:2px;\n"
                                "font:bold 30px")
        self.next.hide()
        self.next.setEnabled(False)

        self.win_label = QtWidgets.QLabel(self.groupBox)
        self.win_label.setGeometry(300, 600, 50, 200)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.win_label.setFont(font)
        self.win_label.setStyleSheet("color:brown")
        self.win_label.close()

        self.restart = QtWidgets.QPushButton("Restart", self.centralwidget)
        self.restart.setGeometry(1250, 2, 50, 22)
        self.restart.setStyleSheet("color:blue;"
                                    "background-color:orange")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.restart.setFont(font)
        self.restart.close()

        self.pic_input_1.clicked.connect(self.pic_input_1_clicked)
        self.pic_input_2.clicked.connect(self.pic_input_2_clicked)
        self.pic_input_3.clicked.connect(self.pic_input_3_clicked)
        self.pic_input_4.clicked.connect(self.pic_input_4_clicked)
        self.submit.clicked.connect(self.submit_clicked)
        self.start.clicked.connect(self.start_clicked)
        self.shuffle.clicked.connect(self.shuffle_clicked)
        self.show_king.clicked.connect(self.show_king_clicked)
        self.show_minister.clicked.connect(self.show_minister_clicked)
        self.its_thief_1.clicked.connect(self.its_thief_1_clicked)
        self.its_thief_2.clicked.connect(self.its_thief_2_clicked)
        self.its_thief_3.clicked.connect(self.its_thief_3_clicked)
        self.its_thief_4.clicked.connect(self.its_thief_4_clicked)
        self.next.clicked.connect(self.next_clicked)
        self.restart.clicked.connect(self.restart_clicked)

        self.pic_1 = "userpic.png"
        self.pic_2 = "userpic.png"
        self.pic_3 = "userpic.png"
        self.pic_4 = "userpic.png"

        MainWindow.showFullScreen()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "King, Minister, Soldier, Thief"))
        self.groupBox.setTitle(_translate("MainWindow", "King, Minster, Soldier, Thief"))
        self.submit.setShortcut(_translate("MainWindow", "Return"))
        self.start.setShortcut(_translate("MainWindow", "Return"))
        self.shuffle.setShortcut(_translate("MainWindow", "Return"))
        self.show_king.setShortcut(_translate("MainWindow", "Return"))
        self.show_minister.setShortcut(_translate("MainWindow", "Return"))
        self.next.setShortcut(_translate("MainWindow", "Return"))

    def pic_input_1_clicked(self):
        try:
            pic_1_path = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image", "C:\\", "Image Files (*.jpg *.gif)")[0]
            print(pic_1_path)
            im = Image.open(pic_1_path)
            print(im.format, "\n", im.size, "\n", im.mode)
            new_im = im.crop((
                (im.size[0] - min(im.size)) // 2,
                (im.size[1] - min(im.size)) // 2,
                (im.size[0] + min(im.size)) // 2,
                (im.size[1] + min(im.size)) // 2
            ))
            new_im.save("image1.jpg")
            print("Saved Squared Image")
            mask = Image.new("L", new_im.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, new_im.size[0], new_im.size[1]), fill=255)

            pic_1 = new_im.copy()
            pic_1.putalpha(mask)

            pic_1.save("image1.png")
            print("Saved Circled Image")
            self.pic_1 = "image1.png"
            self.pic_input_1.setIcon(QtGui.QIcon(self.pic_1))
            self.pic_input_1.setStyleSheet("border-radius:50px")
            self.pic_1_label.setPixmap(QtGui.QPixmap(self.pic_1))
            self.pic_1_label.setScaledContents(True)
            self.winner_pic.setPixmap(QtGui.QPixmap(self.pic_1))
            self.winner_pic.setScaledContents(True)
        except:
            pass
    
    def pic_input_2_clicked(self):
        try:
            pic_2_path = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image", "C:\\", "Image Files (*.jpg *.gif)")[0]
            im = Image.open(pic_2_path)
            print(im.format, "\n", im.size, "\n", im.mode)
            new_im = im.crop((
                (im.size[0] - min(im.size)) // 2,
                (im.size[1] - min(im.size)) // 2,
                (im.size[0] + min(im.size)) // 2,
                (im.size[1] + min(im.size)) // 2
            ))
            new_im.save("image2.jpg")
            print("Saved Squared Image")
            mask = Image.new("L", new_im.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, new_im.size[0], new_im.size[1]), fill=255)

            pic_2 = new_im.copy()
            pic_2.putalpha(mask)

            pic_2.save("image2.png")
            print("Saved Circled Image")
            self.pic_2 = "image2.png"
            self.pic_input_2.setIcon(QtGui.QIcon(self.pic_2))
            self.pic_input_2.setStyleSheet("border-radius:50px")
            self.pic_2_label.setPixmap(QtGui.QPixmap(self.pic_2))
            self.pic_2_label.setScaledContents(True)
            self.winner_pic.setPixmap(QtGui.QPixmap(self.pic_2))
            self.winner_pic.setScaledContents(True)
        except:
            pass

    def pic_input_3_clicked(self):
        try:
            pic_3_path = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image", "C:\\", "Image Files (*.jpg *.gif)")[0]
            im = Image.open(pic_3_path)
            print(im.format, "\n", im.size, "\n", im.mode)
            new_im = im.crop((
                (im.size[0] - min(im.size)) // 2,
                (im.size[1] - min(im.size)) // 2,
                (im.size[0] + min(im.size)) // 2,
                (im.size[1] + min(im.size)) // 2
            ))
            new_im.save("image3.jpg")
            print("Saved Squared Image")
            mask = Image.new("L", new_im.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, new_im.size[0], new_im.size[1]), fill=255)

            pic_3 = new_im.copy()
            pic_3.putalpha(mask)

            pic_3.save("image3.png")
            print("Saved Circled Image")
            self.pic_3 = "image3.png"
            self.pic_input_3.setIcon(QtGui.QIcon(self.pic_3))
            self.pic_input_3.setStyleSheet("border-radius:50px")
            self.pic_3_label.setPixmap(QtGui.QPixmap(self.pic_3))
            self.pic_3_label.setScaledContents(True)
            self.winner_pic.setPixmap(QtGui.QPixmap(self.pic_3))
            self.winner_pic.setScaledContents(True)
        except:
            pass

    def pic_input_4_clicked(self):
        try:
            pic_4_path = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image", "C:\\", "Image Files (*.jpg *.gif)")[0]
            im = Image.open(pic_4_path)
            print(im.format, "\n", im.size, "\n", im.mode)
            new_im = im.crop((
                (im.size[0] - min(im.size)) // 2,
                (im.size[1] - min(im.size)) // 2,
                (im.size[0] + min(im.size)) // 2,
                (im.size[1] + min(im.size)) // 2
            ))
            new_im.save("image4.jpg")
            print("Saved Squared Image")
            mask = Image.new("L", new_im.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, new_im.size[0], new_im.size[1]), fill=255)

            pic_4 = new_im.copy()
            pic_4.putalpha(mask)

            pic_4.save("image4.png")
            print("Saved Circled Image")
            self.pic_4 = "image4.png"
            self.pic_input_4.setIcon(QtGui.QIcon(self.pic_4))
            self.pic_input_4.setStyleSheet("border-radius:50px")
            self.pic_4_label.setPixmap(QtGui.QPixmap(self.pic_4))
            self.pic_4_label.setScaledContents(True)
            self.winner_pic.setPixmap(QtGui.QPixmap(self.pic_4))
            self.winner_pic.setScaledContents(True)
        except:
            pass

    def submit_clicked(self):
        if self.name_input_1.text() == "":
            self.name1 = "Player 1"
        else:
            self.name1 = self.name_input_1.text()
        
        if self.name_input_2.text() == "":
            self.name2 = "Player 2"
        else:
            self.name2 = self.name_input_2.text()
        
        if self.name_input_3.text() == "":
            self.name3 = "Player 3"
        else:
            self.name3 = self.name_input_3.text()

        if self.name_input_4.text() ==  "":
            self.name4 = "Player 4"
        else:
            self.name4 = self.name_input_4.text()
        
        self.player1.close()
        self.player2.close()
        self.player3.close()
        self.player4.close()
        self.name_input_1.close()
        self.name_input_2.close()
        self.name_input_3.close()
        self.name_input_4.close()
        self.pic_input_1.close()
        self.pic_input_2.close()
        self.pic_input_3.close()
        self.pic_input_4.close()
        
        self.label.setText("Set the Target Score between 2000 and 100000")
        self.label.adjustSize()
        self.label.move(300, 50)
        self.label.setStyleSheet("color:green")
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        self.label.setFont(font)

        self.player_1_name.setText(self.name1)
        self.player_2_name.setText(self.name2)
        self.player_3_name.setText(self.name3)
        self.player_4_name.setText(self.name4)
        self.player_1_name.adjustSize()
        self.player_2_name.adjustSize()
        self.player_3_name.adjustSize()
        self.player_4_name.adjustSize()

        self.submit.close()
        self.target.show()
        self.start.show()
        self.restart.show()

    def start_clicked(self):
        if self.target.text() == "":
            self.target_score = 0
        else:
            self.target_score = int(self.target.text())
        if self.target_score < 2000:
            pass
        else:
            self.label.close()
            self.start.close()
            self.target.close()
            self.player_1_name.show()
            self.player_2_name.show()
            self.player_3_name.show()
            self.player_4_name.show()
            self.score_1.show()
            self.score_2.show()
            self.score_3.show()
            self.score_4.show()
            self.pic_1_label.show()
            self.pic_2_label.show()
            self.pic_3_label.show()
            self.pic_4_label.show()
            self.shuffle.show()

    def shuffle_clicked(self):
        self.lst = ["King", "Minister", "Soldier", "Thief"]
        role_1 = random.choice(self.lst)
        self.lst.remove(role_1)
        role_2 = random.choice(self.lst)
        self.lst.remove(role_2)
        role_3 = random.choice(self.lst)
        self.lst.remove(role_3)
        role_4 = random.choice(self.lst)
        self.lst2 = [role_1, role_2, role_3, role_4]
        self.shuffle.close()
        self.show_king.show()
        print(self.lst2)

    def show_king_clicked(self):
        self.show_king.hide()
        if self.lst2.index("King") == 0:
            self.king = self.name1
            scores = str(int(self.score_1.text().replace("Total Score: ", "")) + 1000)
            self.score_1.setText("Total Score: " + scores)
            self.king_pic_1.show()
            self.you_got_1.setText(f"{self.king} is the King")
            self.you_got_1.show()
        elif self.lst2.index("King") == 1:
            self.king = self.name2
            scores = str(int(self.score_2.text().replace("Total Score: ", "")) + 1000)
            self.score_2.setText("Total Score: " + scores)
            self.king_pic_2.show()
            self.you_got_2.setText(f"{self.king} is the King")
            self.you_got_2.show()
        elif self.lst2.index("King") == 2:
            self.king = self.name3
            scores = str(int(self.score_3.text().replace("Total Score: ", "")) + 1000)
            self.score_3.setText("Total Score: " + scores)
            self.king_pic_3.show()
            self.you_got_3.setText(f"{self.king} is the King")
            self.you_got_3.show()
        elif self.lst2.index("King") == 3:
            self.king = self.name4
            scores = str(int(self.score_4.text().replace("Total Score: ", "")) + 1000)
            self.score_4.setText("Total Score: " + scores)
            self.king_pic_4.show()
            self.you_got_4.setText(f"{self.king} is the King")
            self.you_got_4.show()
        else:
            pass
        self.label1.setText(f"Woo! {self.king} is the King!")
        self.label1.move(450, 280)
        self.label1.show()
        self.label1.adjustSize()
        self.show_minister.show()
        QtTest.QTest.qWait(1)
        playsound("Applause.wav")
        print(f"{self.king} is the King")

    def show_minister_clicked(self):
        self.show_minister.hide()
        if self.lst2.index("Minister") == 0:
            self.minister = self.name1
            self.minister_pic_1.show()
            self.you_got_1.setText(f"{self.minister} is Minister")
            self.you_got_1.show()
        elif self.lst2.index("Minister") == 1:
            self.minister = self.name2
            self.minister_pic_2.show()
            self.you_got_2.setText(f"{self.minister} is Minister")
            self.you_got_2.show()
        elif self.lst2.index("Minister") == 2:
            self.minister = self.name3
            self.minister_pic_3.show()
            self.you_got_3.setText(f"{self.minister} is Minister")
            self.you_got_3.show()
        elif self.lst2.index("Minister") == 3:
            self.minister = self.name4
            self.minister_pic_4.show()
            self.you_got_4.setText(f"{self.minister} is Minister")
            self.you_got_4.show()
        else:
            pass
        self.label1.setText(f'''
        {self.minister} is the Minister.
        Now {self.minister}, find the Thief and the Soldier!
        ''')
        self.label1.adjustSize()
        self.label1.move(220, 230)
        if self.lst2.index("Thief") == 0 or self.lst2.index("Soldier") == 0:
            self.its_thief_1.setText(f"{self.name1} is a Thief")
            self.its_thief_1.adjustSize()
            self.its_thief_1.show()
            self.its_thief_1.setEnabled(True)
        if self.lst2.index("Thief") == 1 or self.lst2.index("Soldier") == 1:
            self.its_thief_2.setText(f"{self.name2} is a Thief")
            self.its_thief_2.adjustSize()
            self.its_thief_2.show()
            self.its_thief_2.setEnabled(True)
        if self.lst2.index("Thief") == 2 or self.lst2.index("Soldier") == 2:
            self.its_thief_3.setText(f"{self.name3} is a Thief")
            self.its_thief_3.adjustSize()
            self.its_thief_3.show()
            self.its_thief_3.setEnabled(True)
        if self.lst2.index("Thief") == 3 or self.lst2.index("Soldier") == 3:
            self.its_thief_4.setText(f"{self.name4} is a Thief")
            self.its_thief_4.adjustSize()
            self.its_thief_4.show()
            self.its_thief_4.setEnabled(True)
        print(f"{self.minister} is the Minister")

    def its_thief_1_clicked(self):
        self.label1.move(250, 280)
        if self.lst2[0] == "Thief":
            self.label1.setText("Great! Correct Choice")
            self.label1.setStyleSheet("color:green")
            minister_index = self.lst2.index("Minister")
            if minister_index == 0:
                scores = int(self.score_1.text().replace("Total Score: ", ""))
                scores += 800
                self.score_1.setText(f"Total Score: {scores}")
            elif minister_index == 1:
                scores = int(self.score_2.text().replace("Total Score: ", ""))
                scores += 800
                self.score_2.setText(f"Total Score: {scores}")
            elif minister_index == 2:
                scores = int(self.score_3.text().replace("Total Score: ", ""))
                scores += 800
                self.score_3.setText(f"Total Score: {scores}")
            elif minister_index == 3:
                scores = int(self.score_4.text().replace("Total Score: ", ""))
                scores += 800
                self.score_4.setText(f"Total Score: {scores}")
            QtTest.QTest.qWait(1)
            playsound("Correct Choice.wav")
        else:
            self.label1.setText("Oops! Wrong Choice")
            self.label1.setStyleSheet("color:red")
            thief_index = self.lst2.index("Thief")
            if thief_index == 0:
                scores = int(self.score_1.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_1.setText(f"Total Score: {scores}")
            elif thief_index == 1:
                scores = int(self.score_2.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_2.setText(f"Total Score: {scores}")
            elif thief_index == 2:
                scores = int(self.score_3.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_3.setText(f"Total Score: {scores}")
            elif thief_index == 3:
                scores = int(self.score_4.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_4.setText(f"Total Score: {scores}")
            QtTest.QTest.qWait(1)
            playsound("buzzer.wav")
        soldier_index = self.lst2.index("Soldier")
        if soldier_index == 0:
            scores = int(self.score_1.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_1.setText(f"Total Score: {scores}")
        elif soldier_index == 1:
            scores = int(self.score_2.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_2.setText(f"Total Score: {scores}")
        elif soldier_index == 2:
            scores = int(self.score_3.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_3.setText(f"Total Score: {scores}")
        elif soldier_index == 3:
            scores = int(self.score_4.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_4.setText(f"Total Score: {scores}")
        self.its_thief_1.hide()
        self.its_thief_2.hide()
        self.its_thief_3.hide()
        self.its_thief_4.hide()
        self.its_thief_1.setEnabled(False)
        self.its_thief_2.setEnabled(False)
        self.its_thief_3.setEnabled(False)
        self.its_thief_4.setEnabled(False)
        self.next.show()
        self.next.setEnabled(True)

    def its_thief_2_clicked(self):
        self.label1.move(250, 280)
        if self.lst2[1] == "Thief":
            self.label1.setText("Great! Correct Choice")
            self.label1.setStyleSheet("color:green")
            minister_index = self.lst2.index("Minister")
            if minister_index == 0:
                scores = int(self.score_1.text().replace("Total Score: ", ""))
                scores += 800
                self.score_1.setText(f"Total Score: {scores}")
            elif minister_index == 1:
                scores = int(self.score_2.text().replace("Total Score: ", ""))
                scores += 800
                self.score_2.setText(f"Total Score: {scores}")
            elif minister_index == 2:
                scores = int(self.score_3.text().replace("Total Score: ", ""))
                scores += 800
                self.score_3.setText(f"Total Score: {scores}")
            elif minister_index == 3:
                scores = int(self.score_4.text().replace("Total Score: ", ""))
                scores += 800
                self.score_4.setText(f"Total Score: {scores}")
            QtTest.QTest.qWait(1)
            playsound("Correct Choice.wav")
        else:
            self.label1.setText("Oops! Wrong Choice")
            self.label1.setStyleSheet("color:red")
            thief_index = self.lst2.index("Thief")
            if thief_index == 0:
                scores = int(self.score_1.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_1.setText(f"Total Score: {scores}")
            elif thief_index == 1:
                scores = int(self.score_2.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_2.setText(f"Total Score: {scores}")
            elif thief_index == 2:
                scores = int(self.score_3.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_3.setText(f"Total Score: {scores}")
            elif thief_index == 3:
                scores = int(self.score_4.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_4.setText(f"Total Score: {scores}")
            QtTest.QTest.qWait(1)
            playsound("buzzer.wav")
        soldier_index = self.lst2.index("Soldier")
        if soldier_index == 0:
            scores = int(self.score_1.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_1.setText(f"Total Score: {scores}")
        elif soldier_index == 1:
            scores = int(self.score_2.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_2.setText(f"Total Score: {scores}")
        elif soldier_index == 2:
            scores = int(self.score_3.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_3.setText(f"Total Score: {scores}")
        elif soldier_index == 3:
            scores = int(self.score_4.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_4.setText(f"Total Score: {scores}")
        self.its_thief_1.hide()
        self.its_thief_2.hide()
        self.its_thief_3.hide()
        self.its_thief_4.hide()
        self.its_thief_1.setEnabled(False)
        self.its_thief_2.setEnabled(False)
        self.its_thief_3.setEnabled(False)
        self.its_thief_4.setEnabled(False)
        self.next.show()
        self.next.setEnabled(True)

    def its_thief_3_clicked(self):
        self.label1.move(250, 280)
        if self.lst2[2] == "Thief":
            self.label1.setText("Great! Correct Choice")
            self.label1.setStyleSheet("color:green")
            minister_index = self.lst2.index("Minister")
            if minister_index == 0:
                scores = int(self.score_1.text().replace("Total Score: ", ""))
                scores += 800
                self.score_1.setText(f"Total Score: {scores}")
            elif minister_index == 1:
                scores = int(self.score_2.text().replace("Total Score: ", ""))
                scores += 800
                self.score_2.setText(f"Total Score: {scores}")
            elif minister_index == 2:
                scores = int(self.score_3.text().replace("Total Score: ", ""))
                scores += 800
                self.score_3.setText(f"Total Score: {scores}")
            elif minister_index == 3:
                scores = int(self.score_4.text().replace("Total Score: ", ""))
                scores += 800
                self.score_4.setText(f"Total Score: {scores}")
            QtTest.QTest.qWait(1)
            playsound("Correct Choice.wav")
        else:
            self.label1.setText("Oops! Wrong Choice")
            self.label1.setStyleSheet("color:red")
            thief_index = self.lst2.index("Thief")
            if thief_index == 0:
                scores = int(self.score_1.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_1.setText(f"Total Score: {scores}")
            elif thief_index == 1:
                scores = int(self.score_2.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_2.setText(f"Total Score: {scores}")
            elif thief_index == 2:
                scores = int(self.score_3.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_3.setText(f"Total Score: {scores}")
            elif thief_index == 3:
                scores = int(self.score_4.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_4.setText(f"Total Score: {scores}")
            QtTest.QTest.qWait(1)
            playsound("buzzer.wav")
        soldier_index = self.lst2.index("Soldier")
        if soldier_index == 0:
            scores = int(self.score_1.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_1.setText(f"Total Score: {scores}")
        elif soldier_index == 1:
            scores = int(self.score_2.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_2.setText(f"Total Score: {scores}")
        elif soldier_index == 2:
            scores = int(self.score_3.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_3.setText(f"Total Score: {scores}")
        elif soldier_index == 3:
            scores = int(self.score_4.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_4.setText(f"Total Score: {scores}")
        self.its_thief_1.hide()
        self.its_thief_2.hide()
        self.its_thief_3.hide()
        self.its_thief_4.hide()
        self.its_thief_1.setEnabled(False)
        self.its_thief_2.setEnabled(False)
        self.its_thief_3.setEnabled(False)
        self.its_thief_4.setEnabled(False)
        self.next.show()
        self.next.setEnabled(True)

    def its_thief_4_clicked(self):
        self.label1.move(250, 280)
        if self.lst2[3] == "Thief":
            self.label1.setText("Great! Correct Choice")
            self.label1.setStyleSheet("color:green")
            minister_index = self.lst2.index("Minister")
            if minister_index == 0:
                scores = int(self.score_1.text().replace("Total Score: ", ""))
                scores += 800
                self.score_1.setText(f"Total Score: {scores}")
            elif minister_index == 1:
                scores = int(self.score_2.text().replace("Total Score: ", ""))
                scores += 800
                self.score_2.setText(f"Total Score: {scores}")
            elif minister_index == 2:
                scores = int(self.score_3.text().replace("Total Score: ", ""))
                scores += 800
                self.score_3.setText(f"Total Score: {scores}")
            elif minister_index == 3:
                scores = int(self.score_4.text().replace("Total Score: ", ""))
                scores += 800
                self.score_4.setText(f"Total Score: {scores}")
            QtTest.QTest.qWait(1)
            playsound("Correct Choice.wav")
        else:
            self.label1.setText("Oops! Wrong Choice")
            self.label1.setStyleSheet("color:red")
            thief_index = self.lst2.index("Thief")
            if thief_index == 0:
                scores = int(self.score_1.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_1.setText(f"Total Score: {scores}")
            elif thief_index == 1:
                scores = int(self.score_2.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_2.setText(f"Total Score: {scores}")
            elif thief_index == 2:
                scores = int(self.score_3.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_3.setText(f"Total Score: {scores}")
            elif thief_index == 3:
                scores = int(self.score_4.text().replace("Total Score: ", ""))
                scores = str(scores + 800)
                self.score_4.setText(f"Total Score: {scores}")
            QtTest.QTest.qWait(1)
            playsound("buzzer.wav")
        soldier_index = self.lst2.index("Soldier")
        if soldier_index == 0:
            scores = int(self.score_1.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_1.setText(f"Total Score: {scores}")
        elif soldier_index == 1:
            scores = int(self.score_2.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_2.setText(f"Total Score: {scores}")
        elif soldier_index == 2:
            scores = int(self.score_3.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_3.setText(f"Total Score: {scores}")
        elif soldier_index == 3:
            scores = int(self.score_4.text().replace("Total Score: ", ""))
            scores = str(scores + 500)
            self.score_4.setText(f"Total Score: {scores}")
        self.its_thief_1.hide()
        self.its_thief_2.hide()
        self.its_thief_3.hide()
        self.its_thief_4.hide()
        self.its_thief_1.setEnabled(False)
        self.its_thief_2.setEnabled(False)
        self.its_thief_3.setEnabled(False)
        self.its_thief_4.setEnabled(False)
        self.next.show()
        self.next.setEnabled(True)

    def next_clicked(self):
        self.shuffle.setText("Shuffle Again")
        self.shuffle.adjustSize()
        self.shuffle.setShortcut("Return")
        self.shuffle.show()
        self.next.hide()
        self.next.setEnabled(False)
        self.king_pic_1.hide()
        self.king_pic_2.hide()
        self.king_pic_3.hide()
        self.king_pic_4.hide()
        self.minister_pic_1.hide()
        self.minister_pic_2.hide()
        self.minister_pic_3.hide()
        self.minister_pic_4.hide()
        self.you_got_1.close()
        self.you_got_2.close()
        self.you_got_3.close()
        self.you_got_4.close()
        self.label1.setText("")
        score1 = int(self.score_1.text().replace("Total Score: ", ""))
        score2 = int(self.score_2.text().replace("Total Score: ", ""))
        score3 = int(self.score_3.text().replace("Total Score: ", ""))
        score4 = int(self.score_4.text().replace("Total Score: ", ""))
        winner_num = 0
        for i in [score1, score2, score3, score4]:
            if self.target_score <= i:
                winner_num += 1
        if winner_num < 1:
            self.winner = ""
        if winner_num == 1:
            if score1 >= self.target_score:
                self.winner = self.name1
            elif score2 >= self.target_score:
                self.winner = self.name2
            elif score3 >= self.target_score:
                self.winner = self.name3
            elif score4 >= self.target_score:
                self.winner = self.name4
            else:
                self.winner = ""
        elif winner_num > 1:
            max_score = max([score1, score2, score3, score4])
            if max_score == score1:
                self.winner = self.name1
            elif max_score == score2:
                self.winner = self.name2
            elif max_score == score3:
                self.winner = self.name3
            elif max_score == score4:
                self.winner = self.name4
            else:
                self.winner = ""

        if self.winner == self.name1 or self.winner == self.name2 or self.winner == self.name3 or self.winner == self.name4:
            self.player_1_name.close()
            self.player_2_name.close()
            self.player_3_name.close()
            self.player_4_name.close()
            self.score_1.close()
            self.score_2.close()
            self.score_3.close()
            self.score_4.close()
            self.pic_1_label.close()
            self.pic_2_label.close()
            self.pic_3_label.close()
            self.pic_4_label.close()
            self.shuffle.close()

            self.winner_pic.setStyleSheet("border-radius:300px")
            if self.winner == self.name1:
                self.winner_pic.setPixmap(QtGui.QPixmap(self.pic_1))
                self.winner_pic.setScaledContents(True)
            elif self.winner == self.name2:
                self.winner_pic.setPixmap(QtGui.QPixmap(self.pic_2))
                self.winner_pic.setScaledContents(True)
            elif self.winner == self.name3:
                self.winner_pic.setPixmap(QtGui.QPixmap(self.pic_3))
                self.winner_pic.setScaledContents(True)
            elif self.winner == self.name4:
                self.winner_pic.setPixmap(QtGui.QPixmap(self.pic_4))
                self.winner_pic.setScaledContents(True)
            
            # self.restart.show()
            self.winner_pic.show()
            self.win_label.setText(f"Woo! {self.winner} is the Winner!")
            self.win_label.adjustSize()
            self.win_label.show()
            QtTest.QTest.qWait(1)
            playsound("Winning Sound.wav")

    def restart_clicked(self):
        self.restart.close()
        self.winner_pic.close()
        self.win_label.close()
        self.player1.show()
        self.player2.show()
        self.player3.show()
        self.player4.show()
        self.name_input_1.show()
        self.name_input_2.show()
        self.name_input_3.show()
        self.name_input_4.show()
        self.name_input_1.setText(self.name1)
        self.name_input_2.setText(self.name1)
        self.name_input_3.setText(self.name1)
        self.name_input_4.setText(self.name1)
        self.submit.show()
        self.label.move(470, 50)
        self.label.setStyleSheet("color:blue")
        self.label.setText("Set the Player\'s Name")
        self.label.show()
        self.target.close()
        self.start.close()
        self.player_1_name.close()
        self.player_2_name.close()
        self.player_3_name.close()
        self.player_4_name.close()
        self.score_1.close()
        self.score_2.close()
        self.score_3.close()
        self.score_4.close()
        self.shuffle.close()
        self.show_king.close()
        self.show_minister.close()
        self.pic_input_1.show()
        self.pic_input_2.show()
        self.pic_input_3.show()
        self.pic_input_4.show()
        self.king_pic_1.close()
        self.king_pic_2.close()
        self.king_pic_3.close()
        self.king_pic_4.close()
        self.you_got_1.close()
        self.you_got_2.close()
        self.you_got_3.close()
        self.you_got_4.close()
        self.pic_1_label.close()
        self.pic_2_label.close()
        self.pic_3_label.close()
        self.pic_4_label.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

