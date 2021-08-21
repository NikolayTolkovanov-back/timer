from PyQt5 import QtCore, QtGui, QtWidgets
from main import MainUi
import os, sys

class StartUi(QtWidgets.QWidget):
    # Добавление картинок в exe
    def resource_path(self, relative):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative)
        else:
            return os.path.join(os.path.abspath("."), relative)
        
    def setupUi(self, mainUi, Form):
        self.mainUi = mainUi

        self.st_hours = self.st_minuts = self.st_seconds = 0

        Form.setObjectName("Form")
        Form.resize(800, 500)
        Form.setWindowFlags(
        QtCore.Qt.Window |
        QtCore.Qt.WindowMinimizeButtonHint |
        QtCore.Qt.WindowCloseButtonHint
        )
        
        icon = QtGui.QIcon()
        icon.addFile(self.resource_path("assets/icons/apple16.png"), QtCore.QSize(16,16))
        icon.addFile(self.resource_path("assets/icons/apple24.png"), QtCore.QSize(24,24))
        icon.addFile(self.resource_path("assets/icons/apple32.png"), QtCore.QSize(32,32))
        icon.addFile(self.resource_path("assets/icons/apple64.png"), QtCore.QSize(64,64))
        icon.addFile(self.resource_path("assets/icons/apple128.png"), QtCore.QSize(128,128)) 
        icon.addFile(self.resource_path("assets/icons/apple256.png"), QtCore.QSize(256,256))
        Form.setWindowIcon(icon)

        self.text_head = QtWidgets.QLabel(Form)
        self.text_head.setGeometry(QtCore.QRect(0, 20, 801, 120))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.text_head.setFont(font)
        self.text_head.setStyleSheet("")
        self.text_head.setTextFormat(QtCore.Qt.AutoText)
        self.text_head.setScaledContents(False)
        self.text_head.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.text_head.setWordWrap(True)
        self.text_head.setIndent(0)
        self.text_head.setObjectName("text_head")

        self.bg = QtWidgets.QLabel(Form)
        self.bg.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.bg.setAcceptDrops(False)
        self.bg.setStyleSheet("")
        self.bg.setMidLineWidth(0)
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap(self.resource_path("assets/img/start_bg.jpg")))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        
        self.spin_hours = QtWidgets.QSpinBox(Form)
        self.spin_hours.setGeometry(QtCore.QRect(270, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spin_hours.setFont(font)
        self.spin_hours.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spin_hours.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spin_hours.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.spin_hours.setStyleSheet("border: none;border-radius: 3px; background: black; color: green;padding-left: 5px;selection-background-color: rgba(0, 0, 0, 0%);selection-color: green ")
        self.spin_hours.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_hours.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spin_hours.setAccelerated(True)
        self.spin_hours.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spin_hours.setProperty("showGroupSeparator", False)
        self.spin_hours.setMaximum(9999)
        self.spin_hours.valueChanged.connect(self.change_hours)
        self.spin_hours.setObjectName("spin_hours")
        
        self.spin_minuts = QtWidgets.QSpinBox(Form)
        self.spin_minuts.setGeometry(QtCore.QRect(370, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spin_minuts.setFont(font)
        self.spin_minuts.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spin_minuts.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.spin_minuts.setStyleSheet("border: none;border-radius: 3px; background: black; color: green;padding-left: 5px;selection-background-color: rgba(0, 0, 0, 0%);selection-color: green ")
        self.spin_minuts.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_minuts.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spin_minuts.setAccelerated(True)
        self.spin_minuts.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spin_minuts.setProperty("showGroupSeparator", False)
        self.spin_minuts.setMaximum(59)
        self.spin_minuts.valueChanged.connect(self.change_minuts)
        self.spin_minuts.setObjectName("spin_minuts")
        
        self.spin_seconds = QtWidgets.QSpinBox(Form)
        self.spin_seconds.setGeometry(QtCore.QRect(470, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spin_seconds.setFont(font)
        self.spin_seconds.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spin_seconds.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.spin_seconds.setStyleSheet("border: none;border-radius: 3px; background: black; color: green;padding-left: 5px;selection-background-color: rgba(0, 0, 0, 0%);selection-color: green ")
        self.spin_seconds.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_seconds.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spin_seconds.setAccelerated(True)
        self.spin_seconds.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spin_seconds.setProperty("showGroupSeparator", False)
        self.spin_seconds.setMaximum(59)
        self.spin_seconds.valueChanged.connect(self.change_seconds)
        self.spin_seconds.setObjectName("spin_seconds")
        
        self.text_time = QtWidgets.QLabel(Form)
        self.text_time.setGeometry(QtCore.QRect(80, 240, 661, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.text_time.setFont(font)
        self.text_time.setStyleSheet("")
        self.text_time.setTextFormat(QtCore.Qt.AutoText)
        self.text_time.setScaledContents(False)
        self.text_time.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.text_time.setWordWrap(True)
        self.text_time.setIndent(0)
        self.text_time.setObjectName("text_time")

        self.btn_send = QtWidgets.QPushButton(Form)
        self.btn_send.setEnabled(True)
        self.btn_send.setGeometry(QtCore.QRect(350, 360, 131, 41))
        self.btn_send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_send.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_send.clicked.connect(self.create_file)
        self.btn_send.clicked.connect(self.change_ui)
        


        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.btn_send.setFont(font)
        self.btn_send.setStyleSheet("QPushButton {\n"
        "    background-color:  black;\n"
        "    border: none;\n"
        "    color: rgb(0, 255, 0);\n"
        "    border-radius: 1px;\n"
        "}\n"
        "\n"
        "QPushButton::hover {\n"
        "    background-color: rgb(0, 85, 255);\n"
        "    color: white;\n"
        "}")
        self.btn_send.setObjectName("btn_send")

        self.bg.raise_()
        self.text_head.raise_()
        self.spin_hours.raise_()
        self.spin_minuts.raise_()
        self.spin_seconds.raise_()
        self.text_time.raise_()
        self.btn_send.raise_()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Таймер Чемпиона"))
        self.text_head.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#000000;\">Добро пожаловать в<br> </span><span style=\" font-size:36pt; color:#ffffff;\">Таймер Чемпиона!</span></p></body></html>"))
        self.text_time.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#00ff00;\">Укажите время :</span></p></body></html>"))
        self.btn_send.setText(_translate("Form", "ОК"))

    def change_ui(self):
        self.mainUi.setupUi(Form)

    def change_hours(self):
        self.st_hours = self.spin_hours.value()

    def change_minuts(self):
        self.st_minuts = self.spin_minuts.value()

    def change_seconds(self):
        self.st_seconds = self.spin_seconds.value()

    def create_file(self):
        self.file_name = 'time.txt' 
        self.path = os.getcwd() + f'\\{self.file_name}' # путь до файла

        if os.path.exists(self.path) != True:
            with open(self.file_name, 'w') as file:
                file.writelines(f'{self.st_hours}\n')
                file.writelines(f'{self.st_minuts}\n')
                file.writelines(f'{self.st_seconds}\n')
                file.close()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()

    startUi = StartUi()
    mainUi = MainUi()

    file_name = 'time.txt'
    path = os.getcwd() + f'\\{file_name}'
    if os.path.exists(path) != True:
        startUi.setupUi(mainUi, Form)
    else:
        mainUi.setupUi(Form)

    Form.show()

    sys.exit(app.exec_())

