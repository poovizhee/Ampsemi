# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start_up_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_start_up(object):
    def setupUi(self, start_up):
        start_up.setObjectName("start_up")
        start_up.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(start_up)
        self.centralwidget.setObjectName("centralwidget")
        self.label_BG_img = QtWidgets.QLabel(self.centralwidget)
        self.label_BG_img.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_BG_img.setFont(font)
        self.label_BG_img.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_BG_img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_BG_img.setAutoFillBackground(False)
        self.label_BG_img.setStyleSheet("background-image: url(C:/Users/MukeshChaudhary/PycharmProjects/pythonProject/GUI_IMAGE/BGstart1.png);")
        self.label_BG_img.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_BG_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_BG_img.setLineWidth(100)
        self.label_BG_img.setText("")
        self.label_BG_img.setPixmap(QtGui.QPixmap("C:/Users/MukeshChaudhary/PycharmProjects/pythonProject/GUI_IMAGE/BGstart1.png"))
        self.label_BG_img.setScaledContents(True)
        self.label_BG_img.setWordWrap(False)
        self.label_BG_img.setIndent(-1)
        self.label_BG_img.setObjectName("label_BG_img")
        self.device_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.device_combo_box.setGeometry(QtCore.QRect(860, 540, 171, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.device_combo_box.setFont(font)
        self.device_combo_box.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background-color: rgb(6, 63, 112);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold\n"
"\n"
"")
        self.device_combo_box.setObjectName("device_combo_box")
        self.device_combo_box.addItem("")
        self.device_combo_box.addItem("")
        self.device_combo_box.addItem("")
        self.device_combo_box.addItem("")
        self.device_combo_box.addItem("")
        self.label_amp_text = QtWidgets.QLabel(self.centralwidget)
        self.label_amp_text.setGeometry(QtCore.QRect(310, 10, 851, 171))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        self.label_amp_text.setFont(font)
        self.label_amp_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_amp_text.setObjectName("label_amp_text")
        self.label_AMP_LOGO = QtWidgets.QLabel(self.centralwidget)
        self.label_AMP_LOGO.setGeometry(QtCore.QRect(110, 30, 181, 121))
        self.label_AMP_LOGO.setText("")
        self.label_AMP_LOGO.setPixmap(QtGui.QPixmap("C:/Users/MukeshChaudhary/PycharmProjects/pythonProject/GUI_IMAGE/LOGO.png"))
        self.label_AMP_LOGO.setScaledContents(True)
        self.label_AMP_LOGO.setObjectName("label_AMP_LOGO")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 240, 721, 461))
        self.label.setStyleSheet("image: url(C:/Users/MukeshChaudhary/PycharmProjects/pythonProject/GUI_IMAGE/chip_prog_logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_proceed = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_proceed.setGeometry(QtCore.QRect(1050, 550, 50, 25))
        self.pushButton_proceed.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;\n"
"\n"
"border-image: url(C:/Users/MukeshChaudhary/PycharmProjects/pythonProject/GUI_IMAGE/proceed.png);\n"
"}\n"
"QPushButton::hover {\n"
"background-color:lightgreen;\n"
"}")
        self.pushButton_proceed.setText("")
        self.pushButton_proceed.setObjectName("pushButton_proceed")
        self.label_ver = QtWidgets.QLabel(self.centralwidget)
        self.label_ver.setGeometry(QtCore.QRect(580, 700, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ver.setFont(font)
        self.label_ver.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ver.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_ver.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ver.setObjectName("label_ver")
        self.label_BG_img.raise_()
        self.label_amp_text.raise_()
        self.label_AMP_LOGO.raise_()
        self.label.raise_()
        self.device_combo_box.raise_()
        self.pushButton_proceed.raise_()
        self.label_ver.raise_()
        start_up.setCentralWidget(self.centralwidget)

        self.retranslateUi(start_up)
        QtCore.QMetaObject.connectSlotsByName(start_up)

    def retranslateUi(self, start_up):
        _translate = QtCore.QCoreApplication.translate
        start_up.setWindowTitle(_translate("start_up", "Welcome to MTP programming"))
        self.device_combo_box.setItemText(0, _translate("start_up", "Select Device"))
        self.device_combo_box.setItemText(1, _translate("start_up", "AMP4592"))
        self.device_combo_box.setItemText(2, _translate("start_up", "AMP4291"))
        self.device_combo_box.setItemText(3, _translate("start_up", "AMP4692"))
        self.device_combo_box.setItemText(4, _translate("start_up", "AMP4792"))
        self.label_amp_text.setText(_translate("start_up", "Advanced Monolithic Power \n"
"         Semiconductor"))
        self.label_ver.setText(_translate("start_up", "Version: 0.86"))

