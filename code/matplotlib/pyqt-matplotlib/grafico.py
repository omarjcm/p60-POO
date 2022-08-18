from interfaz_ui import *
import numpy as np

class Grafico(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        indice = 0
        numeros = np.random.randint(100, size=(12))
        self.enero_txt.setText(str(numeros[indice]))
        indice += 1
        self.febrero_txt.setText(str(numeros[indice]))
        indice += 1
        self.marzo_txt.setText(str(numeros[indice]))
        indice += 1
        self.abril_txt.setText(str(numeros[indice]))
        indice += 1
        self.mayo_txt.setText(str(numeros[indice]))
        indice += 1
        self.junio_txt.setText(str(numeros[indice]))
        indice += 1
        self.julio_txt.setText(str(numeros[indice]))
        indice += 1
        self.agosto_txt.setText(str(numeros[indice]))
        indice += 1
        self.septiembre_txt.setText(str(numeros[indice]))
        indice += 1
        self.octubre_txt.setText(str(numeros[indice]))
        indice += 1
        self.noviembre_txt.setText(str(numeros[indice]))
        indice += 1
        self.diciembre_txt.setText(str(numeros[indice]))
        indice += 1

        self.generar_grafico_btn.clicked.connect( self.generar_grafico )

    def generar_grafico(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Grafico()
    window.show()
    app.exec_()