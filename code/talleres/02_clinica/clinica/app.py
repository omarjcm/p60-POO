from Paciente import *
from Consulta import *
from Especialidad import *
from datetime import datetime

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

def menu_especialidades():
    print('Seleccionar la especialidad: ')
    print('1 - Medicina General - $30')
    print('2 - Cardiologia - $35')
    print('3 - Traumatologia - $50')
    print('4 - Dermatologia - $45')
    print('5 - Pediatria - $40')

if __name__ == '__main__':
    menu_principal()