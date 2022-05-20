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

def costoTotal(listaPaquetes, descuento):
    # la funcion recibe una lista de diccionarios

    costoTotalEnvio = 0

    for paquete in listaPaquetes:
        # extraer los datos de la lista
        alto, ancho, profundo = paquete["ALTO"], paquete["ANCHO"], paquete["PROFUNDO"]
        costoEnvio = calcularCosto(alto, ancho, profundo)

        costoTotalEnvio += costoEnvio

    costoDescuento = (costoTotalEnvio*descuento)/100
    costoTotalEnvio -= costoDescuento

    return costoTotalEnvio

