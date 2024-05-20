from Package_Input import Validate as V

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    entero = input(mensaje)
    entero = int(entero)
    numero = V.validate_number(entero,mensaje_error, minimo, maximo, reintentos)
    if numero == None:
        return None
    numero = int(numero)
    return numero


#-----------------------------------------------------------------------------------------------

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> int|None:
    flotante = input(mensaje)
    flotante = float(flotante)
    numero = V.validate_number(flotante,mensaje_error,minimo,maximo,reintentos)

    return numero


#-----------------------------------------------------------------------------------------------

def get_string(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str|None:
    cadena = input(mensaje)
    texto = V.validate_lenght(cadena,mensaje_error,longitud,reintentos)
    return texto


#-----------------------------------------------------------------------------------------------