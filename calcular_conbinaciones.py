from mis_funciones_math import factorial, combinaciones

n = int(input('Ingrese valor de n: '))
r = int(input('Ingrese valor de r: '))

nc = combinaciones(n, r)

print(f'''
n = {n},
r = {r},
Factorial de n = {factorial(n)},
Factorial de r = {factorial(r)},
Factorial de n-r = {factorial(n-r)},
Numero de combinaciones = {nc}''')
