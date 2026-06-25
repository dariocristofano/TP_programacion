from modulos.reutilizables import validar_indice, obtener_claves


def crear_proyecto(proyectos: dict) -> None:
    '''
    crea un nuevo proyecto en el diccionario de proyectos
    recibe el diccionario de proyectos
    no retorna nada
    '''
    nombre = input("Ingrese el nombre del proyecto: ")
    proyectos[nombre] = {"tablas": {}}
    print(f"Proyecto '{nombre}' creado exitosamente")


def elegir_proyecto(proyectos: dict) -> dict:
    '''
    muestra los proyectos disponibles y permite elegir uno
    recibe el diccionario de proyectos
    retorna el diccionario del proyecto elegido
    '''
    claves = obtener_claves(proyectos)

    for i in range(len(claves)):
        print(f"  {i+1}. {claves[i]}")

    eleccion = validar_indice("Que proyecto?: ", len(claves))
    return proyectos[claves[eleccion]]


def eliminar_proyecto(proyectos: dict) -> None:
    '''
    elimina un proyecto del diccionario de proyectos
    recibe el diccionario de proyectos
    no retorna nada
    '''
    claves = obtener_claves(proyectos)

    for i in range(len(claves)):
        print(f"  {i+1}. {claves[i]}")

    eleccion = validar_indice("Que proyecto desea eliminar?: ", len(claves))
    nombre = claves[eleccion]
    del proyectos[nombre]
    print(f"Proyecto '{nombre}' eliminado exitosamente")


def mostrar_proyecto(proyectos: dict) -> None:
    '''
    muestra la informacion de un proyecto
    recibe el diccionario de proyectos
    no retorna nada
    '''
    proyecto = elegir_proyecto(proyectos)
    claves_tablas = obtener_claves(proyecto["tablas"])

    print(f"Tablas: {len(claves_tablas)}")

    for i in range(len(claves_tablas)):
        print(f"  {i+1}. {claves_tablas[i]}")


def mostrar_menu_proyectos(proyectos: dict) -> None:
    '''
    submenu para gestionar proyectos
    recibe el diccionario de proyectos
    no retorna nada
    '''
    print()
    print("1. Crear proyecto")
    print("2. Mostrar proyecto")
    print("3. Eliminar proyecto")

    opcion = input("Elija una opcion: ")

    if opcion == "1":
        crear_proyecto(proyectos)

    elif opcion == "2":
        if len(proyectos) == 0:
            print("No hay proyectos cargados")
        else:
            mostrar_proyecto(proyectos)

    elif opcion == "3":
        if len(proyectos) == 0:
            print("No hay proyectos cargados")
        else:
            eliminar_proyecto(proyectos)

    else:
        print("Opcion invalida")
