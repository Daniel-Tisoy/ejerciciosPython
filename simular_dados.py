import random

def lanzar_dados():
    """ simulará la accion de lanzar dados,
    devolviendo una tupla con dos valores enteros"""
    lista_numeros = [1,2,3,4,5,6]
    lanzar = random.choices(lista_numeros, k=2)
    return lanzar

if __name__ == "__main__":

    print(r"Iniciando Juego :)")

    jugando = True

    while jugando == True:

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
            #lower para convertir en minuscula el input
            print("Juego finalizado")
            jugando = False
