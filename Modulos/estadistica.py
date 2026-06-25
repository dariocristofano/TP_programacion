
from reutilizables import elegir_tabla, validar_entero, validar_indice



def calcular_maximo(tabla: dict, columna: int) -> float:
    '''
    calcula el valor maximo de una columna
    recibe un diccionario de tabla y el indice de la columna
    retorna el valor maximo como float
    '''
    maximo = float(tabla["filas"][0][columna])
    for i in range(len(tabla["filas"])):
        valor = float(tabla["filas"][i][columna])
        if valor > maximo:
            maximo = valor
    return maximo


def calcular_minimo(tabla: dict, columna: int) -> float:
    '''
    calcula el valor minimo de una columna
    recibe un diccionario de tabla y el indice de la columna
    retorna el valor minimo como float
    '''
    minimo = float(tabla["filas"][0][columna])
    for i in range(len(tabla["filas"])):
        valor = float(tabla["filas"][i][columna])
        if valor < minimo:
            minimo = valor
    return minimo


def calcular_promedio_aritmetico(tabla: dict, columna: int) -> float:
    '''
    calcula el promedio aritmetico de una columna
    recibe un diccionario de tabla y el indice de la columna
    retorna el promedio aritmetico como float
    '''
    acumulador = 0
    for i in range(len(tabla["filas"])):
        acumulador += float(tabla["filas"][i][columna])
    return acumulador / len(tabla["filas"])


def calcular_promedio_geometrico(tabla: dict, columna: int) -> float:
    '''
    calcula el promedio geometrico de una columna
    recibe un diccionario de tabla y el indice de la columna
    retorna el promedio geometrico como float
    '''
    producto = 1
    for i in range(len(tabla["filas"])):
        producto *= float(tabla["filas"][i][columna])
    return producto ** (1 / len(tabla["filas"]))


def calcular_frecuencia(tabla: dict, columna: int) -> dict:
    '''
    calcula la frecuencia de cada valor de una columna
    recibe un diccionario de tabla y el indice de la columna
    retorna un diccionario con los valores y sus frecuencias
    '''
    valores = []
    conteos = []

    for i in range(len(tabla["filas"])):
        valor = tabla["filas"][i][columna]
        encontrado = False
        for j in range(len(valores)):
            if valores[j] == valor:
                conteos[j] += 1
                encontrado = True
        if encontrado == False:
            valores.append(valor)
            conteos.append(1)

    frecuencia = {}
    for i in range(len(valores)):
        frecuencia[valores[i]] = conteos[i]

    return frecuencia


def calcular_dispersion(tabla: dict, columna: int) -> tuple:
    '''
    calcula la varianza y el desvio estandar de una columna
    recibe un diccionario de tabla y el indice de la columna
    retorna una tupla con la varianza y el desvio estandar
    '''
    promedio = calcular_promedio_aritmetico(tabla, columna)
    suma_diferencias = 0
    for i in range(len(tabla["filas"])):
        diferencia = float(tabla["filas"][i][columna]) - promedio
        suma_diferencias += (diferencia ** 2)
    varianza = suma_diferencias / len(tabla["filas"])
    desvio = varianza ** 0.5
    return varianza, desvio


def calcular_posicion(tabla: dict, columna: int) -> dict:
    '''
    calcula la mediana y los cuartiles de una columna
    recibe un diccionario de tabla y el indice de la columna
    retorna un diccionario con la mediana q1 y q3
    '''
    valores = []
    for i in range(len(tabla["filas"])):
        valores.append(float(tabla["filas"][i][columna]))

    for i in range(len(valores)):
        for j in range(len(valores) - 1):
            if valores[j] > valores[j + 1]:
                aux = valores[j]
                valores[j] = valores[j + 1]
                valores[j + 1] = aux

    n = len(valores)
    if n % 2 == 0:
        mediana = (valores[n // 2 - 1] + valores[n // 2]) / 2
    else:
        mediana = valores[n // 2]

    q1 = valores[n // 4]
    q3 = valores[(3 * n) // 4]

    return {
        "mediana": mediana,
        "q1": q1,
        "q3": q3
    }


def mostrar_menu_estadistica(tablas: list) -> None:
    '''
    submenu para calcular estadisticas de una columna
    recibe la lista de tablas
    no retorna nada
    '''
    tabla = elegir_tabla(tablas)

    for i in range(len(tabla["columnas"])):
        print(f"{i+1}. {tabla['columnas'][i]}")

    columna = validar_indice(
        "Que columna desea analizar?: ",
        len(tabla["columnas"])
    )

    es_numerica = True

    for i in range(len(tabla["filas"])):
        valor = tabla["filas"][i][columna]
        es_numero = True

        for j in range(len(valor)):
            if ord(valor[j]) < 48 or ord(valor[j]) > 57:
                es_numero = False

        if es_numero == False:
            es_numerica = False

    if es_numerica == False:
        print("La columna no es numerica")
        return

    print()
    print("1. Maximo y minimo")
    print("2. Promedio aritmetico")
    print("3. Promedio geometrico")
    print("4. Frecuencias")
    print("5. Dispersion")
    print("6. Posicion")
    opcion = input("Que desea calcular?: ")

    if opcion == "1":
        print(f"Maximo: {calcular_maximo(tabla, columna)}")
        print(f"Minimo: {calcular_minimo(tabla, columna)}")

    elif opcion == "2":
        print(f"Promedio aritmetico: {calcular_promedio_aritmetico(tabla, columna)}")

    elif opcion == "3":
        print(f"Promedio geometrico: {calcular_promedio_geometrico(tabla, columna)}")
    
    elif opcion == "4":
        frecuencia = calcular_frecuencia(tabla, columna)
        for valor in frecuencia:
            print(f"{valor}: {frecuencia[valor]} veces")

    elif opcion == "5":
        varianza, desvio = calcular_dispersion(tabla, columna)
        print(f"Varianza: {varianza}")
        print(f"Desvio estandar: {desvio}")

    elif opcion == "6":
        posicion = calcular_posicion(tabla, columna)
        print(f"Mediana: {posicion['mediana']}")
        print(f"Q1: {posicion['q1']}")
        print(f"Q3: {posicion['q3']}")

    else:
        print("Opcion invalida")
        mostrar_menu_estadistica(tablas)