# Solicitar un valor y determinar si es o no un numero
numero = input("Ingrese un numero: ")
try:
    numero = int(numero)
    print("El numero ingresado es un numero")
except ValueError:
    print("El numero ingresado no es un numero")
    print(numero)

if int(numero):
    print("El numero ingresado es un numero")
else:
    print("El numero ingresado no es un numero")