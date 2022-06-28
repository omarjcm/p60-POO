from controlador.gestionar_estudiante import Gestionar_Estudiante
from vista.gestionar_vestudiante_ui import *
from vista.vestudiante import *

class Gestionar_VEstudiante(QtWidgets.QMainWindow, Ui_Gestionar_VEstudiante):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.gestionar_estudiantes = Gestionar_Estudiante()
        self.cargar_datos()

        self.cancelar_btn.clicked.connect( self.cancelar )
        self.agregar_btn.clicked.connect( self.agregar )


    def cargar_datos(self):
        indice = 0
        for estudiante in self.gestionar_estudiantes.ref_estudiantes:
            self.estudiantes_tbl.setRowCount(indice + 1)

            modificar_btn = QtWidgets.QPushButton("Modificar")
            modificar_btn.clicked.connect(self.modificar_estudiante)
            eliminar_btn = QtWidgets.QPushButton("Eliminar")
            eliminar_btn.clicked.connect(self.eliminar_estudiante)

            self.estudiantes_tbl.setItem(indice, 0, QtWidgets.QTableWidgetItem( estudiante.cedula ))
            self.estudiantes_tbl.setItem(indice, 1, QtWidgets.QTableWidgetItem( estudiante.nombre ))
            self.estudiantes_tbl.setItem(indice, 2, QtWidgets.QTableWidgetItem( estudiante.apellido ))
            self.estudiantes_tbl.setItem(indice, 3, QtWidgets.QTableWidgetItem( str(estudiante.edad) ))
            self.estudiantes_tbl.setCellWidget(indice, 4, modificar_btn)
            self.estudiantes_tbl.setCellWidget(indice, 5, eliminar_btn)

            indice += 1

    @QtCore.pyqtSlot()
    def modificar_estudiante(self):
        button = self.sender()
        if button:
            row = self.estudiantes_tbl.indexAt(button.pos()).row()
            estudiante = self.gestionar_estudiantes.ref_estudiantes[row]
            self.gestionar_estudiantes.modificar(estudiante)

    @QtCore.pyqtSlot()
    def eliminar_estudiante(self):
        button = self.sender()
        
        if button:
            row = self.estudiantes_tbl.indexAt(button.pos()).row()
            estudiante = self.gestionar_estudiantes.ref_estudiantes[row]
            self.gestionar_estudiantes.eliminar(estudiante)
            
            self.estudiantes_tbl.removeRow(row)
            self.estudiantes_tbl.clearSelection()

    def agregar(self):
        self.estudiante = QtWidgets.QMainWindow()
        self.ui = VEstudiante()
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