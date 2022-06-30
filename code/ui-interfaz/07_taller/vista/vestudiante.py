from modelo.estudiante import Estudiante
from vista.vestudiante_ui import *

class VEstudiante(QtWidgets.QMainWindow, Ui_VEstudiante):
    dato_signal = QtCore.pyqtSignal(object)  # <-- This is the sub window's signal

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.cancelar_btn.clicked.connect( self.cancelar )
        self.guardar_btn.clicked.connect( self.guardar )

    def obtener_ventana(self, ventana):
        self.ventana = ventana
        if self.ventana.tipo_accion == 'MODIFICAR':
            self.actualizar(self.ventana.estudiante)
        
    def actualizar(self, estudiante):
        self.cedula_txt.setText(estudiante.cedula)
        self.nombre_txt.setText(estudiante.nombre)
        self.apellido_txt.setText(estudiante.apellido)
        self.edad_txt.setText(str(estudiante.edad))

    def guardar(self):
        estudiante = Estudiante(
            self.cedula_txt.text(),
            self.nombre_txt.text(), 
            self.apellido_txt.text(),
            self.edad_txt.text()
        )
        self.dato_signal.emit(estudiante)
        self.close()

    def cancelar(self):
        self.close()