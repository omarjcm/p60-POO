from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

    def hablar(self, tema=None):
        if (tema is None):
            print('bla')
        else:
            print('Tema de conversacion: ' + tema)