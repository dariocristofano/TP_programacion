def validar_entero(mensaje: str) -> int:
    '''
    valida que el input sea un numero entero positivo
    recibe el mensaje a mostrar
    retorna el numero validado
    '''
    numero = input(mensaje)
    es_valido = True

    for i in range(len(numero)):
        if ord(numero[i]) < 48 or ord(numero[i]) > 57:
            es_valido = False

    if es_valido and len(numero) > 0:
        return int(numero)

    print("Opcion invalida")
    return validar_entero(mensaje)


def validar_indice(mensaje: str, cantidad: int) -> int:
    '''
    pide un numero entre 1 y cantidad
    retorna el indice correspondiente (base 0)
    '''
    opcion = validar_entero(mensaje) - 1

    while opcion < 0 or opcion >= cantidad:
        print("Opcion invalida")
        opcion = validar_entero(mensaje) - 1

    return opcion


def obtener_claves(diccionario: dict) -> list:
    '''
    retorna una lista con las claves de un diccionario
    recibe un diccionario
    retorna una lista con las claves
    '''
    claves = []

    for clave in diccionario:
        claves.append(clave)

    return claves
