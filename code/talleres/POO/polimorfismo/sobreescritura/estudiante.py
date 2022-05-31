from persona import Persona

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
