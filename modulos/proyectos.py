from modulos.reutilizables import validar_indice, obtener_nombres


def crear_proyecto(proyectos: list) -> None:
    '''
    crea un nuevo proyecto y lo agrega a la lista de proyectos
    recibe la lista de proyectos
    no retorna nada
    '''
    nombre = input("Ingrese el nombre del proyecto: ")
    proyectos.append({"nombre": nombre, "tablas": []})
    print(f"Proyecto '{nombre}' creado exitosamente")


def elegir_proyecto(proyectos: list) -> dict:
    '''
    muestra los proyectos disponibles y permite elegir uno
    recibe la lista de proyectos
    retorna el diccionario del proyecto elegido
    '''
    nombres = obtener_nombres(proyectos)

    for i in range(len(nombres)):
        print(f"  {i+1}. {nombres[i]}")

    eleccion = validar_indice("Que proyecto?: ", len(nombres))
    return proyectos[eleccion]


def eliminar_proyecto(proyectos:list) -> None:
    pass


def mostrar_proyecto(proyectos: list) -> None:
    '''
    muestra la informacion de un proyecto
    recibe la lista de proyectos
    no retorna nada
    '''
    proyecto = elegir_proyecto(proyectos)
    tablas = proyecto["tablas"]

    print(f"Tablas: {len(tablas)}")

    for i in range(len(tablas)):
        print(f"  {i+1}. {tablas[i]['nombre']}")


def mostrar_menu_proyectos(proyectos: list) -> None:
    '''
    submenu para gestionar proyectos
    recibe la lista de proyectos
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
