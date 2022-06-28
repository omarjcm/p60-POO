from persona import *
from ventana_ui import *

class Ventana(QtWidgets.QMainWindow, Ventana_UI):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.actualizar_btn.clicked.connect( self.abrir_ventana )
        self.cerrar_btn.clicked.connect(self.cerrar_ventana)

    def abrir_ventana(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Persona()
        self.ui.obtener_ventana(self)
        self.ui.nombre_signal.connect(self.actualizar_nombre)
        self.hide()
        self.ui.show()

    def cerrar_ventana(self):
        self.close()

    def actualizar_nombre(self, objeto):
        print(objeto.nombre)
        self.nombre_ou.setText( objeto.nombre )
        self.apellido_ou.setText( objeto.apellido )

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ventana()
    window.show()
    app.exec_()