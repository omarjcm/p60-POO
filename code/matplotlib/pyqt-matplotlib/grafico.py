from interfaz_ui import *
import numpy as np

class Grafico(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        numeros = np.random.randint(100, size=(12))
        self.enero_txt.setText(str(numeros[0]))

        self.generar_grafico_btn.clicked.connect( self.generar_grafico )

    def generar_grafico(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Grafico()
    window.show()
    app.exec_()