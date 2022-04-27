# dividir entre dos numeros diferentes de 0
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

if b != 0:
    print("La division es: ", a / b)
# de lo contrario, mostrar mensaje de error
else:
    print("No se puede dividir entre 0")
