from Package_Input.ingreso_datos import get_int
from Package_Input.Especificas import *

# a-Pedir el ingreso de 10 números enteros entre -1000 y 1000.
def ingresar_numeros(lista:list, mensaje:str, mensaje_errror:str, maximo, minimo, reintentos)->None:
    for i in range(len(lista)):
        numero = get_int(mensaje,mensaje_errror , minimo, maximo ,reintentos)
        numero = int(numero)
        lista[i] = numero
        
    return None

# b-Mostrar la cantidad de números positivos y negativos.
def contador_positivos_negativos(lista:list)->str:
    positivos = 0
    negativos = 0

    for i in range(len(lista)):
        if determinar_positividad(lista[i]) == True:
            positivos += 1
        elif determinar_positividad(lista[i]) == False:
            negativos += 1
        
        resultado = f'La cantidad de números positivos es {positivos} y la cantidad de números negativos es {negativos}'
        
    return resultado

# c-Mostrar la sumatoria de los números pares.
def sumar_pares(lista:list)->int:
    pares = 0
    for i in range(len(lista)):
        if definir_paridad(lista[i]) == True:
            pares += lista[i]
            resultado = f'La suma de los número pares es {pares}'
    return resultado

# d-Informar el mayor de los números impares.
def mayor_impar(lista:list)->int:
    mayor_lista = lista[0]

    for i in range(len(lista)):
        if definir_paridad(lista[i]) == False:
            if lista[i] > mayor_lista:
                mayor_lista = lista[i]

    return mayor_lista

# e-Imprimir todos los números ingresados.
def mostrar_lista(lista:list):

    for i in range(len(lista)):
        print(lista[i])

# f-Imprimir todos los números pares.
def mostrar_pares(lista:list):
    for i in range(len(lista)):
        if definir_paridad(lista[i]) == True:
            print(lista[i])

# g-Imprimir los números de los índices impares.
def imprimir_indice_impares(lista:list):
    for i in range(len(lista)):
        if definir_paridad(lista[i]) == False:
            print(i)