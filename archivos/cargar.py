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


def cargar_proyectos() -> list:
    '''
    carga los proyectos desde el archivo csv
    no recibe parametros
    retorna la lista de proyectos (lista de diccionarios)
    '''
    archivo = open("archivos/proyectos.csv", "r")
    proyectos = []
    proyecto_actual = False
    tabla_actual = False
 
    for linea in archivo:
        valores = separar_linea(linea)
 
        if len(valores) == 0:
            continue
 
        if valores[0] == "PROYECTO":
            nuevo_proyecto = {"nombre": valores[1], "tablas": []}
            proyectos.append(nuevo_proyecto)
            proyecto_actual = nuevo_proyecto
            tabla_actual = False
 
        elif valores[0] == "TABLA":
            nueva_tabla = {"nombre": valores[1], "matriz": []}
            proyecto_actual["tablas"].append(nueva_tabla)
            tabla_actual = nueva_tabla["matriz"]
 
        else:
            if tabla_actual != False:
                tabla_actual.append(valores)
 
    archivo.close()
    return proyectos



