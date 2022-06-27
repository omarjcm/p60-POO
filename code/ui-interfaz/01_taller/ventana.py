from ventana_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.texto_lbl.setText('Haz click en el boton.')
        self.cambiar_btn.setText('Presioname')

        self.cambiar_btn.clicked.connect( self.actualizar )

    def actualizar(self):
        self.texto_lbl.setText('Acabas de dar click en el boton.')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()