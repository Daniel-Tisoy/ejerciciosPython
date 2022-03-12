# calcular número de meses entre 1951 y 2002
# hayar cantidad de años
def num_anios(anio_inicial, anio_final):
    return anio_final - anio_inicial


def calcular_meses():
    numero_anios = num_anios(1951, 2002)
    cant_meses = numero_anios * 12
    return cant_meses


def main():
    print(calcular_meses())


if __name__ == "__main__":
    main()
