# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'svi2_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(871, 633)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 150, 91, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(580, 130, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 91, 21))
        self.label_3.setObjectName("label_3")
        self.comboBox_vdd2 = QtWidgets.QComboBox(Form)
        self.comboBox_vdd2.setGeometry(QtCore.QRect(300, 80, 191, 22))
        self.comboBox_vdd2.setObjectName("comboBox_vdd2")
        self.comboBox_vdd2.addItem("")
        self.comboBox_vdd2.addItem("")
        self.comboBox_vdd1 = QtWidgets.QComboBox(Form)
        self.comboBox_vdd1.setGeometry(QtCore.QRect(300, 20, 191, 22))
        self.comboBox_vdd1.setObjectName("comboBox_vdd1")
        self.comboBox_vdd1.addItem("")
        self.comboBox_vdd1.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(180, 200, 91, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox_psi0 = QtWidgets.QComboBox(Form)
        self.comboBox_psi0.setGeometry(QtCore.QRect(300, 200, 191, 22))
        self.comboBox_psi0.setObjectName("comboBox_psi0")
        self.comboBox_psi0.addItem("")
        self.comboBox_psi0.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(180, 240, 91, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox_psi1 = QtWidgets.QComboBox(Form)
        self.comboBox_psi1.setGeometry(QtCore.QRect(300, 240, 191, 22))
        self.comboBox_psi1.setObjectName("comboBox_psi1")
        self.comboBox_psi1.addItem("")
        self.comboBox_psi1.addItem("")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(180, 280, 91, 21))
        self.label_6.setObjectName("label_6")
        self.comboBox_tfn = QtWidgets.QComboBox(Form)
        self.comboBox_tfn.setGeometry(QtCore.QRect(300, 280, 191, 22))
        self.comboBox_tfn.setObjectName("comboBox_tfn")
        self.comboBox_tfn.addItem("")
        self.comboBox_tfn.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(150, 330, 121, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(180, 370, 91, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_vid = QtWidgets.QLineEdit(Form)
        self.lineEdit_vid.setGeometry(QtCore.QRect(300, 150, 191, 21))
        self.lineEdit_vid.setAcceptDrops(True)
        self.lineEdit_vid.setToolTip("")
        self.lineEdit_vid.setToolTipDuration(4)
        self.lineEdit_vid.setStatusTip("")
        self.lineEdit_vid.setWhatsThis("")
        self.lineEdit_vid.setAutoFillBackground(False)
        self.lineEdit_vid.setText("")
        self.lineEdit_vid.setPlaceholderText("")
        self.lineEdit_vid.setObjectName("lineEdit_vid")
        self.comboBox_ll_trim = QtWidgets.QComboBox(Form)
        self.comboBox_ll_trim.setGeometry(QtCore.QRect(300, 330, 191, 22))
        self.comboBox_ll_trim.setAutoFillBackground(False)
        self.comboBox_ll_trim.setObjectName("comboBox_ll_trim")
        self.comboBox_ll_trim.addItem("")
        self.comboBox_ll_trim.addItem("")
        self.comboBox_ll_trim.addItem("")
        self.comboBox_ll_trim.addItem("")
        self.comboBox_ll_trim.addItem("")
        self.comboBox_ll_trim.addItem("")
        self.comboBox_ll_trim.addItem("")
        self.comboBox_ll_trim.addItem("")
        self.comboBox_offset = QtWidgets.QComboBox(Form)
        self.comboBox_offset.setGeometry(QtCore.QRect(300, 370, 191, 22))
        self.comboBox_offset.setObjectName("comboBox_offset")
        self.comboBox_offset.addItem("")
        self.comboBox_offset.addItem("")
        self.comboBox_offset.addItem("")
        self.comboBox_offset.addItem("")
        self.pushButton_tele = QtWidgets.QPushButton(Form)
        self.pushButton_tele.setGeometry(QtCore.QRect(580, 300, 161, 61))
        self.pushButton_tele.setObjectName("pushButton_tele")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(170, 410, 91, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_clk = QtWidgets.QLineEdit(Form)
        self.lineEdit_clk.setGeometry(QtCore.QRect(300, 410, 191, 21))
        self.lineEdit_clk.setAcceptDrops(True)
        self.lineEdit_clk.setToolTip("")
        self.lineEdit_clk.setToolTipDuration(4)
        self.lineEdit_clk.setStatusTip("")
        self.lineEdit_clk.setWhatsThis("")
        self.lineEdit_clk.setAutoFillBackground(False)
        self.lineEdit_clk.setText("")
        self.lineEdit_clk.setPlaceholderText("")
        self.lineEdit_clk.setObjectName("lineEdit_clk")
        self.radioButton_votf = QtWidgets.QRadioButton(Form)
        self.radioButton_votf.setGeometry(QtCore.QRect(620, 220, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_votf.setFont(font)
        self.radioButton_votf.setObjectName("radioButton_votf")

        self.retranslateUi(Form)
        self.comboBox_psi0.setCurrentIndex(0)
        self.comboBox_ll_trim.setCurrentIndex(3)
        self.comboBox_offset.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "VID CODE"))
        self.pushButton.setText(_translate("Form", "SEND COMMAND"))
        self.label_2.setText(_translate("Form", "VDD2"))
        self.label_3.setText(_translate("Form", "VDD1"))
        self.comboBox_vdd2.setItemText(0, _translate("Form", "0 - Not selected"))
        self.comboBox_vdd2.setItemText(1, _translate("Form", "1 - Selected"))
        self.comboBox_vdd1.setItemText(0, _translate("Form", "0 - Not selected"))
        self.comboBox_vdd1.setItemText(1, _translate("Form", "1 - Selected"))
        self.label_4.setText(_translate("Form", "PSI0_L"))
        self.comboBox_psi0.setItemText(0, _translate("Form", "0 - Assert"))
        self.comboBox_psi0.setItemText(1, _translate("Form", "1 - Deassert"))
        self.label_5.setText(_translate("Form", "PSI1_L"))
        self.comboBox_psi1.setItemText(0, _translate("Form", "0 - Assert"))
        self.comboBox_psi1.setItemText(1, _translate("Form", "1 - Deassert"))
        self.label_6.setText(_translate("Form", "TFN"))
        self.comboBox_tfn.setItemText(0, _translate("Form", "0 - Disable"))
        self.comboBox_tfn.setItemText(1, _translate("Form", "1 - Enable"))
        self.label_7.setText(_translate("Form", "Load line slope trim"))
        self.label_8.setText(_translate("Form", "offset trim"))
        self.comboBox_ll_trim.setCurrentText(_translate("Form", "3 - Initial LL Slope(Default Value)"))
        self.comboBox_ll_trim.setItemText(0, _translate("Form", "0 - Remove all LL droop from output"))
        self.comboBox_ll_trim.setItemText(1, _translate("Form", "1 - Initial LL Slope -40%"))
        self.comboBox_ll_trim.setItemText(2, _translate("Form", "2 - Initial LL Slope -20%"))
        self.comboBox_ll_trim.setItemText(3, _translate("Form", "3 - Initial LL Slope(Default Value)"))
        self.comboBox_ll_trim.setItemText(4, _translate("Form", "4 - Initial LL Slope +20%"))
        self.comboBox_ll_trim.setItemText(5, _translate("Form", "5 - Initial LL Slope +40%"))
        self.comboBox_ll_trim.setItemText(6, _translate("Form", "6 - Initial LL Slope +60%"))
        self.comboBox_ll_trim.setItemText(7, _translate("Form", "7 - Initial LL Slope +80%"))
        self.comboBox_offset.setItemText(0, _translate("Form", "0 - Remove all Offsetfrom output"))
        self.comboBox_offset.setItemText(1, _translate("Form", "1 - Initial Offset -25mV"))
        self.comboBox_offset.setItemText(2, _translate("Form", "2 - Use Initial Offset(Default Value)"))
        self.comboBox_offset.setItemText(3, _translate("Form", "3 - Initial Offset +25mV"))
        self.pushButton_tele.setText(_translate("Form", "REPORT TELEMETRY"))
        self.label_9.setText(_translate("Form", "clock frequency"))
        self.radioButton_votf.setText(_translate("Form", "VOTF"))
