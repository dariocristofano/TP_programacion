
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
    else:
        print("Opcion invalida")
        return validar_entero(mensaje)
    

def elegir_tabla(tablas: list) -> dict:
    '''
    muestra las tablas disponibles y permite elegir una
    recibe la lista de tablas
    retorna el diccionario de la tabla elegida
    '''
    for i in range(len(tablas)):
        print(f"{i+1}. {tablas[i]['nombre']}")

    eleccion = validar_indice("Que tabla?: ", len(tablas)) 
    return tablas[eleccion]

#esta funcion se usa en el punto c y d

def validar_indice(mensaje: str, cantidad: int) -> int:
    '''
    pide un número entre 1 y cantidad
    retorna el índice correspondiente
    '''
    opcion = validar_entero(mensaje) - 1

    while opcion < 0 or opcion >= cantidad:
        print("Opcion invalida")
        opcion = validar_entero(mensaje) - 1

    return opcion