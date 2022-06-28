from estudiante import *
from persona_ui import *

class Persona(QtWidgets.QMainWindow, Persona_UI):
    nombre_signal = QtCore.pyqtSignal(object)  # <-- This is the sub window's signal

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.guardar_btn.clicked.connect(self.guardar)
        self.cancelar_btn.clicked.connect(self.cancelar)

    def obtener_ventana(self, ventana):
        self.ventana = ventana

    def guardar(self):
        print(self.nombre_txt.text())
        estudiante = Estudiante(self.nombre_txt.text(), self.apellido_txt.text())
        self.nombre_signal.emit(estudiante)
        self.hide()
        self.ventana.show()

    def cancelar(self):
        self.hide()
        self.ventana.show()