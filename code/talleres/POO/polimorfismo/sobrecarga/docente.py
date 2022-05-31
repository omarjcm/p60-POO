from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

    def hablar(self, tema=None):
        if (tema is None):
            print('bla')
        else:
            print('Tema de conversacion: ' + tema)

    def enseniar(self, horas=None, tema=None):
        if horas is not None and tema is not None:
            print('Las {} horas a revisar con respecto al tema {}.'.format(horas, tema))
        else:
            print('No existen horas para las clases respectivas')
