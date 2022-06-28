from vista.vestudiante_ui import *

class VEstudiante(QtWidgets.QMainWindow, Ui_VEstudiante):
    dato_signal = QtCore.pyqtSignal(object)  # <-- This is the sub window's signal

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.cancelar_btn.clicked.connect( self.cancelar )

    def cancelar(self):
        self.hide()