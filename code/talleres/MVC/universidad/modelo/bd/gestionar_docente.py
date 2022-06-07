from controlador.gestionar_objeto import Gestionar_Objeto

class Gestionar_Docente(Gestionar_Objeto):
    def __init__(self):
        self.ref_docentes = []

    def insertar(self, objeto):
        self.ref_docentes.append(objeto)

    def modificar(self, objeto):
        for elemento in self.ref_docentes:
            if elemento.cedula == objeto.cedula:
                elemento.edad = objeto.edad

    def eliminar(self, objeto):
        for elemento in self.ref_docentes:
            if elemento.cedula == objeto.cedula:
                del elemento

    def leer(self, objeto):
        for elemento in self.ref_docentes:
            if elemento.cedula == objeto.cedula:
                return elemento

