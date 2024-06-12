# b-Mostrar la cantidad de números positivos y negativos.
def determinar_positividad(numero:int)->bool:
    valor = None
    if numero > 0:
        valor = True
    elif numero < 0:
        valor = False
    return valor

# c-Mostrar la sumatoria de los números pares.
def definir_paridad(numero:int)->bool:
    valor = None
    if numero % 2 == 0:
        valor = True
    elif numero % 2 != 0:
        valor = False
    return valor
