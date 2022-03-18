import random

def lanzar_dados():
    """ simulará la accion de lanzar dados,
    devolviendo una tupla con dos valores enteros"""
    num_aleatorio1 = random.randint(1, 6)
    num_aleatorio2 = random.randint(1,6)
    return (num_aleatorio1, num_aleatorio2)

if __name__ == "__main__":

    print(r"Iniciando Juego :)")

    jugando = True

    while jugando:

        # elegir dos números al aleatorios entre 1 y 6
        lanza_dados = lanzar_dados()

        # el programa debe imprimirlos en pantalla
        print("Resultados lanzamiento:")
        print("Dado 1: ",lanza_dados[0]) 
        print("Dado 2: ",lanza_dados[1]) 
        
        # imprimir su suma
        print("suma: ", lanza_dados[0]+lanza_dados[1])
        
        # preguntar al usuario si quiere tirar otra vez
        nuevo_intento = input("¿Desea lanzar de nuevo?[y/n]: ")
        if nuevo_intento.lower() != "y":
            #lower para convertir en minuscula
            print("Juego finalizado")
            jugando = False
