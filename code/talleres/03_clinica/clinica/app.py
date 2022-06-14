from vista.Menu_Principal import Menu_Principal

if __name__ == '__main__':
    app = Menu_Principal()

    while(True):
        '''
        Se presenta que se desea gestionar: Consultas, Pacientes, Especialidad
        '''
        app.menu_principal()
        opcion = int(input('Ingresar opcion: '))

        if opcion == 0:
            break

        app.menu_opcion(opcion)
        subopcion = int(input('Ingresar opcion: '))
        app.opcion_seleccionada(opcion, subopcion)

