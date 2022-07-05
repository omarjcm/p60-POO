from controlador.gestionar_objeto import Gestionar_Objeto
from modelo.estudiante import Estudiante

class Gestionar_Estudiante(Gestionar_Objeto):
    def __init__(self):
        self.ref_estudiantes = [
            Estudiante('0937485959', 'Roque', 'Ovaco', 23),
            Estudiante('0937485912', 'Amir', 'Mustafa', 22),
            Estudiante('0937481259', 'Samyr', 'Menedez', 24),
            Estudiante('0937125959', 'Steeven', 'Aguayo', 21),
            Estudiante('0912485959', 'Samuel', 'Diaz', 25),
            Estudiante('0937345959', 'Ariana', 'Izurieta', 24),
            Estudiante('0937483459', 'Joseph', 'Peña', 23),
            Estudiante('0937485934', 'Esteban', 'Guerrero', 22)
        ]

    def insertar(self, objeto):
        self.ref_estudiantes.append(objeto)

    def modificar(self, objeto):
        for elemento in self.ref_estudiantes:
            if elemento.cedula == objeto.cedula:
                elemento.nombre = objeto.nombre
                elemento.apellido = objeto.apellido
                elemento.edad = objeto.edad

    def eliminar(self, objeto):
        for elemento in self.ref_estudiantes:
            if elemento.cedula == objeto.cedula:
                self.ref_estudiantes.remove(elemento)

    def leer(self, objeto):
        if objeto is not None:
            for elemento in self.ref_estudiantes:
                if elemento.cedula == objeto.cedula:
                    return elemento
        else:
            return self.ref_estudiantes


    