from Package_Input.ingreso_datos import get_int

lista_numeros = [-1] * 4


# a-Pedir el ingreso de 10 números enteros entre -1000 y 1000.
def ingresar_numeros(lista:list, mensaje:str, mensaje_errror:str, maximo, minimo, reintentos)->None:
    for i in range(len(lista)):
        numero = get_int(mensaje,mensaje_errror , minimo, maximo ,reintentos)
        numero = int(numero)
        lista[i] = numero
        
    return None

# b-Mostrar la cantidad de números positivos y negativos.
def determinar_positividad(numero:int)->bool:
    valor = None
    if numero > 0:
        valor = True
    elif numero < 0:
        valor = False
    return valor

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
def definir_paridad(numero:int)->bool:
    valor = None
    if numero % 2 == 0:
        valor = True
    elif numero % 2 != 0:
        valor = False
    return valor

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

while True:
    print("""
        
        Elija una de las siguientes opciones:
        a-Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
        b-Mostrar la cantidad de números positivos y negativos.
        c-Mostrar la sumatoria de los números pares.
        d-Informar el mayor de los números impares.
        e-Imprimir todos los números ingresados.
        f-Imprimir todos los números pares.
        g-Imprimir los números de los índices impares.  
        h-Salir

""")
    opcion = input("")
    
    match opcion:
        case "a":
            ingresar_numeros(lista_numeros, 'Ingrese un número entre -1000 y 1000: ', 'Error, numero fuera de rango. Reingrese el número: ', 1000, -1000, 5)
            pass
        case "b":
            resultado = contador_positivos_negativos(lista_numeros)
            print(f'{resultado}\n')
            pass
        case "c": 
            resultado = sumar_pares(lista_numeros)
            print(resultado)
            pass
        case "d":
            resultado = mayor_impar(lista_numeros)
            print(resultado)
            pass
        case "e":
            resultado = mostrar_lista(lista_numeros)
            pass
        case "f":
            resultado = mostrar_pares(lista_numeros)

            pass
        case "g":
            resultado = imprimir_indice_impares(lista_numeros)

            pass
        case "h":
            break
        case _:
            opcion = input("Ingrese una opción válida")








    # for i in range(len(lista)):
    #     numero_ingresado = input('Ingrese un número entre -1000 y 1000')
    #     numero_ingresado = int(numero_ingresado)
    #     if numero_ingresado < -1000 or numero_ingresado > 1000:
    #         numero_ingresado = input('Error, ingrese un número en el rango indicado (entre -1000 y 1000)')
        # lista[i] = numero_ingresado