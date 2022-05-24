from Paciente import *
from Consulta import *

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

for paciente in pacientes:
    print(paciente.nombre)