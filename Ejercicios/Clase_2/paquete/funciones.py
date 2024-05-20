import math
from random import randint

#Consignas
"""
1- Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
2- Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
3- Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
4- Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables (que reciban el mensaje de pedido de datos por parámetro).
5- Agregar validaciones.
6- Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
7- Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
8- Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
9 - Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado."""



def solicitar_entero(mensaje:str, mensaje_error:str, rango_1:int, rango_2:int) -> int:
    entero = input(mensaje)
    entero = int(entero)
    while entero < rango_1 or entero > rango_2:
        entero = input(mensaje_error)
        entero = int(entero)    

    return entero

#-----------------------------------------------------------------------------------------------

def solicitar_flotante(mensaje:str, mensaje_error:str, rango_1:float, rango_2:float) -> float:
    flotante = input(mensaje)
    flotante = float(flotante)
    while flotante < rango_1 or flotante > rango_2:
        flotante = input(mensaje_error)
        flotante = float(flotante)

    return flotante

#-----------------------------------------------------------------------------------------------

def solicitar_cadena(mensaje:str) -> str:
    cadena = input(mensaje)
    
    return cadena

#-----------------------------------------------------------------------------------------------

def calcular_area(radio:int):
    area = math.pi * (radio ** 2)

    return area

#-----------------------------------------------------------------------------------------------

def par_o_impar(mensaje:str) -> str:
    numero = input(mensaje)
    numero = float(numero)
    if numero % 2 == 0:
        resultado = "El número es par"
    else:
        resultado = "El número es impar"

    print(resultado)

#-----------------------------------------------------------------------------------------------

def encontrar_maximo(numero_1:int, numero_2:int, numero_3:int) -> int:
    if numero_1 > numero_2 and numero_1 > numero_3:
        return numero_1
    elif numero_2 > numero_3:
        return numero_2
    else:
        return numero_3

#-----------------------------------------------------------------------------------------------

def calcular_potencia(base:int, exponente:int) -> int:
    potencia = base ** exponente

    return potencia

#-----------------------------------------------------------------------------------------------

def generar_numero_aleatorio(limite_a:int, limite_b:int) -> int:
    return randint(limite_a, limite_b)
    


#-----------------------------------------------------------------------------------------------

#Validación del tipo de dato (No se requiere para estos puntos)
#1
'''def solicitar_entero()->int:
        #En este ejemplo solicitamos los datos dentro de la función
        numero = input(mensaje)
        numero = float(numero)
        while numero % 2 != 1 and numero % 2 != 0:
            numero = input(mensaje)
            numero = float(numero)
        return(numero)

    mensaje = 'Ingrese un número entero: '
    numero_entero = solicitar_entero()
    print(f"El numero entero es {numero_entero}")

    #2
        def solicitar_flotante()->float:
        numero = input(mensaje)
        numero = float(numero)
        while numero % 2 == 1 or numero % 2 == 0:
            numero = input(mensaje)
            numero = float(numero)
        return(numero)


    mensaje = 'Ingrese un número flotante: '
    numero_flotante = solicitar_flotante()
    print(f"El numero flotante es {numero_flotante}")'''
