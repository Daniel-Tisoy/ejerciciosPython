# calcular volumen y costo de envio de un paquete
# costo de envio = volumen * 5
# agregar la caracteristica de calcular varios paquetes
numeroPaquetes = int(input())
costoTotal = 0

for i in range(1, numeroPaquetes+1):
    # crear tres variables [alto-ancho-profundo]
    alto = float(input())
    ancho = float(input())
    profundo = float(input())
    # calcular volumen
    volumen = alto * ancho * profundo
    # calcular costo de envio
    costo_envio = volumen * 5
    if alto>30:
        costo_envio += 2000

    if costo_envio > 10000:
        valor_iva = (costo_envio * 19)/100
        costo_envio += valor_iva
    costoTotal += costo_envio
    # imprimir volumen y costo
    print(volumen)
    print(costo_envio)
print(costoTotal)
