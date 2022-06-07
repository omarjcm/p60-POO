from modelo.bd.gestionar_docente import Gestionar_Docente

class Menu_Principal():
    def __init__(self) -> None:
        self.ref_gestionar_docente = Gestionar_Docente()

    def menu_principal(self):
        print('*'*50)
        print('UNIVERSIDAD')
        print('*'*50)

        