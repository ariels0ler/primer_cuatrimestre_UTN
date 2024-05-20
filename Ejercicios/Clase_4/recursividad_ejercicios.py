from  Package_Input.Input import *

'''def calcular_factorial(numero):
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
    return resultado

print(calcular_factorial(5))'''


#--------------------------------------------------------------------

def sumar_naturales(numero:int) -> int:
    while numero == None:
        numero = get_int('Ingrese un número: ',"Error, reingrese el núemero: ", 1, 10, 2)

    if numero == 1:
        resultado = 1
    else:
        resultado = numero + sumar_naturales(numero - 1)
    return resultado

'''print(sumar_naturales(get_int('Ingrese un número: ',"Error, reingrese el núemero: ", 1, 10, 2)))'''
#--------------------------------------------------------------------

def calcular_potencia(base:int, exponente:int) -> int:
    while base == None:
        base = get_int('Ingrese la base de la potencia: ', 'Error, reingrese la base: ', 0, 1000, 5)
    while exponente == None:
        exponente = get_int('Ingrese el exponente de la potencia: ', 'Error, reingrese el exponente: ', 0, 1000, 5)
        
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)
    return resultado

'''print(calcular_potencia(get_int('Ingrese la base de la potencia: ','Error, reingrese la base: ',0,1000,5),get_int('Ingrese el exponente de la potencia: ', 'Error, reingrese el exponente: ', 0, 1000, 5)))'''

#--------------------------------------------------------------------

def sumar_digitos(numero:int)->int:
    if numero == 0:
        resultado = 0
    else:
        resultado = numero % 10 + sumar_digitos(numero // 10)
    return resultado

print(sumar_digitos(get_int('Ingrese un número: ', 'Error, reingrese el número: ', 11,10000 , 2)))