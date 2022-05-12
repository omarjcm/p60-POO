print('Sistema de la Clinica UPS')

opcion = 'N'
while opcion == 'N':
    nombre = input('Nombre del Paciente: ')
    sexo = input('Sexo [M-F]: ')
    anio = input('Año de Nacimiento: ')

    print('Seleccionar la especialidad: ')
    print('1 - Medicina General - $30')
    print('2 - Cardiologia - $35')
    print('3 - Traumatologia - $50')
    print('4 - Dermatologia - $45')
    print('5 - Pediatria - $40')
    especialidad = input('Especialidad [1-2-3-4-5]: ')

    opcion = input('¿Desea salir? ')