from modulos.reutilizables import validar_indice, validar_valor_numerico
from modulos.tablas import elegir_tabla


def calcular_maximo(tabla: list, columna: int) -> tuple:
    '''
    calcula el valor maximo de una columna numerica y cuantas veces aparece
    recibe la matriz y el indice de la columna
    retorna una tupla con el maximo y su conteo
    '''
    maximo = float(tabla[1][columna])

    for i in range(1, len(tabla)):
        valor = float(tabla[i][columna])

        if valor > maximo:
            maximo = valor

    conteo = 0
    for i in range(1, len(tabla)):
        if float(tabla[i][columna]) == maximo:
            conteo += 1

    return maximo, conteo


def calcular_minimo(tabla: list, columna: int) -> tuple:
    '''
    calcula el valor minimo de una columna numerica y cuantas veces aparece
    recibe la matriz y el indice de la columna
    retorna una tupla con el minimo y su conteo
    '''
    minimo = float(tabla[1][columna])

    for i in range(1, len(tabla)):
        valor = float(tabla[i][columna])

        if valor < minimo:
            minimo = valor

    conteo = 0
    for i in range(1, len(tabla)):
        if float(tabla[i][columna]) == minimo:
            conteo += 1

    return minimo, conteo


def calcular_promedio_aritmetico(tabla: list, columna: int) -> float:
    '''
    calcula el promedio aritmetico de una columna numerica
    recibe la matriz y el indice de la columna
    retorna el promedio aritmetico como float
    '''
    acumulador = 0

    for i in range(1, len(tabla)):
        acumulador += float(tabla[i][columna])

    return acumulador / (len(tabla) - 1)


def calcular_promedio_geometrico(tabla: list, columna: int) -> float:
    '''
    calcula el promedio geometrico de una columna numerica
    recibe la matriz y el indice de la columna
    retorna el promedio geometrico como float
    '''
    producto = 1

    for i in range(1, len(tabla)):
        producto *= float(tabla[i][columna])

    return producto ** (1 / (len(tabla) - 1))


def calcular_frecuencia(tabla: list, columna: int) -> dict:
    '''
    calcula la frecuencia de cada valor de una columna
    recibe la matriz y el indice de la columna
    retorna un diccionario con los valores y sus frecuencias
    '''
    valores = []
    conteos = []

    for i in range(1, len(tabla)):
        valor = tabla[i][columna]
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


def calcular_dispersion(tabla: list, columna: int) -> tuple:
    '''
    calcula la varianza y el desvio estandar de una columna numerica
    recibe la matriz y el indice de la columna
    retorna una tupla con la varianza y el desvio estandar
    '''
    promedio = calcular_promedio_aritmetico(tabla, columna)
    suma_diferencias = 0

    for i in range(1, len(tabla)):
        diferencia = float(tabla[i][columna]) - promedio
        suma_diferencias += (diferencia ** 2)

    varianza = suma_diferencias / (len(tabla) - 1)
    desvio = varianza ** 0.5

    return varianza, desvio

def calcular_coeficiente_variacion(tabla: list, columna: int) -> float:
    '''
    calcula el coeficiente de variacion de una columna numerica
    recibe la matriz y el indice de la columna
    retorna el coeficiente de variacion como float
    '''
    promedio = calcular_promedio_aritmetico(tabla, columna)
    varianza, desvio = calcular_dispersion(tabla, columna)

    return (desvio / promedio) * 100

def calcular_posicion(tabla: list, columna: int) -> dict:
    '''
    calcula la mediana y los cuartiles de una columna numerica
    recibe la matriz y el indice de la columna
    retorna un diccionario con mediana, q1 y q3
    '''
    valores = []

    for i in range(1, len(tabla)):
        valores.append(float(tabla[i][columna]))

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

    return {"mediana": mediana, "q1": q1, "q3": q3}

def calcular_deciles(tabla: list, columna: int) -> dict:
    '''
    calcula los deciles de una columna numerica
    recibe la matriz y el indice de la columna
    retorna un diccionario con los 9 deciles
    '''
    valores = []

    for i in range(1, len(tabla)):
        valores.append(float(tabla[i][columna]))

    for i in range(len(valores)):
        for j in range(len(valores) - 1):
            if valores[j] > valores[j + 1]:
                aux = valores[j]
                valores[j] = valores[j + 1]
                valores[j + 1] = aux

    n = len(valores)
    deciles = {}

    for i in range(1, 10):
        deciles[i] = valores[(i * n) // 10]

    return deciles


def mostrar_menu_estadistica(proyectos: list) -> None:
    '''
    submenu para calcular estadisticas de una columna
    recibe la lista de proyectos
    no retorna nada
    '''
    tabla = elegir_tabla(proyectos)
    puede_continuar = tabla != False

    if puede_continuar == True:
        print()
        for i in range(len(tabla[0])):
            print(f"  {i+1}. {tabla[0][i]}")

        columna = validar_indice("Que columna desea analizar?: ", len(tabla[0]))

        es_numerica = True
        for i in range(1, len(tabla)):
            if validar_valor_numerico(tabla[i][columna]) == False:
                es_numerica = False

        if es_numerica == False:
            print("La columna seleccionada no es numerica")
            puede_continuar = False

    if puede_continuar == True:
        print()
        print("1. Maximo y minimo")
        print("2. Promedio aritmetico")
        print("3. Promedio geometrico")
        print("4. Frecuencias")
        print("5. Dispersion (varianza y desvio estandar)")
        print("6. Posicion (mediana y cuartiles)")
        print("7. Coeficiente de variacion")
        print("8. Deciles")

        opcion = input("Que desea calcular?: ")

        if opcion == "1":
            maximo, conteo_max = calcular_maximo(tabla, columna)
            minimo, conteo_min = calcular_minimo(tabla, columna)
            print(f"  Maximo: {maximo} (aparece {conteo_max} vez/veces)")
            print(f"  Minimo: {minimo} (aparece {conteo_min} vez/veces)")

        elif opcion == "2":
            resultado = calcular_promedio_aritmetico(tabla, columna)
            print(f"  Promedio aritmetico: {resultado:.4f}")

        elif opcion == "3":
            resultado = calcular_promedio_geometrico(tabla, columna)
            print(f"  Promedio geometrico: {resultado:.4f}")

        elif opcion == "4":
            frecuencia = calcular_frecuencia(tabla, columna)
            for valor in frecuencia:
                print(f"  {valor}: {frecuencia[valor]} veces")

        elif opcion == "5":
            varianza, desvio = calcular_dispersion(tabla, columna)
            print(f"  Varianza: {varianza:.4f}")
            print(f"  Desvio estandar: {desvio:.4f}")

        elif opcion == "6":
            posicion = calcular_posicion(tabla, columna)
            print(f"  Mediana: {posicion['mediana']}")
            print(f"  Q1: {posicion['q1']}")
            print(f"  Q3: {posicion['q3']}")

        elif opcion == "7":
            resultado = calcular_coeficiente_variacion(tabla, columna)
            print(f"  Coeficiente de variacion: {resultado:.4f}%")

        elif opcion == "8":
            deciles = calcular_deciles(tabla, columna)
            for i in range(1, 10):
                print(f"  D{i}: {deciles[i]}")

        else:
            print("Opcion invalida")
            mostrar_menu_estadistica(proyectos)
