def guardar_usuarios(usuarios: list) -> None:
    '''
    guarda la lista de usuarios en un archivo csv
    recibe la lista de usuarios
    no retorna nada
    '''
    archivo = open("archivos/usuarios.csv", "w")

    for i in range(len(usuarios)):
        archivo.write(usuarios[i][0] + "," + usuarios[i][1] + "\n")

    archivo.close()


def guardar_proyectos(proyectos: list) -> None:
    '''
    guarda la lista de proyectos en un archivo csv
    recibe la lista de proyectos (lista de diccionarios)
    no retorna nada
    '''
    archivo = open("archivos/proyectos.csv", "w")

    for i in range(len(proyectos)):
        archivo.write("PROYECTO," + proyectos[i]["nombre"] + "\n")
        
        tablas = proyectos[i]["tablas"]

        for j in range(len(tablas)):
            archivo.write("TABLA," + tablas[j]["nombre"] + "\n")

            matriz = tablas[j]["matriz"]

            for k in range(len(matriz)):
                fila = ""

                for l in range(len(matriz[k])):

                    fila += matriz[k][l]

                    if l < len(matriz[k]) - 1:
                        fila += ","

                archivo.write(fila + "\n")

    archivo.close()
