from controlador.gestionar_estudiante import Gestionar_Estudiante
from vista.gestionar_vestudiante_ui import *
from vista.vestudiante import *
from vista.mensaje.pregunta import *

from PyQt5.QtWidgets import QDesktopWidget

class Gestionar_VEstudiante(QtWidgets.QMainWindow, Ui_Gestionar_VEstudiante):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # se centra la ventana
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # se inicializa el objeto que permitira gestionar a los estudiantes
        self.gestionar_estudiantes = Gestionar_Estudiante()
        # se cargan los datos en la tabla
        self.cargar_datos()
        # se añaden los eventos a los botones principales de la ventana
        self.cancelar_btn.clicked.connect( self.cancelar )
        self.agregar_btn.clicked.connect( self.agregar )


    def cargar_datos(self):
        indice = 0
        for estudiante in self.gestionar_estudiantes.ref_estudiantes:
            self.estudiantes_tbl.setRowCount(indice + 1)
            # declaracion de los botones que iran dentro de la tabla.
            modificar_btn = QtWidgets.QPushButton("Modificar")
            modificar_btn.clicked.connect(self.modificar_estudiante)
            eliminar_btn = QtWidgets.QPushButton("Eliminar")
            eliminar_btn.clicked.connect(self.eliminar_estudiante)
            # se agrega estudiante por estudiante a las filas de las tablas.
            self.estudiantes_tbl.setItem(indice, 0, QtWidgets.QTableWidgetItem( estudiante.cedula ))
            self.estudiantes_tbl.setItem(indice, 1, QtWidgets.QTableWidgetItem( estudiante.nombre ))
            self.estudiantes_tbl.setItem(indice, 2, QtWidgets.QTableWidgetItem( estudiante.apellido ))
            self.estudiantes_tbl.setItem(indice, 3, QtWidgets.QTableWidgetItem( str(estudiante.edad) ))
            # se agregan los botones en la tabla (estudiante por estudiante)
            self.estudiantes_tbl.setCellWidget(indice, 4, modificar_btn)
            self.estudiantes_tbl.setCellWidget(indice, 5, eliminar_btn)

            indice += 1

    @QtCore.pyqtSlot()
    def modificar_estudiante(self):
        button = self.sender()
        if button:
            self.tipo_accion = 'MODIFICAR'
            row = self.estudiantes_tbl.indexAt(button.pos()).row()
            self.estudiante = self.gestionar_estudiantes.ref_estudiantes[row]
            self.gestionar_estudiantes.modificar(self.estudiante)
            self.abrir_ventana()

    @QtCore.pyqtSlot()
    def eliminar_estudiante(self):
        button = self.sender()

        consulta = Si_No(self, 'Eliminar Estudiante', '¿Está seguro que desea eliminar al Estudiante?')
        consulta.mostrar()
        
        if button and consulta.acepto():
            row = self.estudiantes_tbl.indexAt(button.pos()).row()
            self.gestionar_estudiantes.eliminar( self.gestionar_estudiantes.ref_estudiantes[row] )

            self.estudiantes_tbl.removeRow(row)
            self.estudiantes_tbl.clearSelection()
    
    def agregar(self):
        self.tipo_accion = 'AGREGAR'
        self.estudiante = None
        self.abrir_ventana()
        
    def abrir_ventana(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = VEstudiante(self)
        self.ui.obtener_ventana(self)
        self.ui.dato_signal.connect(self.obtener_dato)
        self.ui.show()

    def obtener_dato(self, objeto):
        self.estudiante = objeto
        print(self.estudiante.cedula)
        print(self.estudiante.nombre)
        print(self.estudiante.apellido)

        if self.tipo_accion == 'AGREGAR':
            pass
        elif self.tipo_accion == 'MODIFICAR':
            pass

    def actualizar_tabla(self, data):
        pass

    def cancelar(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Gestionar_Estudiante()
    window.show()
    app.exec_()