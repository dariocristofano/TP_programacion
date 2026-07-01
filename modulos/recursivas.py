
def calcular_es_multiplo(numero: int, base: int) -> bool:
    """
    verifica si numero es multiplo de base de forma recursiva
    numero: entero que se evalua, base: divisor para verificar
    retorna true si numero es multiplo de base o false si no lo es
    """
    if base == 0:
        resultado = False
    elif base < 0:
        resultado = calcular_es_multiplo(numero, -base)
    elif numero < 0:
        resultado = calcular_es_multiplo(numero + base, base)
    elif numero == 0:
        resultado = True
    elif numero < base:
        resultado = False
    else:
        resultado = calcular_es_multiplo(numero - base, base)


    return resultado

#4, 2


def calcular_es_par(numero: int) -> bool:
    """
    verifica si un numero entero es par de forma recursiva
    numero: entero que se evalua
    retorna true si es par o false si es impar
    """
    if numero < 0:
        return calcular_es_par(numero + 2)
    elif numero == 0:
        resultado = True
    elif numero == 1:
        resultado = False
    else:
        resultado = calcular_es_par(numero - 2)


    return resultado


def calcular_es_primo(numero: int, divisor: int = 2) -> bool:
    """
    verifica si un numero entero es primo de forma recursiva
    numero: entero que se evalua, divisor: para verificar
    retorna true si es primo, false si no lo es
    """
    if numero <= 1:
        resultado = False
    elif numero == 2:
        resultado = True
    elif numero % divisor == 0:
        resultado = False
    elif divisor >= numero - 1:
        resultado = True
    else:
        resultado = calcular_es_primo(numero, divisor + 1)


    return resultado

#10, 11




def esta_en_rango(numero: int, minimo: int, maximo: int) -> bool:
    """
    verifica si un numero se encuentra dentro de un rango dado de forma recursiva
    numero: entero a que se evalua, minimo: limite minimo, maximo: limite maximo
    retorna true si numero esta entre minimo y maximo inclusive o false si no
    """
    if minimo > maximo:
        resultado = False
    elif numero == minimo:
        resultado = True
    else:
        resultado = esta_en_rango(numero, minimo + 1, maximo)


    return resultado

#8, 2, 10
#12, 2, 10