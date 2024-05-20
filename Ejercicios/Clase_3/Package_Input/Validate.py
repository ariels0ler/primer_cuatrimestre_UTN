
def validate_number(numero:int|float,mensaje_error:str, minimo:int|float, maximo:int|float,reintentos:int) -> int|float|None:
    
    while numero < minimo or numero > maximo:
        if reintentos > 0:
            reintentos -= 1
            numero = input(mensaje_error)
            numero = float(numero)
        elif reintentos == 0:
            return None
    return numero

    
def validate_lenght(cadena:str,mensaje_error:str, longitud:int, reintentos:int) -> str|None:
    while len(cadena) > longitud:
        if reintentos > 0:
            reintentos -= 1
            cadena = input(mensaje_error)
        elif reintentos == 0:
            return None
    return cadena