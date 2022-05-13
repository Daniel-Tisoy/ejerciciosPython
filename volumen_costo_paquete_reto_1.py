# calcular volumen y costo de envio de un paquete
# costo de envio = volumen * 5
def calcularCosto(alto, ancho, profundo):

    volumen = alto * ancho * profundo
    costoEnvio = volumen * 5

    if alto>30:
        costoEnvio += 2000

    if costoEnvio > 10000:
        valorIva = (costoEnvio * 19)/100
        costoEnvio += valorIva

    return costoEnvio

def costoTotal(numeroPaquetes, descuento):

    costoTotalEnvio = 0

    for i in range(1, numeroPaquetes+1):
        # crear tres variables [alto-ancho-profundo]
        alto = float(input("inserte valor:"))
        ancho = float(input("inserte valor:"))
        profundo = float(input("inserte valor:"))

        costoEnvio = calcularCosto(alto, ancho, profundo)

        costoTotalEnvio += costoEnvio

    costoDescuento = (costoTotalEnvio*descuento)/100
    costoTotalEnvio -= costoDescuento

    return costoTotalEnvio

print(calcularCosto(35,10,5))
print(costoTotal(2, 50))
