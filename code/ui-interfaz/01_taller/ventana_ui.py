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
        MainWindow.resize(730, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.texto_lbl = QtWidgets.QLabel(self.centralwidget)
        self.texto_lbl.setGeometry(QtCore.QRect(60, 30, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.texto_lbl.setFont(font)
        self.texto_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.texto_lbl.setObjectName("texto_lbl")
        self.cambiar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cambiar_btn.setGeometry(QtCore.QRect(290, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cambiar_btn.setFont(font)
        self.cambiar_btn.setObjectName("cambiar_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.texto_lbl.setText(_translate("MainWindow", "Programación Orientada a Objetos"))
        self.cambiar_btn.setText(_translate("MainWindow", "Cambiar Texto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

