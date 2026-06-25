from modulos.reutilizables import validar_entero, validar_indice, obtener_claves
from modulos.proyectos import elegir_proyecto


def crear_tabla(filas: int, columnas: int) -> list:
    '''
    crea una matriz vacia de (filas+1) x columnas
    la fila 0 es para los encabezados
    recibe cantidad de filas de datos y cantidad de columnas
    retorna la matriz vacia
    '''
    matriz = []

    for i in range(filas + 1):
        fila = []

        for j in range(columnas):
            fila.append("")

        matriz.append(fila)

    return matriz


def cargar_tabla(tabla: list) -> None:
    '''
    carga los datos en una matriz ya creada
    fila 0 se carga con nombres de columnas
    filas siguientes con los datos
    recibe la matriz
    no retorna nada
    '''
    columnas = len(tabla[0])

    for j in range(columnas):
        tabla[0][j] = input(f"Nombre de la columna {j+1}: ")

    for i in range(1, len(tabla)):
        for j in range(columnas):
            tabla[i][j] = input(f"Fila {i} - {tabla[0][j]}: ")


def agregar_tabla(proyectos: dict) -> None:
    '''
    crea y carga una tabla y la agrega al proyecto elegido
    recibe el diccionario de proyectos
    no retorna nada
    '''
    proyecto = elegir_proyecto(proyectos)

    nombre = input("Nombre de la tabla: ")
    filas = validar_entero("Cuantas filas de datos?: ")
    columnas = validar_entero("Cuantas columnas?: ")

    tabla = crear_tabla(filas, columnas)
    cargar_tabla(tabla)

    proyecto["tablas"][nombre] = tabla

    print(f"Tabla '{nombre}' agregada exitosamente")


def elegir_tabla(proyectos: dict) -> list:
    '''
    permite elegir un proyecto y luego una tabla dentro de el
    recibe el diccionario de proyectos
    retorna la matriz de la tabla elegida o None si no hay tablas
    '''
    proyecto = elegir_proyecto(proyectos)
    tablas = proyecto["tablas"]
    claves = obtener_claves(tablas)

    if len(claves) == 0:
        print("Este proyecto no tiene tablas")
        return None

    for i in range(len(claves)):
        print(f"  {i+1}. {claves[i]}")

    eleccion = validar_indice("Que tabla?: ", len(claves))
    return tablas[claves[eleccion]]


def modificar_tabla(proyectos: dict) -> None:
    '''
    modifica un elemento especifico de una tabla
    recibe el diccionario de proyectos
    no retorna nada
    '''
    tabla = elegir_tabla(proyectos)

    if tabla == None:
        return

    fila = validar_indice("Que fila desea modificar?: ", len(tabla) - 1) + 1
    columna = validar_indice("Que columna desea modificar?: ", len(tabla[0]))

    elemento = input("Nuevo valor: ")
    tabla[fila][columna] = elemento

    print("Modificado correctamente")


def mostrar_tabla(tabla: list) -> None:
    '''
    muestra una tabla completa con formato prolijo
    recibe la matriz
    no retorna nada
    '''
    ancho = 15
    sep = "+" + ("-" * ancho + "+") * len(tabla[0])

    print(sep)

    encabezado = "|"
    for j in range(len(tabla[0])):
        encabezado += tabla[0][j][:ancho].center(ancho) + "|"
    print(encabezado)

    for i in range(1, len(tabla)):
        print(sep)
        fila_str = "|"
        for j in range(len(tabla[i])):
            fila_str += tabla[i][j][:ancho].ljust(ancho) + "|"
        print(fila_str)

    print(sep)


def mostrar_columna(tabla: list) -> None:
    '''
    muestra una columna especifica de una tabla
    recibe la matriz
    no retorna nada
    '''
    for i in range(len(tabla[0])):
        print(f"  {i+1}. {tabla[0][i]}")

    columna = validar_indice("Que columna desea ver?: ", len(tabla[0]))

    print(f"\n  {tabla[0][columna]}")
    print("  " + "-" * 15)

    for i in range(1, len(tabla)):
        print(f"  {tabla[i][columna]}")


def mostrar_fila(tabla: list) -> None:
    '''
    muestra una fila especifica de una tabla
    recibe la matriz
    no retorna nada
    '''
    fila = validar_indice("Que fila desea ver?: ", len(tabla) - 1) + 1

    print()

    for j in range(len(tabla[0])):
        print(f"  {tabla[0][j]}: {tabla[fila][j]}")
