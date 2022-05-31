from gestionar_objeto import Gestionar_Objeto

class Gestionar_Estudiante(Gestionar_Objeto):
    def __init__(self):
        self.__estudiantes = []

    @property
    def estudiantes(self):
        return self.__estudiantes

    @estudiantes.setter
    def estudiantes(self, valor):
        self.__estudiantes = valor

    def insertar(self, objeto):
        self.__estudiantes.append(objeto)

    def modificar(self, objeto):
        for elemento in self.__estudiantes:
            if elemento.nombre == objeto.nombre and elemento.apellido == objeto.apellido:
                elemento.edad = objeto.edad

    def eliminar(self, objeto):
        for elemento in self.__estudiantes:
            if elemento.nombre == objeto.nombre and elemento.apellido == objeto.apellido:
                del elemento

    def leer(self, objeto):
        for elemento in self.__estudiantes:
            if elemento.nombre == objeto.nombre and elemento.apellido == objeto.apellido:
                return elemento

