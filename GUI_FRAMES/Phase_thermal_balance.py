# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Phase_thermal_balance.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Phase_thermal_balance(object):
    def setupUi(self, Phase_thermal_balance):
        Phase_thermal_balance.setObjectName("Phase_thermal_balance")
        Phase_thermal_balance.resize(479, 621)
        self.centralwidget = QtWidgets.QWidget(Phase_thermal_balance)
        self.centralwidget.setObjectName("centralwidget")
        self.label_main_Phase_thermal_balance = QtWidgets.QLabel(self.centralwidget)
        self.label_main_Phase_thermal_balance.setGeometry(QtCore.QRect(10, 0, 461, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_main_Phase_thermal_balance.setFont(font)
        self.label_main_Phase_thermal_balance.setStyleSheet("background-color: rgb(38, 23, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_main_Phase_thermal_balance.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main_Phase_thermal_balance.setObjectName("label_main_Phase_thermal_balance")
        self.frame_phase_display = QtWidgets.QFrame(self.centralwidget)
        self.frame_phase_display.setGeometry(QtCore.QRect(10, 40, 461, 571))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_phase_display.setFont(font)
        self.frame_phase_display.setStyleSheet("\n"
"border: 2px solid darkorange;\n"
"border-radius:0px;\n"
"")
        self.frame_phase_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_phase_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_phase_display.setObjectName("frame_phase_display")
        self.pushButton_Discard = QtWidgets.QPushButton(self.frame_phase_display)
        self.pushButton_Discard.setGeometry(QtCore.QRect(90, 520, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Discard.setFont(font)
        self.pushButton_Discard.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_Discard.setStyleSheet("QPushButton{background-color: rgb(219, 100, 17);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid red;\n"
"background-color: orange;\n"
"}\n"
"")
        self.pushButton_Discard.setObjectName("pushButton_Discard")
        self.pushButton_Save = QtWidgets.QPushButton(self.frame_phase_display)
        self.pushButton_Save.setGeometry(QtCore.QRect(260, 520, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Save.setFont(font)
        self.pushButton_Save.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_Save.setStyleSheet("QPushButton{background-color: rgb(0, 153, 74);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid green;\n"
"background-color:lightgreen;\n"
"}\n"
"")
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.comboBox_thermal_offset1 = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_thermal_offset1.setGeometry(QtCore.QRect(300, 70, 80, 25))
        self.comboBox_thermal_offset1.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_thermal_offset1.setObjectName("comboBox_thermal_offset1")
        self.comboBox_thermal_offset1.addItem("")
        self.comboBox_thermal_offset1.addItem("")
        self.comboBox_thermal_offset1.addItem("")
        self.comboBox_thermal_offset1.addItem("")
        self.comboBox_thermal_offset1.addItem("")
        self.comboBox_thermal_offset1.addItem("")
        self.comboBox_thermal_offset1.addItem("")
        self.comboBox_thermal_offset1.addItem("")
        self.comboBox_freq_switch_RailA = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_freq_switch_RailA.setGeometry(QtCore.QRect(110, 460, 90, 25))
        self.comboBox_freq_switch_RailA.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_freq_switch_RailA.setObjectName("comboBox_freq_switch_RailA")
        self.comboBox_freq_switch_RailA.addItem("")
        self.comboBox_freq_switch_RailA.addItem("")
        self.comboBox_freq_switch_RailA.addItem("")
        self.comboBox_freq_switch_RailA.addItem("")
        self.label_display_RailB = QtWidgets.QLabel(self.frame_phase_display)
        self.label_display_RailB.setGeometry(QtCore.QRect(230, 420, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_display_RailB.setFont(font)
        self.label_display_RailB.setStyleSheet("border: none;")
        self.label_display_RailB.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_display_RailB.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display_RailB.setObjectName("label_display_RailB")
        self.label_display_RailA = QtWidgets.QLabel(self.frame_phase_display)
        self.label_display_RailA.setGeometry(QtCore.QRect(110, 420, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_display_RailA.setFont(font)
        self.label_display_RailA.setStyleSheet("border: none;")
        self.label_display_RailA.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_display_RailA.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display_RailA.setObjectName("label_display_RailA")
        self.label_RailA_7 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_7.setGeometry(QtCore.QRect(110, 20, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_RailA_7.setFont(font)
        self.label_RailA_7.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_7.setObjectName("label_RailA_7")
        self.label_RailA_18 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_18.setGeometry(QtCore.QRect(210, 70, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_18.setFont(font)
        self.label_RailA_18.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RailA_18.setObjectName("label_RailA_18")
        self.label_RailA_8 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_8.setGeometry(QtCore.QRect(60, 70, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_8.setFont(font)
        self.label_RailA_8.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_8.setObjectName("label_RailA_8")
        self.label_RailA_22 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_22.setGeometry(QtCore.QRect(60, 360, 321, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_RailA_22.setFont(font)
        self.label_RailA_22.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_22.setObjectName("label_RailA_22")
        self.comboBox_freq_switch_RailB = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_freq_switch_RailB.setGeometry(QtCore.QRect(240, 460, 90, 25))
        self.comboBox_freq_switch_RailB.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_freq_switch_RailB.setObjectName("comboBox_freq_switch_RailB")
        self.comboBox_freq_switch_RailB.addItem("")
        self.comboBox_freq_switch_RailB.addItem("")
        self.comboBox_freq_switch_RailB.addItem("")
        self.comboBox_freq_switch_RailB.addItem("")
        self.label_RailA_9 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_9.setGeometry(QtCore.QRect(60, 100, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_9.setFont(font)
        self.label_RailA_9.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_9.setObjectName("label_RailA_9")
        self.label_RailA_19 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_19.setGeometry(QtCore.QRect(210, 100, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_19.setFont(font)
        self.label_RailA_19.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RailA_19.setObjectName("label_RailA_19")
        self.label_RailA_10 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_10.setGeometry(QtCore.QRect(60, 130, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_10.setFont(font)
        self.label_RailA_10.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_10.setObjectName("label_RailA_10")
        self.label_RailA_20 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_20.setGeometry(QtCore.QRect(210, 130, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_20.setFont(font)
        self.label_RailA_20.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RailA_20.setObjectName("label_RailA_20")
        self.label_RailA_11 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_11.setGeometry(QtCore.QRect(60, 160, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_11.setFont(font)
        self.label_RailA_11.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_11.setObjectName("label_RailA_11")
        self.label_RailA_21 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_21.setGeometry(QtCore.QRect(210, 160, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_21.setFont(font)
        self.label_RailA_21.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RailA_21.setObjectName("label_RailA_21")
        self.label_RailA_12 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_12.setGeometry(QtCore.QRect(60, 190, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_12.setFont(font)
        self.label_RailA_12.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_12.setObjectName("label_RailA_12")
        self.label_RailA_23 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_23.setGeometry(QtCore.QRect(210, 190, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_23.setFont(font)
        self.label_RailA_23.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RailA_23.setObjectName("label_RailA_23")
        self.label_RailA_13 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_13.setGeometry(QtCore.QRect(60, 220, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_13.setFont(font)
        self.label_RailA_13.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_13.setObjectName("label_RailA_13")
        self.label_RailA_24 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_24.setGeometry(QtCore.QRect(210, 220, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_24.setFont(font)
        self.label_RailA_24.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RailA_24.setObjectName("label_RailA_24")
        self.label_RailA_14 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_14.setGeometry(QtCore.QRect(60, 250, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_14.setFont(font)
        self.label_RailA_14.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_14.setObjectName("label_RailA_14")
        self.label_RailA_25 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_25.setGeometry(QtCore.QRect(210, 250, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_25.setFont(font)
        self.label_RailA_25.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RailA_25.setObjectName("label_RailA_25")
        self.label_RailA_15 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_15.setGeometry(QtCore.QRect(60, 280, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_15.setFont(font)
        self.label_RailA_15.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_15.setObjectName("label_RailA_15")
        self.label_RailA_26 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_26.setGeometry(QtCore.QRect(210, 280, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_26.setFont(font)
        self.label_RailA_26.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RailA_26.setObjectName("label_RailA_26")
        self.label_RailA_45 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_45.setGeometry(QtCore.QRect(60, 310, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_45.setFont(font)
        self.label_RailA_45.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_45.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_RailA_45.setObjectName("label_RailA_45")
        self.label_RailA_46 = QtWidgets.QLabel(self.frame_phase_display)
        self.label_RailA_46.setGeometry(QtCore.QRect(210, 310, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_RailA_46.setFont(font)
        self.label_RailA_46.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.label_RailA_46.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_RailA_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RailA_46.setObjectName("label_RailA_46")
        self.comboBox_thermal_offset2 = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_thermal_offset2.setGeometry(QtCore.QRect(300, 100, 80, 25))
        self.comboBox_thermal_offset2.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_thermal_offset2.setObjectName("comboBox_thermal_offset2")
        self.comboBox_thermal_offset2.addItem("")
        self.comboBox_thermal_offset2.addItem("")
        self.comboBox_thermal_offset2.addItem("")
        self.comboBox_thermal_offset2.addItem("")
        self.comboBox_thermal_offset2.addItem("")
        self.comboBox_thermal_offset2.addItem("")
        self.comboBox_thermal_offset2.addItem("")
        self.comboBox_thermal_offset2.addItem("")
        self.comboBox_thermal_offset3 = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_thermal_offset3.setGeometry(QtCore.QRect(300, 130, 80, 25))
        self.comboBox_thermal_offset3.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_thermal_offset3.setObjectName("comboBox_thermal_offset3")
        self.comboBox_thermal_offset3.addItem("")
        self.comboBox_thermal_offset3.addItem("")
        self.comboBox_thermal_offset3.addItem("")
        self.comboBox_thermal_offset3.addItem("")
        self.comboBox_thermal_offset3.addItem("")
        self.comboBox_thermal_offset3.addItem("")
        self.comboBox_thermal_offset3.addItem("")
        self.comboBox_thermal_offset3.addItem("")
        self.comboBox_thermal_offset4 = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_thermal_offset4.setGeometry(QtCore.QRect(300, 160, 80, 25))
        self.comboBox_thermal_offset4.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_thermal_offset4.setObjectName("comboBox_thermal_offset4")
        self.comboBox_thermal_offset4.addItem("")
        self.comboBox_thermal_offset4.addItem("")
        self.comboBox_thermal_offset4.addItem("")
        self.comboBox_thermal_offset4.addItem("")
        self.comboBox_thermal_offset4.addItem("")
        self.comboBox_thermal_offset4.addItem("")
        self.comboBox_thermal_offset4.addItem("")
        self.comboBox_thermal_offset4.addItem("")
        self.comboBox_thermal_offset5 = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_thermal_offset5.setGeometry(QtCore.QRect(300, 190, 80, 25))
        self.comboBox_thermal_offset5.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_thermal_offset5.setObjectName("comboBox_thermal_offset5")
        self.comboBox_thermal_offset5.addItem("")
        self.comboBox_thermal_offset5.addItem("")
        self.comboBox_thermal_offset5.addItem("")
        self.comboBox_thermal_offset5.addItem("")
        self.comboBox_thermal_offset5.addItem("")
        self.comboBox_thermal_offset5.addItem("")
        self.comboBox_thermal_offset5.addItem("")
        self.comboBox_thermal_offset5.addItem("")
        self.comboBox_thermal_offset6 = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_thermal_offset6.setGeometry(QtCore.QRect(300, 220, 80, 25))
        self.comboBox_thermal_offset6.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_thermal_offset6.setObjectName("comboBox_thermal_offset6")
        self.comboBox_thermal_offset6.addItem("")
        self.comboBox_thermal_offset6.addItem("")
        self.comboBox_thermal_offset6.addItem("")
        self.comboBox_thermal_offset6.addItem("")
        self.comboBox_thermal_offset6.addItem("")
        self.comboBox_thermal_offset6.addItem("")
        self.comboBox_thermal_offset6.addItem("")
        self.comboBox_thermal_offset6.addItem("")
        self.comboBox_thermal_offset7 = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_thermal_offset7.setGeometry(QtCore.QRect(300, 250, 80, 25))
        self.comboBox_thermal_offset7.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_thermal_offset7.setObjectName("comboBox_thermal_offset7")
        self.comboBox_thermal_offset7.addItem("")
        self.comboBox_thermal_offset7.addItem("")
        self.comboBox_thermal_offset7.addItem("")
        self.comboBox_thermal_offset7.addItem("")
        self.comboBox_thermal_offset7.addItem("")
        self.comboBox_thermal_offset7.addItem("")
        self.comboBox_thermal_offset7.addItem("")
        self.comboBox_thermal_offset7.addItem("")
        self.comboBox_thermal_offset8 = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_thermal_offset8.setGeometry(QtCore.QRect(300, 280, 80, 25))
        self.comboBox_thermal_offset8.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_thermal_offset8.setObjectName("comboBox_thermal_offset8")
        self.comboBox_thermal_offset8.addItem("")
        self.comboBox_thermal_offset8.addItem("")
        self.comboBox_thermal_offset8.addItem("")
        self.comboBox_thermal_offset8.addItem("")
        self.comboBox_thermal_offset8.addItem("")
        self.comboBox_thermal_offset8.addItem("")
        self.comboBox_thermal_offset8.addItem("")
        self.comboBox_thermal_offset8.addItem("")
        self.comboBox_thermal_offset9 = QtWidgets.QComboBox(self.frame_phase_display)
        self.comboBox_thermal_offset9.setGeometry(QtCore.QRect(300, 310, 80, 25))
        self.comboBox_thermal_offset9.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: black;\n"
"\n"
"    background-color: rgb(151, 188, 168);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"font:bold;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color:lightgreen;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.comboBox_thermal_offset9.setObjectName("comboBox_thermal_offset9")
        self.comboBox_thermal_offset9.addItem("")
        self.comboBox_thermal_offset9.addItem("")
        self.comboBox_thermal_offset9.addItem("")
        self.comboBox_thermal_offset9.addItem("")
        self.comboBox_thermal_offset9.addItem("")
        self.comboBox_thermal_offset9.addItem("")
        self.comboBox_thermal_offset9.addItem("")
        self.comboBox_thermal_offset9.addItem("")
        Phase_thermal_balance.setCentralWidget(self.centralwidget)

        self.retranslateUi(Phase_thermal_balance)
        QtCore.QMetaObject.connectSlotsByName(Phase_thermal_balance)

    def retranslateUi(self, Phase_thermal_balance):
        _translate = QtCore.QCoreApplication.translate
        Phase_thermal_balance.setWindowTitle(_translate("Phase_thermal_balance", "Device Configuration"))
        self.label_main_Phase_thermal_balance.setText(_translate("Phase_thermal_balance", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Phase Thermal</span><span style=\" font-size:14pt;\"> Balance</span></p></body></html>"))
        self.pushButton_Discard.setText(_translate("Phase_thermal_balance", "Discard"))
        self.pushButton_Save.setText(_translate("Phase_thermal_balance", "Save"))
        self.comboBox_thermal_offset1.setItemText(0, _translate("Phase_thermal_balance", "0 A"))
        self.comboBox_thermal_offset1.setItemText(1, _translate("Phase_thermal_balance", "1.5 A"))
        self.comboBox_thermal_offset1.setItemText(2, _translate("Phase_thermal_balance", "3 A"))
        self.comboBox_thermal_offset1.setItemText(3, _translate("Phase_thermal_balance", "4.5 A"))
        self.comboBox_thermal_offset1.setItemText(4, _translate("Phase_thermal_balance", "6 A"))
        self.comboBox_thermal_offset1.setItemText(5, _translate("Phase_thermal_balance", "7.5 A"))
        self.comboBox_thermal_offset1.setItemText(6, _translate("Phase_thermal_balance", "9 A"))
        self.comboBox_thermal_offset1.setItemText(7, _translate("Phase_thermal_balance", "11.5 A"))
        self.comboBox_freq_switch_RailA.setItemText(0, _translate("Phase_thermal_balance", "160 KHz"))
        self.comboBox_freq_switch_RailA.setItemText(1, _translate("Phase_thermal_balance", "230 KHz"))
        self.comboBox_freq_switch_RailA.setItemText(2, _translate("Phase_thermal_balance", "350 KHz"))
        self.comboBox_freq_switch_RailA.setItemText(3, _translate("Phase_thermal_balance", "800 KHz"))
        self.label_display_RailB.setText(_translate("Phase_thermal_balance", "Beta"))
        self.label_display_RailA.setText(_translate("Phase_thermal_balance", "Alpha"))
        self.label_RailA_7.setText(_translate("Phase_thermal_balance", "Thermal Balance Offset"))
        self.label_RailA_18.setText(_translate("Phase_thermal_balance", "  :             "))
        self.label_RailA_8.setText(_translate("Phase_thermal_balance", "Phase 1"))
        self.label_RailA_22.setText(_translate("Phase_thermal_balance", "Current Balance Loop Bandwidth"))
        self.comboBox_freq_switch_RailB.setItemText(0, _translate("Phase_thermal_balance", "160 KHz"))
        self.comboBox_freq_switch_RailB.setItemText(1, _translate("Phase_thermal_balance", "230 KHz"))
        self.comboBox_freq_switch_RailB.setItemText(2, _translate("Phase_thermal_balance", "350 KHz"))
        self.comboBox_freq_switch_RailB.setItemText(3, _translate("Phase_thermal_balance", "800 KHz"))
        self.label_RailA_9.setText(_translate("Phase_thermal_balance", "Phase 2"))
        self.label_RailA_19.setText(_translate("Phase_thermal_balance", "  :             "))
        self.label_RailA_10.setText(_translate("Phase_thermal_balance", "Phase 3"))
        self.label_RailA_20.setText(_translate("Phase_thermal_balance", "  :             "))
        self.label_RailA_11.setText(_translate("Phase_thermal_balance", "Phase 4"))
        self.label_RailA_21.setText(_translate("Phase_thermal_balance", "  :             "))
        self.label_RailA_12.setText(_translate("Phase_thermal_balance", "Phase 5"))
        self.label_RailA_23.setText(_translate("Phase_thermal_balance", "  :             "))
        self.label_RailA_13.setText(_translate("Phase_thermal_balance", "Phase 6"))
        self.label_RailA_24.setText(_translate("Phase_thermal_balance", "  :             "))
        self.label_RailA_14.setText(_translate("Phase_thermal_balance", "Phase 7"))
        self.label_RailA_25.setText(_translate("Phase_thermal_balance", "  :             "))
        self.label_RailA_15.setText(_translate("Phase_thermal_balance", "Phase 8"))
        self.label_RailA_26.setText(_translate("Phase_thermal_balance", "  :             "))
        self.label_RailA_45.setText(_translate("Phase_thermal_balance", "Phase 9"))
        self.label_RailA_46.setText(_translate("Phase_thermal_balance", "  :             "))
        self.comboBox_thermal_offset2.setItemText(0, _translate("Phase_thermal_balance", "0 A"))
        self.comboBox_thermal_offset2.setItemText(1, _translate("Phase_thermal_balance", "1.5 A"))
        self.comboBox_thermal_offset2.setItemText(2, _translate("Phase_thermal_balance", "3 A"))
        self.comboBox_thermal_offset2.setItemText(3, _translate("Phase_thermal_balance", "4.5 A"))
        self.comboBox_thermal_offset2.setItemText(4, _translate("Phase_thermal_balance", "6 A"))
        self.comboBox_thermal_offset2.setItemText(5, _translate("Phase_thermal_balance", "7.5 A"))
        self.comboBox_thermal_offset2.setItemText(6, _translate("Phase_thermal_balance", "9 A"))
        self.comboBox_thermal_offset2.setItemText(7, _translate("Phase_thermal_balance", "11.5 A"))
        self.comboBox_thermal_offset3.setItemText(0, _translate("Phase_thermal_balance", "0 A"))
        self.comboBox_thermal_offset3.setItemText(1, _translate("Phase_thermal_balance", "1.5 A"))
        self.comboBox_thermal_offset3.setItemText(2, _translate("Phase_thermal_balance", "3 A"))
        self.comboBox_thermal_offset3.setItemText(3, _translate("Phase_thermal_balance", "4.5 A"))
        self.comboBox_thermal_offset3.setItemText(4, _translate("Phase_thermal_balance", "6 A"))
        self.comboBox_thermal_offset3.setItemText(5, _translate("Phase_thermal_balance", "7.5 A"))
        self.comboBox_thermal_offset3.setItemText(6, _translate("Phase_thermal_balance", "9 A"))
        self.comboBox_thermal_offset3.setItemText(7, _translate("Phase_thermal_balance", "11.5 A"))
        self.comboBox_thermal_offset4.setItemText(0, _translate("Phase_thermal_balance", "0 A"))
        self.comboBox_thermal_offset4.setItemText(1, _translate("Phase_thermal_balance", "1.5 A"))
        self.comboBox_thermal_offset4.setItemText(2, _translate("Phase_thermal_balance", "3 A"))
        self.comboBox_thermal_offset4.setItemText(3, _translate("Phase_thermal_balance", "4.5 A"))
        self.comboBox_thermal_offset4.setItemText(4, _translate("Phase_thermal_balance", "6 A"))
        self.comboBox_thermal_offset4.setItemText(5, _translate("Phase_thermal_balance", "7.5 A"))
        self.comboBox_thermal_offset4.setItemText(6, _translate("Phase_thermal_balance", "9 A"))
        self.comboBox_thermal_offset4.setItemText(7, _translate("Phase_thermal_balance", "11.5 A"))
        self.comboBox_thermal_offset5.setItemText(0, _translate("Phase_thermal_balance", "0 A"))
        self.comboBox_thermal_offset5.setItemText(1, _translate("Phase_thermal_balance", "1.5 A"))
        self.comboBox_thermal_offset5.setItemText(2, _translate("Phase_thermal_balance", "3 A"))
        self.comboBox_thermal_offset5.setItemText(3, _translate("Phase_thermal_balance", "4.5 A"))
        self.comboBox_thermal_offset5.setItemText(4, _translate("Phase_thermal_balance", "6 A"))
        self.comboBox_thermal_offset5.setItemText(5, _translate("Phase_thermal_balance", "7.5 A"))
        self.comboBox_thermal_offset5.setItemText(6, _translate("Phase_thermal_balance", "9 A"))
        self.comboBox_thermal_offset5.setItemText(7, _translate("Phase_thermal_balance", "11.5 A"))
        self.comboBox_thermal_offset6.setItemText(0, _translate("Phase_thermal_balance", "0 A"))
        self.comboBox_thermal_offset6.setItemText(1, _translate("Phase_thermal_balance", "1.5 A"))
        self.comboBox_thermal_offset6.setItemText(2, _translate("Phase_thermal_balance", "3 A"))
        self.comboBox_thermal_offset6.setItemText(3, _translate("Phase_thermal_balance", "4.5 A"))
        self.comboBox_thermal_offset6.setItemText(4, _translate("Phase_thermal_balance", "6 A"))
        self.comboBox_thermal_offset6.setItemText(5, _translate("Phase_thermal_balance", "7.5 A"))
        self.comboBox_thermal_offset6.setItemText(6, _translate("Phase_thermal_balance", "9 A"))
        self.comboBox_thermal_offset6.setItemText(7, _translate("Phase_thermal_balance", "11.5 A"))
        self.comboBox_thermal_offset7.setItemText(0, _translate("Phase_thermal_balance", "0 A"))
        self.comboBox_thermal_offset7.setItemText(1, _translate("Phase_thermal_balance", "1.5 A"))
        self.comboBox_thermal_offset7.setItemText(2, _translate("Phase_thermal_balance", "3 A"))
        self.comboBox_thermal_offset7.setItemText(3, _translate("Phase_thermal_balance", "4.5 A"))
        self.comboBox_thermal_offset7.setItemText(4, _translate("Phase_thermal_balance", "6 A"))
        self.comboBox_thermal_offset7.setItemText(5, _translate("Phase_thermal_balance", "7.5 A"))
        self.comboBox_thermal_offset7.setItemText(6, _translate("Phase_thermal_balance", "9 A"))
        self.comboBox_thermal_offset7.setItemText(7, _translate("Phase_thermal_balance", "11.5 A"))
        self.comboBox_thermal_offset8.setItemText(0, _translate("Phase_thermal_balance", "0 A"))
        self.comboBox_thermal_offset8.setItemText(1, _translate("Phase_thermal_balance", "1.5 A"))
        self.comboBox_thermal_offset8.setItemText(2, _translate("Phase_thermal_balance", "3 A"))
        self.comboBox_thermal_offset8.setItemText(3, _translate("Phase_thermal_balance", "4.5 A"))
        self.comboBox_thermal_offset8.setItemText(4, _translate("Phase_thermal_balance", "6 A"))
        self.comboBox_thermal_offset8.setItemText(5, _translate("Phase_thermal_balance", "7.5 A"))
        self.comboBox_thermal_offset8.setItemText(6, _translate("Phase_thermal_balance", "9 A"))
        self.comboBox_thermal_offset8.setItemText(7, _translate("Phase_thermal_balance", "11.5 A"))
        self.comboBox_thermal_offset9.setItemText(0, _translate("Phase_thermal_balance", "0 A"))
        self.comboBox_thermal_offset9.setItemText(1, _translate("Phase_thermal_balance", "1.5 A"))
        self.comboBox_thermal_offset9.setItemText(2, _translate("Phase_thermal_balance", "3 A"))
        self.comboBox_thermal_offset9.setItemText(3, _translate("Phase_thermal_balance", "4.5 A"))
        self.comboBox_thermal_offset9.setItemText(4, _translate("Phase_thermal_balance", "6 A"))
        self.comboBox_thermal_offset9.setItemText(5, _translate("Phase_thermal_balance", "7.5 A"))
        self.comboBox_thermal_offset9.setItemText(6, _translate("Phase_thermal_balance", "9 A"))
        self.comboBox_thermal_offset9.setItemText(7, _translate("Phase_thermal_balance", "11.5 A"))

