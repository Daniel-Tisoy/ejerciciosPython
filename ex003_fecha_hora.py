# Ejercicio 3: obtener la fecha y hora actuales del sistema
from datetime import datetime

dt = datetime.now()
print('\n', dt, '\n')
print('fecha:')
print(dt.year, dt.month, dt.day, sep='/')
print('\nHora: ')
print(dt.hour, dt.minute, sep=':')

# usar formato strftime
print(dt.strftime('%d/%m/%Y -> %H: %M: %S'))
