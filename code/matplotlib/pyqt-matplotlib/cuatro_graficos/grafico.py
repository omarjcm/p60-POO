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

        self.widget.canvas.ax1.clear()
        self.widget.canvas.ax1.set_xlim([-1, 12])
        self.widget.canvas.ax1.set_ylim([0, max(data)*1.1])
        self.widget.canvas.ax1.set_xticks(x)
        self.widget.canvas.ax1.set_xticklabels(meses)
        self.widget.canvas.ax1.bar(x, data, align='center', width=1)

        self.widget.canvas.ax2.clear()
        self.widget.canvas.ax2.set_xlim([1, 12])
        self.widget.canvas.ax2.set_ylim([0, max(data)*1.1])
        self.widget.canvas.ax2.set_xticks(x)
        self.widget.canvas.ax2.set_xticklabels(x, fontsize=8, color='red')
        self.widget.canvas.ax2.yaxis.set_tick_params(labelsize=8, labelcolor='blue')
        self.widget.canvas.ax2.grid(axis='both', color='0.7', linestyle='-')
        self.widget.canvas.ax2.plot(x, data, color='green')

        self.widget.canvas.ax3.clear()
        self.widget.canvas.ax3.set_xlim([0.5, 12.5])
        self.widget.canvas.ax3.set_ylim([0, max(data)*1.1])
        self.widget.canvas.ax3.set_xticks(x)
        self.widget.canvas.ax3.set_xticklabels(x, fontsize=8)
        self.widget.canvas.ax3.yaxis.set_tick_params(labelsize=8)
        self.widget.canvas.ax3.grid(axis='y', color='0.3', linestyle='-')
        self.widget.canvas.ax3.scatter(x, data, color='magenta')

        self.widget.canvas.ax4.clear()
        self.widget.canvas.ax4.pie(data, labels=meses)

        self.widget.canvas.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Grafico()
    window.show()
    app.exec_()