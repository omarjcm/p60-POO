from datetime import datetime 

especialidades = [
    ['1', 'Medicina General', 0],
    ['2', 'Cardiologia', 0],
    ['3', 'Traumatologia', 0],
    ['4', 'Dermatologia', 0],
    ['5', 'Pediatria', 0]
]
pacientes = [
    ['Pablo Banderas', 'M', '1996', '3', 50],
    ['Angie Santos', 'F', '2001', '4', 45],
    ['Julian Tamayo', 'M', '2002', '3', 50],
    ['Marcelo Bolaños', 'M', '2001', '3', 50],
    ['Samantha Iglesias', 'F', '2003', '1', 30],
    ['Marco Guevara', 'M', '2003', '1', 30],
    ['Julia Child', 'F', '1948', '2', 35],
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

# Total de los descuentos realizados.
total_descuentos = 0.0
for paciente in pacientes:
    anio_actual = int(anio_actual)
    anio_nacimiento = int(paciente[2])

    if (anio_actual - anio_nacimiento) >= 65:
        descuento = paciente[4]*0.1
        paciente[4] = paciente[4] - descuento
        total_descuentos += descuento

print('Total de descuentos: {}'.format(total_descuentos))

# Total en consultas.
total_consultas = 0.0
for paciente in pacientes:
    total_consultas += paciente[4]

print('Total en consultas: {}'.format(total_consultas))
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

# Cantidad de consultas por especialidad.
for paciente in pacientes:
    if especialidades[0][0] == paciente[3]:
        especialidades[0][2] += 1
    elif especialidades[1][0] == paciente[3]:
        especialidades[1][2] += 1
    elif especialidades[2][0] == paciente[3]:
        especialidades[2][2] += 1
    elif especialidades[3][0] == paciente[3]:
        especialidades[3][2] += 1
    elif especialidades[4][0] == paciente[3]:
        especialidades[4][2] += 1

for especialidad in especialidades:
    if (especialidad[2] != 1):
        print('{} - {} veces.'.format(especialidad[1], especialidad[2]))
    else:
        print('{} - {} vez.'.format(especialidad[1], especialidad[2]))

# Total recaudado por especialidad.
