especialidades = [
    [1, 'Medicina General'],
    [2, 'Cardiologia'],
    [3, 'Traumatologia'],
    [4, 'Dermatologia'],
    [5, 'Pediatria']
]
pacientes = []

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

for paciente in pacientes:
    print(  )