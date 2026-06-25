
from Modulos._init_ import *

tablas = []
usuarios = [["admin", "1234"]]


def menu_mostrar_tablas(tablas: list) -> None:
    '''
    menu pequenio para mostrar tabla completa, columna o fila. hecho
    para facilitar la opcion C de mostrar tabla, columna o fila
    recibe la lista de tablas
    no retorna nada
    '''
    tabla = elegir_tabla(tablas)

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








def mostrar_menu_principal(tablas: list) -> None:
    '''
    bucle principal del menu
    recibe la lista de tablas
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
            pass

        elif opcion == "B" or opcion == "b":
            crear_tabla(tablas)

        elif opcion == "C" or opcion == "c":
            if len(tablas) == 0:
                print("No hay tablas cargadas")
            else:
                tabla = elegir_tabla(tablas)
                modificar_tablas(tabla)

        elif opcion == "D" or opcion == "d":
            if len(tablas) == 0:
                print("No hay tablas cargadas")
            else:
                menu_mostrar_tablas(tablas)

        elif opcion == "E" or opcion == "e":
            if len(tablas) == 0:
                print("No hay tablas cargadas")
            else:
                mostrar_menu_estadistica(tablas)

        elif opcion == "F" or opcion == "f":
            print("Saliendo del programa")
            corriendo = False

        else:
            print("Opcion invalida")


def login(tablas: list) -> None:
    '''
    maneja el inicio de sesion y registro de usuarios
    recibe la lista de tablas
    no retorna nada
    '''
    print("1. Iniciar sesion")
    print("2. Registrarse")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        usuario = input("Usuario: ")
        contrasena = input("Contrasena: ")
        encontrado = False

        for i in range(len(usuarios)):
            if usuarios[i][0] == usuario and usuarios[i][1] == contrasena:
                encontrado = True

        if encontrado:
            print(f"Bienvenido {usuario}")
            mostrar_menu_principal(tablas)
        else:
            print("Usuario o contrasena incorrectos")
            login(tablas)

    elif opcion == "2":
        usuario = input("Ingrese un nombre de usuario: ")
        contrasena = input("Establezca una contrasena: ")


        usuarios.append([usuario, contrasena])
        print(f"Usuario {usuario} registrado exitosamente")
        mostrar_menu_principal(tablas)
        
    else:
        print("Opcion invalida")
        login(tablas)


