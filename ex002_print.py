# Ejercicio 2: Exponer el uso básico de la función print

print('Ejemplo básico')

# salto de linea
print('Ejemplo básico.', end=' ')
print('Ejemplo básico.') 

# separadores
print('\nSoy', 'un', 'Programador')
print('Soy', 'un', 'Programador', sep='-')

# placeholders
print('\n{} un {}'.format('Soy', 'Programador'))

# imprimir objetos
numeros = [2,3,4,7,90]
print('\n', numeros, sep='')

capitales = {'Colombia': 'Bogotá', 'Perú': 'Lima'}
print('\n', capitales, sep='')