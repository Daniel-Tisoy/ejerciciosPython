operaciones_usuario = ["Definamos qué es una función de Python: ",
                       "Una función es ",
                       "un arreglo unidimensional de datos",
                       "DESHACER",
                       "DESHACER",
                       "REHACER",
                       "un grupo de instrucciones"]


def deshacer_accion(pila_texto_escrito, var_texto_actual):

    var_pila_rehacer = var_texto_actual
    var_texto_actual = pila_texto_escrito.pop()

    result = (pila_texto_escrito, var_texto_actual, var_pila_rehacer)
    return result


def rehacer_accion(pila_rehacer, var_texto_actual):
    var_pila_texto_escrito = var_texto_actual
    var_texto_actual = pila_rehacer.pop()

    result = (pila_rehacer, var_texto_actual, var_pila_texto_escrito)

    return result


def actualizar_estado_editor(operaciones_usuario):
    texto_escrito = list()
    texto_actual = ''
    deshacer = list()

    for i in range(len(operaciones_usuario)):
        if operaciones_usuario[i] == 'deshacer'.upper():
            var_deshacer_accion = deshacer_accion(texto_escrito, texto_actual)
            texto_escrito = var_deshacer_accion[0]
            texto_actual = var_deshacer_accion[1]
            deshacer.append(var_deshacer_accion[2])
            continue
        elif operaciones_usuario[i] == 'rehacer'.upper():
            var_rehacer_accion = rehacer_accion(deshacer, texto_actual)
            texto_escrito.append(var_rehacer_accion[2])
            texto_actual = var_rehacer_accion[1]
            deshacer = var_rehacer_accion[0]
            continue

        texto_escrito.append(texto_actual)
        texto_actual = operaciones_usuario[i]
        deshacer = list()

    texto = texto_escrito[0].join(texto_escrito[1:]) + texto_actual
    return texto


print(actualizar_estado_editor(operaciones_usuario))
