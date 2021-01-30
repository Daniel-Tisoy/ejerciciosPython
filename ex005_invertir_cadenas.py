# ejercicio 5: Obtener la representación inversa de una cadena de caracteres.
# Python --> nohtyP

cadena = 'Python'
# solucion 1
lista_inversa = list()
for i in range(len(cadena)-1, -1, -1):
    # len -1 para determinal el rango
    # -1 debido a que el rango no incluye al mismo número
    # -1 para indicar decremento
    lista_inversa.append(cadena[i])
resultado = ''.join(lista_inversa)
print(resultado)

# solucion 2
lista_inversa = list()
for i in cadena:
    lista_inversa.append(i)
print(''.join(lista_inversa[::-1]))

# solucion 3
lista_inversa.reverse()
print(''.join(lista_inversa))

# solucion 4
print(cadena[::-1])  # [inicio : final : orden de lectura]

# solucion 5
for i in range(len(cadena)-1, -1, -1):
    print(cadena[i], end='')
print(end='\n')