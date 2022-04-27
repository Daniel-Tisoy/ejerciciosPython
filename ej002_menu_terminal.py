# solicitar dos numeros
a, b = input("Ingrese dos numeros: ").split()

# elaborar un menu de opciones suma resta multiplicar dividir
print("*** menu principal ***")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Salir")
# digitar una opcion
opcion = int(input("Ingrese una opcion: "))
# realizar la operacion
if opcion == 1:
    print("La suma es: ", int(a) + int(b))
elif opcion == 2:
    print("La resta es: ", int(a) - int(b))
elif opcion == 3:
    print("La multiplicacion es: ", int(a) * int(b))
elif opcion == 4:
    print("La division es: ", int(a) / int(b))
else:
    print("Opcion no valida")
