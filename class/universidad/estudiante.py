from persona import Persona

class Estudiante(Persona):
    def __init__(self, cedula, nombre, apellido, fecha_nacimiento, quintil):
        super().__init__(cedula, nombre, apellido, fecha_nacimiento)
        self.__quintil = quintil

    @property
    def quintil(self):
        return self.__quintil

    @quintil.setter
    def quintil(self, valor):
        self.__quintil = valor
    