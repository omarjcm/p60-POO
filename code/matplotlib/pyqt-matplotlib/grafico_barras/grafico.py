from interfaz_ui import *
import numpy as np
import matplotlib.ticker as ticker

class Grafico(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.generar_numeros_aleatorios()
        self.generar_grafico_btn.clicked.connect( self.generar_grafico )
    
    def generar_numeros_aleatorios(self):
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

    def generar_grafico(self):
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        x = [i for i in range(12)]

        data = []
        data.append( int(self.enero_txt.text()) )
        data.append( int(self.febrero_txt.text()) )
        data.append( int(self.marzo_txt.text()) )
        data.append( int(self.abril_txt.text()) )
        data.append( int(self.mayo_txt.text()) )
        data.append( int(self.junio_txt.text()) )
        data.append( int(self.julio_txt.text()) )
        data.append( int(self.agosto_txt.text()) )
        data.append( int(self.septiembre_txt.text()) )
        data.append( int(self.octubre_txt.text()) )
        data.append( int(self.noviembre_txt.text()) )
        data.append( int(self.diciembre_txt.text()) )

        self.widget.canvas.ax.clear()
        self.widget.canvas.ax.axis( [-0.5, 11.5, 0, max(data)+10] )
        self.widget.canvas.ax.xaxis.set_major_locator(ticker.FixedLocator((x)))
        self.widget.canvas.ax.xaxis.set_major_formatter(ticker.FixedFormatter((meses)))
        self.widget.canvas.ax.bar(x, data, align='center', width=1)
        self.widget.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Grafico()
    window.show()
    app.exec_()