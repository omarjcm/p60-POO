from modelo.bd.gestionar_docente import Gestionar_Docente

class Menu_Principal():
    def __init__(self) -> None:
        self.ref_gestionar_docente = Gestionar_Docente()
        self.opciones = ['Estudiante', 'Docente']

    def menu_principal(self):
        print('*'*50)
        print('UNIVERSIDAD')
        print('*'*50)

        indice = 1
        for opcion in self.opciones:
            print('[{}].- {}'.format(indice, opcion))
            indice += 1

        print('[{}].- {}'.format(0, 'Salir'))



