from Paciente import *
from Consulta import *
from Especialidad import *

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

for consulta in consultas:
    print(consulta)