from grafico_canvas import Grafico_Canvas
from PyQt5 import QtWidgets

class Grafico_Barra(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = Grafico_Canvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)