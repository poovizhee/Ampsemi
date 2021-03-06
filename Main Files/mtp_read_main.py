# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mtp_read.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reading_Device_Registers(object):
    def setupUi(self, Reading_Device_Registers):
        Reading_Device_Registers.setObjectName("Reading_Device_Registers")
        Reading_Device_Registers.resize(680, 330)
        self.centralwidget = QtWidgets.QWidget(Reading_Device_Registers)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("background-color: rgb(4, 38, 102);\n"
"color: rgb(255, 230, 35);\n"
"border-radius: 20px;\n"
"\n"
"")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_device = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_device.setGeometry(QtCore.QRect(150, 30, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label_device.setFont(font)
        self.label_device.setStyleSheet("color: rgb(133, 124, 255);\n"
"")
        self.label_device.setAlignment(QtCore.Qt.AlignCenter)
        self.label_device.setObjectName("label_device")
        self.label_description = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QtCore.QRect(130, 110, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(70, 200, 531, 21))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"border-style: none;\n"
"border-radius: 10px;\n"
"background-color:rgb(98,114,164);\n"
"color: rgb(200,200,200);\n"
"\n"
"\n"
"text-align:center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:0.977273, y2:0.517, stop:0.301136 rgba(220, 51, 97, 255), stop:0.886364 rgba(120, 205, 120, 255));\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_progressbar_text = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_progressbar_text.setGeometry(QtCore.QRect(0, 230, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_progressbar_text.setFont(font)
        self.label_progressbar_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_progressbar_text.setObjectName("label_progressbar_text")
        self.label = QtWidgets.QLabel(self.dropShadowFrame)
        self.label.setGeometry(QtCore.QRect(40, 10, 141, 111))
        self.label.setStyleSheet("image: url(GUI_IMAGE/mtp_read2.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("GUI_IMAGE/mtp_read2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_device.raise_()
        self.progressBar.raise_()
        self.label_progressbar_text.raise_()
        self.label_description.raise_()
        self.label.raise_()
        self.verticalLayout.addWidget(self.dropShadowFrame)
        Reading_Device_Registers.setCentralWidget(self.centralwidget)

        self.retranslateUi(Reading_Device_Registers)
        QtCore.QMetaObject.connectSlotsByName(Reading_Device_Registers)

    def retranslateUi(self, Reading_Device_Registers):
        _translate = QtCore.QCoreApplication.translate
        Reading_Device_Registers.setWindowTitle(_translate("Reading_Device_Registers", "Reading MTP"))
        self.label_device.setText(_translate("Reading_Device_Registers", "AMP 4592"))
        self.label_description.setText(_translate("Reading_Device_Registers", "Please Wait ! Device registers are being read."))
        self.label_progressbar_text.setText(_translate("Reading_Device_Registers", "Reading..."))

