from reutilizables import validar_entero, validar_indice

#sprint 3


def crear_tabla(tablas: list) -> None:
    '''
    crea una tabla con columnas y filas ingresadas por el usuario
    recibe la lista de tablas
    no retorna nada
    '''
    nombre = input("Nombre de la tabla: ")

    filas = validar_entero("Cuantas filas quiere?: ")
    columnas = validar_entero("Cuantas columnas quiere?: ")

    matriz = []
    columnas_lista = []

    for i in range(columnas):
        columna_nombre = input(f"Ingrese el nombre de la columna {i+1}: ")
        columnas_lista.append(columna_nombre)

    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            elemento = input(f"Ingrese el elemento de la fila {i+1} columna {columnas_lista[j]}: ")
            matriz[i].append(elemento)

    tabla = {
        "nombre": nombre,
        "columnas": columnas_lista,
        "filas": matriz
    }
    tablas.append(tabla)
    print(f"Tabla {nombre} creada exitosamente")


def modificar_tablas(tablas: dict) -> None:
    '''
    modifica un elemento especifico de una tabla
    recibe un diccionario de tabla
    no retorna nada
    '''
    fila = validar_indice(
        "Que fila desea modificar?: ",
        len(tablas['filas'])
    )

    columna = validar_indice(
        "Que columna desea modificar?: ",
        len(tablas['columnas'])
    )

    elemento = input("Que elemento quiere ingresar: ")
    tablas["filas"][fila][columna] = elemento


def mostrar_tabla(tablas: dict) -> None:
    '''
    muestra una tabla completa con formato prolijo
    recibe un diccionario de tabla
    no retorna nada
    '''
    lineas = "─" * (15 * len(tablas["columnas"]))

    print(lineas)
    print("|", end="")
    for i in range(len(tablas["columnas"])):
        print(f"{tablas['columnas'][i]:<15}", end="|")
    print()

    for i in range(len(tablas["filas"])):
        print(lineas)
        print("|", end="")
        for j in range(len(tablas["filas"][i])):
            print(f"{tablas['filas'][i][j]:<15}", end="|")
        print()

    print(lineas)


def mostrar_columna(tablas: dict) -> None:
    '''
    muestra una columna especifica de una tabla
    recibe un diccionario de tabla
    no retorna nada
    '''
    columna = validar_indice(
        "Que columna desea ver?: ",
        len(tablas["columnas"])
    )

    print(tablas["columnas"][columna])
    for i in range(len(tablas["filas"])):
        print(tablas["filas"][i][columna])


def mostrar_fila(tablas: dict) -> None:
    '''
    muestra una fila especifica de una tabla
    recibe un diccionario de tabla
    no retorna nada
    '''

    fila = validar_indice(
        "Que fila desea ver?: ",
        len(tablas["filas"])
    )

    for i in range(len(tablas["filas"][fila])):
        print(tablas["filas"][fila][i], end=" ")
    print()


















    


