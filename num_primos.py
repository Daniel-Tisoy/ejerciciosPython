def es_primo(numero):
    resultado = True
    counter = 0
    for divisor in range(2, numero):
        if (numero % divisor) == 0:
            resultado = False
            break
        counter += 1
    return (resultado, counter)
print(es_primo(13))

