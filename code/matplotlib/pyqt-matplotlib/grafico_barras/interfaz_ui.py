# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from grafico_barra import Grafico_Barra

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 181, 343))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.enero_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enero_txt.setObjectName("enero_txt")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.enero_txt)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.febrero_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.febrero_txt.setObjectName("febrero_txt")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.febrero_txt)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.marzo_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.marzo_txt.setObjectName("marzo_txt")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.marzo_txt)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.abril_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.abril_txt.setObjectName("abril_txt")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.abril_txt)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.mayo_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mayo_txt.setObjectName("mayo_txt")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mayo_txt)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.junio_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.junio_txt.setObjectName("junio_txt")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.junio_txt)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.julio_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.julio_txt.setObjectName("julio_txt")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.julio_txt)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.agosto_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.agosto_txt.setObjectName("agosto_txt")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.agosto_txt)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.septiembre_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.septiembre_txt.setObjectName("septiembre_txt")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.septiembre_txt)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.octubre_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.octubre_txt.setObjectName("octubre_txt")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.octubre_txt)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.noviembre_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.noviembre_txt.setObjectName("noviembre_txt")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.noviembre_txt)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.diciembre_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.diciembre_txt.setObjectName("diciembre_txt")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.diciembre_txt)
        self.generar_grafico_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generar_grafico_btn.setGeometry(QtCore.QRect(340, 400, 381, 31))
        self.generar_grafico_btn.setObjectName("generar_grafico_btn")
        self.widget = Grafico_Barra(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(260, 30, 551, 341))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Valores mensuales"))
        self.label.setText(_translate("MainWindow", "Enero:"))
        self.label_2.setText(_translate("MainWindow", "Febrero:"))
        self.label_3.setText(_translate("MainWindow", "Marzo:"))
        self.label_4.setText(_translate("MainWindow", "Abril:"))
        self.label_5.setText(_translate("MainWindow", "Mayo:"))
        self.label_6.setText(_translate("MainWindow", "Junio:"))
        self.label_7.setText(_translate("MainWindow", "Julio:"))
        self.label_8.setText(_translate("MainWindow", "Agosto:"))
        self.label_9.setText(_translate("MainWindow", "Septiembre:"))
        self.label_10.setText(_translate("MainWindow", "Octubre:"))
        self.label_11.setText(_translate("MainWindow", "Noviembre:"))
        self.label_12.setText(_translate("MainWindow", "Diciembre:"))
        self.generar_grafico_btn.setText(_translate("MainWindow", "Generar Gráfico"))

