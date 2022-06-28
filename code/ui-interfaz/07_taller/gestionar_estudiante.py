from gestionar_estudiante_ui import *
from estudiante import *

class Gestionar_Estudiante(QtWidgets.QMainWindow, Gestionar_Estudiante_UI):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.cancelar_btn.clicked.connect( self.cancelar )
        self.agregar_btn.clicked.connect( self.agregar )

    def agregar(self):
        self.estudiante = QtWidgets.QMainWindow()
        self.ui = Estudiante()
        self.ui.dato_signal.connect(self.actualizar_tabla)
        self.ui.show()

    def actualizar_tabla(self, data):
        pass

    def cancelar(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Gestionar_Estudiante()
    window.show()
    app.exec_()