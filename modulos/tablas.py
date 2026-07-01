from modulos.reutilizables import validar_entero, validar_indice, obtener_nombres, validar_valor_numerico
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


def cargar_tabla_validada(tabla: list) -> None:
    '''
    carga los datos en una matriz validando que cada columna sea tipo consistente
    no permite mezclar numeros con texto en la misma columna
    recibe la matriz
    no retorna nada
    '''
    columnas = len(tabla[0])
    tipos_columnas = []

    for j in range(columnas):
        tipos_columnas.append(False)

    for j in range(columnas):
        tabla[0][j] = input(f"Nombre de la columna {j+1}: ")

    for i in range(1, len(tabla)):

        for j in range(columnas):

            while True:

                valor = input (f"Fila {i} - {tabla[0][j]}: ")

                if len(valor) == 0:
                    print("ERROR: el valor no puede estar vacio.")

                elif tipos_columnas[j] == False:

                    if validar_valor_numerico(valor) == True:
                        tipos_columnas[j] = "numerico"
                    else:
                        tipos_columnas[j] = "texto"
                    tabla[i][j] = valor
                    break



                elif tipos_columnas[j] == "numerico":
                    if validar_valor_numerico(valor) == True:
                        tabla[i][j] = valor
                        break
                    else:
                        print(f"ERROR: '{tabla[0][j]}' es numerica. Ingrese un numero.")

                else:
                    if validar_valor_numerico(valor) == False:
                        tabla[i][j] = valor
                        break
                    else:
                        print(f"ERROR: '{tabla[0][j]}' es texto. No ingrese numeros.")


def agregar_tabla(proyectos: list) -> None:
    '''
    crea y carga una tabla y la agrega al proyecto elegido
    recibe la lista de proyectos
    no retorna nada
    '''
    proyecto = elegir_proyecto(proyectos)

    nombre = input("Nombre de la tabla: ")
    filas = validar_entero("Cuantas filas de datos?: ")
    columnas = validar_entero("Cuantas columnas?: ")

    tabla = crear_tabla(filas, columnas)
    cargar_tabla_validada(tabla)

    proyecto["tablas"].append({"nombre": nombre, "matriz": tabla})

    print(f"Tabla '{nombre}' agregada exitosamente")


def elegir_tabla(proyectos: list) -> list:
    '''
    permite elegir un proyecto y luego una tabla dentro de el
    recibe la lista de proyectos
    retorna la matriz de la tabla elegida o False si no hay tablas
    '''
    proyecto = elegir_proyecto(proyectos)
    tablas = proyecto["tablas"]
    nombres = obtener_nombres(tablas)

    if len(nombres) == 0:
        print("Este proyecto no tiene tablas")
        return False

    for i in range(len(nombres)):
        print(f"  {i+1}. {nombres[i]}")

    eleccion = validar_indice("Que tabla?: ", len(nombres))
    return tablas[eleccion]["matriz"]


def modificar_tabla(proyectos: list) -> None:
    '''
    modifica un elemento especifico de una tabla
    recibe la lista de proyectos
    no retorna nada
    '''
    tabla = elegir_tabla(proyectos)

    if tabla == False:
        return

    fila = validar_indice("Que fila desea modificar?: ", len(tabla) - 1) + 1
    columna = validar_indice("Que columna desea modificar?: ", len(tabla[0]))

    es_numerica = False

    for i in range(1, len(tabla)):

        if validar_valor_numerico(tabla[i][columna]) == True:
            es_numerica = True

    while True:
        elemento = input("Nuevo valor: ")

        if len(elemento) == 0:
            print("ERROR: el valor no puede estar vacio.")

        elif es_numerica == True and validar_valor_numerico(elemento) == False:
            print("ERROR: la columna es numerica. Ingrese un numero.")

        elif es_numerica == False and validar_valor_numerico(elemento) == True:
            print("ERROR: la columna es de texto. No ingrese numeros.")

        else:
            break

    tabla[fila][columna] = elemento
    print("Modificado correctamente")


def mostrar_tabla(tabla: list) -> None:
    '''
    muestra una tabla completa con formato prolijo
    recibe la matriz
    no retorna nada
    '''
    lineas = "─" * (15 * len(tabla[0]))

    print(lineas)
    print("|", end="")
    for j in range(len(tabla[0])):
        print(f"{tabla[0][j]:<15}", end="|")
    print()

    for i in range(1, len(tabla)):
        print(lineas)
        print("|", end="")
        for j in range(len(tabla[i])):
            print(f"{tabla[i][j]:<15}", end="|")
        print()

    print(lineas)


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
