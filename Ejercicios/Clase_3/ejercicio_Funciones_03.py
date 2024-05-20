
def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    entero = input(mensaje)
    entero = int(entero)
    while entero < minimo or entero > maximo:
        if reintentos > 0:
            reintentos -= 1
            entero = input(mensaje_error)
            entero = int(entero)
        else:
            return None

    return entero

#-----------------------------------------------------------------------------------------------

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> int|None:
    flotante = input(mensaje)
    flotante = float(flotante)
    while flotante < minimo or flotante > maximo:
        if reintentos > 0:
            reintentos -= 1 
            flotante = input(mensaje_error)
            flotante = float(flotante)
        else:
            return None
    
    return flotante

#-----------------------------------------------------------------------------------------------

def get_string(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str|None:
    cadena = input(mensaje)
    while len(cadena) > longitud:
        if reintentos > 0:
            reintentos -= 1
            cadena = input(mensaje_error)
        else:
            return None
    return cadena
prueba = get_string('Ingrese una cadena: ', 'Error, cadena muy larga. Reingrese la cadena: ', 4, 2)
print(f'La cadena ingresada es {prueba}')
#-----------------------------------------------------------------------------------------------