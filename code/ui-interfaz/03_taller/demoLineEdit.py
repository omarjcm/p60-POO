from demoLineEdit_ui import *

class DemoLineEdit(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ButtonClickMe.clicked.connect( self.actualizar_mensaje )

    def actualizar_mensaje(self):
        self.labelResponse.setText('¡Hola {}!'.format(self.lineEditName.text()))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DemoLineEdit()
    window.show()
    app.exec_()