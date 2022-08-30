import time
import locale

locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
d1 = time.strftime("%A, %d. %B %Y %I:%M%p")
print(d1) 

locale.setlocale(locale.LC_ALL, 'es_EC.UTF8')
d2 = time.strftime("%A, %d de %B %Y %I:%M%p")
print(d2)

