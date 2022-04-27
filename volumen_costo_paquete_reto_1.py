# calcular volumen y costo de envio de un paquete
# costo de envio = volumen * 5
# crear tres variables [alto-ancho-profundo]
alto = float(input())
ancho = float(input())
profundo = float(input())
# calcular volumen
volumen = alto * ancho * profundo
# calcular costo de envio
costo_envio = volumen * 5
# imprimir volumen y costo
print(volumen)
print(costo_envio)
