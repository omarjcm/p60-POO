from docente import Docente
from estudiante import Estudiante

if __name__ == '__main__':
    objeto = Estudiante('Guillermo', 'Pizarro', 40)
    objeto.hablar()

    objeto2 = Docente('Javier', 'Ortiz')
    objeto2.hablar()
    objeto2.hablar('POO')

