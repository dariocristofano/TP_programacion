def separar_linea(linea: str) -> list:
    '''
    separa una linea csv en una lista de valores
    recibe la linea como string
    retorna una lista con los valores
    '''
    valores = []
    valor_actual = ""

    for i in range(len(linea)):

        if ord(linea[i]) == 44:
            valores.append(valor_actual)
            valor_actual = ""

        elif ord(linea[i]) == 10 or ord(linea[i]) == 13:
            pass

        else:
            valor_actual += linea[i]

    if len(valor_actual) > 0:
        valores.append(valor_actual)

    return valores


def cargar_usuarios() -> list:
    '''
    carga los usuarios desde el archivo csv
    no recibe parametros
    retorna la lista de usuarios
    '''
    archivo = open("archivos/usuarios.csv", "r")
    usuarios = []

    for linea in archivo:
        valores = separar_linea(linea)

        if len(valores) == 2:
            usuarios.append([valores[0], valores[1]])

    archivo.close()
    return usuarios






