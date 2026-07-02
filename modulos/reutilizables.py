def validar_entero(mensaje: str) -> int:
    '''
    valida que el input sea un numero entero positivo
    recibe el mensaje a mostrar
    retorna el numero validado
    '''
    es_valido = False

    while es_valido == False:
        numero = input(mensaje)
        es_valido = len(numero) > 0

        for i in range(len(numero)):
            if ord(numero[i]) < 48 or ord(numero[i]) > 57:
                es_valido = False

        if es_valido == False:
            print("Opcion invalida")

    return int(numero)


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


def obtener_nombres(lista: list) -> list:
    '''
    retorna una lista con el valor de la clave "nombre" de cada diccionario
    recibe una lista de diccionarios que contienen la clave "nombre"
    (sirve tanto para la lista de proyectos como para la lista de tablas)
    retorna una lista de strings con los nombres
    '''
    nombres = []

    for i in range(len(lista)):
        nombres.append(lista[i]["nombre"])

    return nombres


def validar_valor_numerico(valor: str) -> bool:
    '''
    valida si un string representa un numero entero o decimal
    recibe el string a verificar
    retorna True si es numerico, False si no
    '''
    es_valido = True
    tiene_punto = False
    inicio = 0

    if len(valor) == 0:
        es_valido = False

    elif ord(valor[0]) == 45:
        inicio = 1

        if len(valor) == 1:
            es_valido = False

    if es_valido == True:
        for j in range(inicio, len(valor)):
            
            if ord(valor[j]) == 46 and tiene_punto == False:
                tiene_punto = True
            elif ord(valor[j]) < 48 or ord(valor[j]) > 57:
                es_valido = False

    return es_valido

#  "-  3 . aq 14"

# "-"