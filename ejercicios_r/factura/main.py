class Producto:
    # precio sin iva incluido
    def __init__(self, codigo, nombre, precio, iva, cantidad) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.iva = iva
        self.cantidad = cantidad

    def precio_con_iva(self):
        aplica_iva = self.valor_iva()
        precio_con_iva = self.precio + aplica_iva
        return round(precio_con_iva, 0)

    def valor_iva(self):
        # devuelva el valor del iva en el producto
        iva = self.precio*(self.iva/100)
        return round(iva)

    def precio_sin_iva(self, precio_iva):
        constante = 1+(self.iva/100)
        resultado = precio_iva/constante
        self.precio = resultado
        return round(resultado)

    def subtotal(self):
        return self.precio*self.cantidad

    def iva_total(self):
        valor_iva = self.valor_iva()
        return self.cantidad*valor_iva

    def precio_total(self):
        # Retorna precio total iva incluido
        precio_con_iva = self.precio_con_iva()
        return precio_con_iva*self.cantidad

    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return round(self.precio)

    def get_iva(self):
        return self.iva

    def get_cantidad(self):
        return self.cantidad


class Factura:

    def __init__(self, lista) -> None:
        self.lista_productos = lista

    def precio_subtotal(self):
        # precio de todos los productos sin iva
        precio = 0
        for productos in self.lista_productos:
            precio += productos.subtotal()
        return round(precio)

    def valor_iva(self):
        # precio del iva de todos los productos
        valor_iva = 0
        for productos in self.lista_productos:
            valor_iva += productos.iva_total()

        return round(valor_iva)

    def precio_total(self):
        total = 0
        for productos in self.lista_productos:
            total += productos.precio_total()
        return total

    def imprimir_factura(self):
        formato = '-'*85  # es el ancho de la tabla
        print('\n'+formato)
        print('                           F A C T U R A')
        print(formato)
        # este formato rellena un con espacios si el string es de menor espacio
        print('|{:<8}|{:<10}|{:<10}|{:<15}|{:<15}|{:<20}|'.format(
            'Codigo', 'Cantidad', 'Producto', 'Precio unitario', 'Iva', 'Precio iva incluido'))
        iva = 0
        for producto in self.lista_productos:

            print('|{:<8}|{:<10}|{:<10}|{:<15}|{:<7}({}%)   |{:<20}|'.format(
                producto.get_codigo(),
                producto.get_cantidad(),
                producto.get_nombre(),
                producto.get_precio(),
                producto.valor_iva(),
                producto.get_iva(),
                producto.precio_con_iva()))
        print(formato)
        print('|{:<30}|{:<15}|{:<15}|{:<20}|'.format(
            'subtotal ', self.precio_subtotal(), self.valor_iva(), self.precio_total()))
        print(formato)
        print('|{:<62}|{:<20}|'.format(
            'total  total a pagar', self.precio_total()))
        print(formato+'\n')


def run():
    # pedir productos
    # generar una lista de productos
    # generar un formato factura
    # imprimir factura
    # i = int(input('Cuantos productos ingresarás: '))
    lista_productos = list()
    # crear los productos
    producto1 = Producto(1010, 'camiseta', 0, 16, 10)

    producto2 = Producto(1020, 'pantalones', 0, 19, 10)
    # los precios en los productos no estan con iva
    # el objeto lo calcula internamente
    producto1.precio_sin_iva(116000)
    producto2.precio_sin_iva(119000)

    lista_productos.append(producto1)
    lista_productos.append(producto2)

    # se crea un objeto factura
    factura = Factura(lista_productos)
    # el objeto hace los calculos y formatos
    factura.imprimir_factura()

    """
    while i > 0:
        print('\n-------------------------------------------------\n')
        cod_producto = input('Ingrese el código del producto: ')
        nom_producto = input('Ingrese el nombre del producto: ')
        precio_unit_iva = int(input('Ingrese el precio unitario con iva: '))
        cantidad = int(input('Ingrese la cantidad el producto: '))
        iva = int(input('Ingrese el porcentaje del iva (sin simbolo %): '))
        # crear un objeto de tipo Producto
        producto = Producto(
            codigo=cod_producto,
            nombre=nom_producto,
            precio=0,
            iva=iva,
            cantidad=cantidad)
        # el precio está con iva
        # definimos el precio sin iva
        producto.precio_sin_iva(precio_unit_iva)

        # agregar el producto a la lista de compra
        lista_productos.append(producto)
        i -= 1
        """


if __name__ == '__main__':
    run()
