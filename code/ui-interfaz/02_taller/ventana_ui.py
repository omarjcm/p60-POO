# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(190, 60, 331, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nombre_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.nombre_lbl.setObjectName("nombre_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nombre_lbl)
        self.apellido_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.apellido_lbl.setObjectName("apellido_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.apellido_lbl)
        self.nombre_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nombre_txt.setObjectName("nombre_txt")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nombre_txt)
        self.apellido_txt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.apellido_txt.setObjectName("apellido_txt")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.apellido_txt)
        self.guardar_btn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.guardar_btn.setObjectName("guardar_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.guardar_btn)
        self.cancelar_btn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.cancelar_btn.setObjectName("cancelar_btn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cancelar_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Formulario"))
        self.nombre_lbl.setText(_translate("MainWindow", "Nombre:"))
        self.apellido_lbl.setText(_translate("MainWindow", "Apellido:"))
        self.guardar_btn.setText(_translate("MainWindow", "Guardar"))
        self.cancelar_btn.setText(_translate("MainWindow", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

