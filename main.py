# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys

class MainUi(QtWidgets.QWidget):

    def resource_path(self, relative):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative)
        else:
            return os.path.join(os.path.abspath("."), relative)
      
    # Создаие объектов
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 500)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.change_time)

        MainWindow.setWindowTitle("Таймер Чемпиона")
        icon = QtGui.QIcon()
        icon.addFile(self.resource_path("assets/icons/apple16.png"), QtCore.QSize(16,16))
        icon.addFile(self.resource_path("assets/icons/apple24.png"), QtCore.QSize(24,24))
        icon.addFile(self.resource_path("assets/icons/apple32.png"), QtCore.QSize(32,32))
        icon.addFile(self.resource_path("assets/icons/apple64.png"), QtCore.QSize(64,64))
        icon.addFile(self.resource_path("assets/icons/apple128.png"), QtCore.QSize(128,128))
        icon.addFile(self.resource_path("assets/icons/apple256.png"), QtCore.QSize(256,256))

        MainWindow.setWindowIcon(icon)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 811, 511))
        self.background.setPixmap(QtGui.QPixmap(self.resource_path("assets/img/main_bg.jpg")))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")

        self.timer_border = QtWidgets.QLabel(self.centralwidget)
        self.timer_border.setGeometry(QtCore.QRect(0, 170, 801, 130))
        self.timer_border.setStyleSheet("background-color: rgba(255, 255, 255,0.5);\n")
        self.timer_border.setObjectName("timer_border")

        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(0, 100, 800, 42))
        self.label_header.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_header.setText("Времени осталось:")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setStyleSheet("color: black; text-align: center; font-size: 40px; background: transparent;")
        self.label_header.setObjectName("label_header")

        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(0,140,800,200)
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.timer_label.setFont(font)
        self.timer_label.setStyleSheet("background: transparent;color: black;")
        self.timer_label.setObjectName("timer_label")


        self.Button_start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_start.setGeometry(QtCore.QRect(130, 380, 171, 51))
        self.Button_start.setText("СТАРТ")
        self.Button_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_start.clicked.connect(self.start_action)
        self.Button_start.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(0, 255, 255);\n"
        "    font-family: \"MS Shell Dlg 2\" ;\n"
        "    font-size: 16px;\n"
        "    font-weight: bold;\n"
        "    border: 2px solid transparent;\n"
        "    border-radius: 3px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: #ffffff;\n"
        "    \n"
        "}"
        "\n"
        "QPushButton:pressed {"
        "    color: red;\n"
        "}")
        self.Button_start.setObjectName("Button_start")

        self.Button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.Button_stop.setGeometry(QtCore.QRect(530, 380, 161, 51))
        self.Button_stop.setText("СТОП")
        self.Button_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_stop.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Button_stop.clicked.connect(self.stop_action)
        self.Button_stop.clicked.connect(self.rewrite_data)
        self.Button_stop.setStyleSheet(
        "QPushButton {\n"
        "    background-color: rgb(245, 0, 4);\n"
        "    font-family: \"MS Shell Dlg 2\" ;\n"
        "    font-size: 16px;\n"
        "    font-weight: bold;\n"
        "    border: 2px solid transparent;\n"
        "    border-radius: 3px;\n"
        "}\n"
        "\n"

        "QPushButton:hover {\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    color: #ffffff;\n"
        "}"
        "\n"
        "QPushButton:pressed {"
        "    color: red;\n"
        "}")
        self.Button_stop.setObjectName("Button_stop")


        self.Button_stop.raise_()
        self.Button_start.raise_()
        self.timer_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.get_data()
        self.start_label()
    # Начальное отображение таймера    
    def start_label(self):
        self.new_hours = self.hours
        self.new_minuts = self.minuts
        self.new_seconds = self.seconds

        if self.new_hours < 10:
            self.new_hours = f'0{self.hours}'

        if self.new_minuts < 10:
            self.new_minuts = f'0{self.minuts}'

        if self.new_seconds < 10:
            self.new_seconds = f'0{self.seconds}'

        self.timer_label.setText(f'{self.new_hours}:{self.new_minuts}:{self.new_seconds}')
    # Получение данных из файла
    def get_data(self):
        with open('time.txt', 'r') as file: 
            self.time_list = file.readlines() # отправка строк из файла в массив
            self.hours = int(self.time_list[0])
            self.minuts = int(self.time_list[1])
            self.seconds = int(self.time_list[2])
            file.close()
    # Изменение времени и отображение таймера 
    def change_time(self):
        
        self.new_hours = self.hours
        self.new_minuts = self.minuts
        self.new_seconds = self.seconds

        if self.new_hours < 10:
            self.new_hours = f'0{self.hours}'

        if self.new_minuts < 10:
            self.new_minuts = f'0{self.minuts}'
            
        if self.new_seconds < 10:
            self.new_seconds = f'0{self.seconds}'
            
        self.timer_label.setText(f'{self.new_hours}:{self.new_minuts}:{self.new_seconds}')
        
        if self.hours == 0 and self.minuts == 0 and self.seconds == 0:
            self.end_timer()
         
        if self.minuts == 0 and self.seconds == 0:
            self.hours -= 1
            if self.minuts == 0:
                self.minuts = 60

        if self.seconds == 0:
            self.seconds = 60               
            self.minuts -= 1

        if self.seconds == 60:
            self.new_seconds = "00"
        if self.minuts == 60:
            self.new_minuts = "00"
        if self.hours == 60:
            self.new_hours = "00"

        self.seconds -= 1
    # Флаг остановки таймера
    def stop_action(self):
        self.timer.stop()
        self.Button_start.setEnabled(True)
        self.Button_stop.setEnabled(False)
    # Флаг запуска таймера
    def start_action(self):
        self.timer.start(1000)
        self.Button_start.setEnabled(False)
        self.Button_stop.setEnabled(True)
    # Окончание времени
    def end_timer(self):
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.timer_label.setFont(font)
        self.timer_label.setText('Поздравляю! Ты перешел на следующий уровень!')
        self.label_header.setText(" ")
        self.timer.stop()
        self.Button_start.setEnabled(False)
        self.Button_stop.setEnabled(False)
    # Перезапись времени в файле
    def rewrite_data(self):
        with open('time.txt', 'w') as file:
            file.writelines(f'{self.hours}\n')
            file.writelines(f'{self.minuts}\n')
            file.writelines(f'{self.seconds}\n')
            file.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainUi = MainUi()
    MainUi.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())