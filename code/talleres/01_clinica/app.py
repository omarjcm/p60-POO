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
    print(paciente)

for paciente in pacientes:
    anio_actual = int(anio_actual)
    anio_nacimiento = int(paciente[2])

    if (anio_actual - anio_nacimiento) >= 65:
        paciente[4] = paciente[4] - paciente[4]*0.1

for paciente in pacientes:
    print(paciente)

# Cantidad de consultas por especialidad.
# Total recaudado por especialidad.
# Total de descuentos.
# Total en consultas.

# Total de pacientes.
print('Total de pacientes: {}'.format( len(pacientes) ) )

# Total de pacientes por sexo.
num_pacientes_m = 0
num_pacientes_f = 0
for paciente in pacientes:
    if paciente[1] == 'M':
        num_pacientes_m += 1
    if paciente[1] == 'F':
        num_pacientes_f += 1

print('Total de pacientes por sexo.')
print('Masculino: {}'.format(num_pacientes_m))
print('Femenino: {}'.format(num_pacientes_f))
