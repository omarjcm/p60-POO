class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    def hablar(self):
        print('bla bla bla')

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido)
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    def hablar(self):
        print( 'Hola soy {} {}.'.format(self._nombre, self._apellido) )


if __name__ == '__main__':
    objeto = Estudiante('Guillermo', 'Pizarro', 40)
    objeto.hablar()