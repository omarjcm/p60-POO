from ventana_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.guardar_btn.clicked.connect(self.guardar)
        self.cancelar_btn.clicked.connect(self.cancelar)

    def guardar(self):
        self.label.setText('Acabas de hacer click en el boton.')

    def cancelar(self):
        self.label.setText('Acabas de hacer click en el boton.')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()