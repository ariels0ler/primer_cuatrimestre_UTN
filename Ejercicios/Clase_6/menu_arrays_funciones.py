from Package_Input.Generales import *

lista_numeros = [-1] * 4

ingreso_a = False

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
            ingreso_a = True
            ingresar_numeros(lista_numeros, 'Ingrese un número entre -1000 y 1000: ', 'Error, numero fuera de rango. Reingrese el número: ', 1000, -1000, 5)
            pass

        case "b":
            if ingreso_a == True:
                resultado = contador_positivos_negativos(lista_numeros)
                print(f'{resultado}\n')
            else:
                print('Primero debe ingresar a la opción "a"')

        case "c": 
            if ingreso_a == True:
                resultado = sumar_pares(lista_numeros)
                print(resultado)
            else:
                print('Primero debe ingresar a la opción "a"')

        case "d":
            if ingreso_a == True: 
                resultado = mayor_impar(lista_numeros)
                print(resultado)
            else:
                print('Primero debe ingresar a la opción "a"')

        case "e":
            if ingreso_a == True:
                resultado = mostrar_lista(lista_numeros)
            else:
                print('Primero debe ingresar a la opción "a"')
        case "f":
            if ingreso_a == True:
                resultado = mostrar_pares(lista_numeros)
            else:
                print('Primero debe ingresar a la opción "a"')

        case "g":
            if ingreso_a == True:
                resultado = imprimir_indice_impares(lista_numeros)
            else:
                print('Primero debe ingresar a la opción "a"')
        
        case "h":
            break
        
        case _:
            opcion = input("Ingrese una opción válida: ")








