# hacer un programa que calcule un impuesto con iva del 19%:
# el resultado, el precion basico del producto.
# El valor del impuesto;
# El presion total del producto,
IVA = 0.19
prec_prod = int(input('Digite el precio del producto: '))
impuesto = prec_prod * IVA
total = prec_prod + impuesto
print('-------------factura---------------\n')
print('precio basico: {}'.format(prec_prod))
print('impuesto: {}'.format(impuesto))
print('precio total iva incluido {}'.format(total))