from datetime import datetime 

especialidades = [
    [1, 'Medicina General'],
    [2, 'Cardiologia'],
    [3, 'Traumatologia'],
    [4, 'Dermatologia'],
    [5, 'Pediatria']
]
pacientes = [
    ['Pablo Banderas', 'M', '1996', '3', 50],
    ['Angie Santos', 'F', '2001', '4', 45],
    ['Luis Parrales', 'M', '1950', '2', 35]
]

print('Sistema de la Clinica UPS')

opcion = 'N'
while opcion == 'N':
    opcion = input('¿Desea ingresar un nuevo paciente? [S-N]: ')
    if opcion == 'N':
        break

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
    
    valor = 0
    if especialidad == '1':
        valor = 30
    elif especialidad == '2':
        valor = 35
    elif especialidad == '3':
        valor = 50
    elif especialidad == '4':
        valor = 45
    elif especialidad == '5':
        valor = 40
    
    pacientes.append( [nombre, sexo, anio, especialidad, valor] )
    opcion = input('¿Desea salir? ')

fecha_actual = datetime.now()
anio_actual = fecha_actual.strftime('%Y')



for paciente in pacientes:
    print( paciente )