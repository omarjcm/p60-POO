from persona import Persona
from gestionarobjeto import Gestionar_Objeto

class Estudiante(Persona, Gestionar_Objeto):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido)
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    def hablar(self, tema=None):
        if tema is not None:
            '''Sobreescritura (añado comportamiento)'''
            super().hablar()
            print('Hablo sobre el tema: ' + tema)
        else:
            '''
            Sobreescritura del comportamiento del metodo en la clase padre,
            se lo vuelve a implementar en la clase hija.
            '''
            print( 'Hola soy {} {}.'.format(self._nombre, self._apellido) )

    def insertar(self, objeto):
        self._nombre = objeto.nombre
        self._apellido = objeto.apellido
        self.__edad = objeto.edad

    def modificar(self, objeto):
        self._nombre = objeto.nombre
        self._apellido = objeto.apellido
        self.__edad = objeto.edad

    def eliminar(self, objeto):
        pass

    def leer(self, objeto):
        pass
