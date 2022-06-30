from PyQt5.QtWidgets import QMessageBox

'''
Basado en: https://stackoverflow.com/questions/59135425/how-to-change-text-of-pyqt-standardbuttons
'''
class Si_No:
    def __init__(self, ventana, titulo, texto):
        self.mensaje = QMessageBox(ventana)
        self.mensaje.setIcon( QMessageBox.Warning )
        self.titulo = titulo
        self.texto = texto

    def mostrar(self):
        self.mensaje.setWindowTitle( self.titulo )
        self.mensaje.setText( self.texto )
        self.boton_si = self.mensaje.addButton('Si', QMessageBox.YesRole)
        self.boton_no = self.mensaje.addButton('No', QMessageBox.AcceptRole)
        self.mensaje.setDefaultButton( self.boton_no )
        self.mensaje.exec_()

    def acepto(self):
        return self.mensaje.clickedButton() == self.boton_si