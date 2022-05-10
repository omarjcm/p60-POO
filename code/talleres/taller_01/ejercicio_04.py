import time
from datetime import datetime, timedelta  

fecha_1 = '10-05-2022'
fecha_2 = '02-05-2022'

format_fecha_1 = time.strptime(fecha_1, '%d-%m-%Y')
format_fecha_2 = time.strptime(fecha_2, '%d-%m-%Y')

print(format_fecha_1 < format_fecha_2)

fecha_actual = datetime.now()
print(fecha_actual)

fecha_ayer = fecha_actual - timedelta(days=2)
print(fecha_ayer)