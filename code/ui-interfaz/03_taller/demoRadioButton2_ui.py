# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 471)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 210, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelSelected = QtWidgets.QLabel(Dialog)
        self.labelSelected.setGeometry(QtCore.QRect(20, 380, 691, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelSelected.setFont(font)
        self.labelSelected.setText("")
        self.labelSelected.setWordWrap(True)
        self.labelSelected.setObjectName("labelSelected")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 50, 59, 136))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonMedium = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonMedium.setFont(font)
        self.radioButtonMedium.setObjectName("radioButtonMedium")
        self.verticalLayout.addWidget(self.radioButtonMedium)
        self.radioButtonLarge = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonLarge.setFont(font)
        self.radioButtonLarge.setObjectName("radioButtonLarge")
        self.verticalLayout.addWidget(self.radioButtonLarge)
        self.radioButtonXL = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonXL.setFont(font)
        self.radioButtonXL.setObjectName("radioButtonXL")
        self.verticalLayout.addWidget(self.radioButtonXL)
        self.radioButtonXXL = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonXXL.setFont(font)
        self.radioButtonXXL.setObjectName("radioButtonXXL")
        self.verticalLayout.addWidget(self.radioButtonXXL)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 260, 189, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonDebitCard = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonDebitCard.setFont(font)
        self.radioButtonDebitCard.setObjectName("radioButtonDebitCard")
        self.verticalLayout_2.addWidget(self.radioButtonDebitCard)
        self.radioButtonNetBanking = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonNetBanking.setFont(font)
        self.radioButtonNetBanking.setObjectName("radioButtonNetBanking")
        self.verticalLayout_2.addWidget(self.radioButtonNetBanking)
        self.radioButtonCashOnDelivery = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButtonCashOnDelivery.setFont(font)
        self.radioButtonCashOnDelivery.setObjectName("radioButtonCashOnDelivery")
        self.verticalLayout_2.addWidget(self.radioButtonCashOnDelivery)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose your Shirt Size"))
        self.label_2.setText(_translate("Dialog", "Choose your payment method"))
        self.radioButtonMedium.setText(_translate("Dialog", "M"))
        self.radioButtonLarge.setText(_translate("Dialog", "L"))
        self.radioButtonXL.setText(_translate("Dialog", "XL"))
        self.radioButtonXXL.setText(_translate("Dialog", "XXL"))
        self.radioButtonDebitCard.setText(_translate("Dialog", "Debit/Credit Card"))
        self.radioButtonNetBanking.setText(_translate("Dialog", "NetBanking"))
        self.radioButtonCashOnDelivery.setText(_translate("Dialog", "Cash On Delivery"))

