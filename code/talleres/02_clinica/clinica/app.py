from Paciente import *
from Consulta import *
from Especialidad import *
from datetime import datetime

frecuencias = [0, 0, 0, 0, 0]
totales = [0.0, 0.0, 0.0, 0.0, 0.0]

especialidades = [
    Especialidad('Medicina General', 30),
    Especialidad('Cardiologia', 35),
    Especialidad('Traumatologia', 50),
    Especialidad('Dermatologia', 45),
    Especialidad('Pediatria', 40)
]

pacientes = [
    Paciente('Pablo', 'Banderas', 'M', 1996),
    Paciente('Angie', 'Santos', 'F', 2001),
    Paciente('Julian', 'Tamayo', 'M', 2002),
    Paciente('Marcelo', 'Bolaños', 'M', 2001),
    Paciente('Samantha', 'Iglesias', 'F', 2003),
    Paciente('Marco' ,'Guevara', 'M', 2003),
    Paciente('Julia', 'Child', 'F', 1948),
    Paciente('Luis', 'Parrales', 'M', 1950)
]

consultas = [
    Consulta('20-04-2022', pacientes[0], especialidades[2]),
    Consulta('20-04-2022', pacientes[1], especialidades[3]),
    Consulta('21-04-2022', pacientes[2], especialidades[2]),
    Consulta('21-04-2022', pacientes[3], especialidades[2]),
    Consulta('21-04-2022', pacientes[4], especialidades[0]),
    Consulta('02-05-2022', pacientes[5], especialidades[0]),
    Consulta('03-05-2022', pacientes[6], especialidades[1]),
    Consulta('10-05-2022', pacientes[7], especialidades[1]),
]

def reporte_descuentos_realizados():
    fecha_actual = datetime.now()
    anio_actual = fecha_actual.strftime('%Y')

    # Total de los descuentos realizados.
    total_descuentos = 0.0
    for consulta in consultas:
        anio_actual = int(anio_actual)
        anio_nacimiento = consulta.ref_paciente.anio_nacimiento

        if (anio_actual - anio_nacimiento) >= 65:
            consulta.valor_descuento = consulta.ref_especialidad.valor*0.1
            consulta.valor_total = consulta.ref_especialidad.valor - consulta.valor_descuento
            total_descuentos += consulta.valor_descuento
        else:
            consulta.valor_total = consulta.ref_especialidad.valor

    print('Total de descuentos: {}'.format(total_descuentos))

def reporte_total_consultas():
    # Total en consultas.
    total_consultas = 0.0
    for consulta in consultas:
        total_consultas += consulta.valor_total

    print('Total en consultas: {}'.format(total_consultas))
    # Total de pacientes.
    print('Total de pacientes: {}'.format( len(consultas) ) )

def reporte_total_x_sexo():
    # Total de pacientes por sexo.
    num_pacientes_m = 0
    num_pacientes_f = 0
    for consulta in consultas:
        if consulta.ref_paciente.sexo == 'M':
            num_pacientes_m += 1
        if consulta.ref_paciente.sexo == 'F':
            num_pacientes_f += 1

    print('Total de pacientes por sexo.')
    print('Masculino: {}'.format(num_pacientes_m))
    print('Femenino: {}'.format(num_pacientes_f))

def reporte_cantidad_x_especialidad():
    # Cantidad de consultas por especialidad.
    for consulta in consultas:
        if consulta.ref_especialidad.nombre == especialidades[0].nombre:
            frecuencias[0] += 1
        elif consulta.ref_especialidad.nombre == especialidades[1].nombre:
            frecuencias[1] += 1
        elif consulta.ref_especialidad.nombre == especialidades[2].nombre:
            frecuencias[2] += 1
        elif consulta.ref_especialidad.nombre == especialidades[3].nombre:
            frecuencias[3] += 1
        elif consulta.ref_especialidad.nombre == especialidades[4].nombre:
            frecuencias[4] += 1

    for indice in range(0, len(frecuencias)):
        if (frecuencias[indice] != 1):
            print('{} - {} veces.'.format(especialidades[indice], frecuencias[indice]))
        else:
            print('{} - {} vez.'.format(especialidades[indice], frecuencias[indice]))

def reporte_recaudado_x_especialidad():
    # Total recaudado por especialidad.
    for indice in range(0, len(frecuencias)):
        print('Recaudado por {} - {}.'.format(especialidades[indice], frecuencias[indice]*consultas[indice].valor_total))


def menu_principal():
    print('Sistema de la Clinica UPS')

    opcion = 'N'
    while opcion == 'N':
        opcion = input('¿Desea ingresar un nuevo paciente? [S-N]: ')
        if opcion == 'N':
            break

        nombre = input('Nombre del Paciente: ')
        apellido = input('Apellido del Paciente: ')
        sexo = input('Sexo [M-F]: ')
        anio_nacimiento = int(input('Año de Nacimiento: '))
        paciente = Paciente(nombre, apellido, sexo, anio_nacimiento)
        
        menu_especialidades()
        subopcion = int(input('Especialidad [1-2-3-4-5]: '))
        especialidad = None
        if (subopcion >=0 and subopcion <=5):
            especialidad = especialidades[subopcion-1]
        else:
            print('No ingresa de manera correcta la especialidad')
        
        fecha_actual = datetime.now()
        consulta = Consulta(fecha_actual, paciente, especialidad)
        consultas.append(consulta)

        opcion = input('¿Desea salir? [S-N]')

    reporte_descuentos_realizados()
    reporte_total_consultas()
    reporte_total_x_sexo()
    reporte_cantidad_x_especialidad()
    reporte_recaudado_x_especialidad()

def menu_especialidades():
    print('Seleccionar la especialidad: ')
    print('1 - Medicina General - $30')
    print('2 - Cardiologia - $35')
    print('3 - Traumatologia - $50')
    print('4 - Dermatologia - $45')
    print('5 - Pediatria - $40')

if __name__ == '__main__':
    menu_principal()


