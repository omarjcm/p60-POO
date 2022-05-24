from Paciente import *
from Consulta import *

paciente1 = Paciente('Pablo', 'Banderas', 'M', '1996')
#print(paciente1.__nombre)
#print(paciente1.getNombre())
print(paciente1.nombre)
paciente1.apellido = 'Banderas Alcivar'
print(paciente1.apellido)

consulta1 = Consulta('01-02-2022', None, None)
print(consulta1.fecha_consulta)