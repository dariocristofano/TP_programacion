from modulos import *
from archivos import *


usuarios = cargar_usuarios()
proyectos = cargar_proyectos()


def registrar_usuario() -> None:
    '''
    registra un nuevo usuario en la lista de usuarios
    no recibe parametros
    no retorna nada
    '''
    usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Establezca una contrasena: ")

    usuarios.append([usuario, contrasena])
    guardar_usuarios(usuarios)

    print(f"Usuario '{usuario}' registrado exitosamente")


def iniciar_sesion() -> bool:
    '''
    valida el inicio de sesion del usuario
    no recibe parametros
    retorna True si el login fue exitoso, False si no
    '''
    usuario = input("Usuario: ")
    contrasena = input("Contrasena: ")

    for i in range(len(usuarios)):
        if usuarios[i][0] == usuario and usuarios[i][1] == contrasena:
            print(f"Bienvenido {usuario}")
            return True

    print("Usuario o contrasena incorrectos")
    return False


def menu_login() -> None:
    '''
    menu de inicio de sesion o registro
    usa recursividad para reintentos
    no recibe parametros
    no retorna nada
    '''
    print()
    print("1. Iniciar sesion")
    print("2. Registrarse")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        exito = iniciar_sesion()
        if exito == False:
            menu_login()

    elif opcion == "2":
        registrar_usuario()

    else:
        print("Opcion invalida")
        menu_login()


def menu_mostrar() -> None:
    '''
    submenu para mostrar tabla completa, columna o fila
    no recibe parametros
    no retorna nada
    '''
    tabla = elegir_tabla(proyectos)

    if tabla == False:
        return

    print()
    print("1. Tabla completa")
    print("2. Una columna")
    print("3. Una fila")

    opcion = input("Que desea ver?: ")

    if opcion == "1":
        mostrar_tabla(tabla)

    elif opcion == "2":
        mostrar_columna(tabla)

    elif opcion == "3":
        mostrar_fila(tabla)

    else:
        print("Opcion invalida")
        menu_mostrar()


def menu_principal() -> None:
    '''
    bucle principal del programa
    no recibe parametros
    no retorna nada
    '''
    corriendo = True

    while corriendo:
        print()
        print("----- MENU -----")
        print("A. Proyectos")
        print("B. Tablas")
        print("C. Variables")
        print("D. Mostrar")
        print("E. Estadistica")
        print("F. Salir")
        print()

        opcion = input("Ingrese una opcion: ")

        if opcion == "A" or opcion == "a":
            mostrar_menu_proyectos(proyectos)

        elif opcion == "B" or opcion == "b":
            if len(proyectos) == 0:
                print("No hay proyectos cargados")
            else:
                agregar_tabla(proyectos)

        elif opcion == "C" or opcion == "c":
            if len(proyectos) == 0:
                print("No hay proyectos cargados")
            else:
                modificar_tabla(proyectos)

        elif opcion == "D" or opcion == "d":
            if len(proyectos) == 0:
                print("No hay proyectos cargados")
            else:
                menu_mostrar()

        elif opcion == "E" or opcion == "e":
            if len(proyectos) == 0:
                print("No hay proyectos cargados")
            else:
                mostrar_menu_estadistica(proyectos)

        elif opcion == "F" or opcion == "f":
            guardar_proyectos(proyectos)
            guardar_usuarios(usuarios)
            print("Datos guardados. Saliendo del programa")
            corriendo = False

        else:
            print("Opcion invalida")


menu_login()
menu_principal()
