nombreCompleto = input("Ingrese su nombre completo: ")
edadAnio = int(input("¿Cuantos años de antiguedad en nuesta empresa tiene?: "))

if (edadAnio <= 1):
    print("Bienvenido", nombreCompleto, "usted tiene", edadAnio, "año")
else:
    print("Bienvenido", nombreCompleto, "usted tiene", edadAnio, "años")
