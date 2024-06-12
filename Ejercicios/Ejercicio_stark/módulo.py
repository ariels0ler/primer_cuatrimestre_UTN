from data_stark import *

def stark_normalizar_datos(lista: list[dict])->int | float:
    '''

    '''
    for i in range(len(lista)):
        while lista[i]["altura"] != float and lista[i]["peso"] != float and lista[i]["fuerza"] != int:
            altura_float = float(lista[i].get("altura"))
            peso_float   = float(lista[i].get("peso"))
            fuerza_int   = int(lista[i].get("fuerza"))
            lista[i]["altura"] = altura_float
            lista[i]["peso"] = peso_float
            lista[i]["fuerza"] = fuerza_int

stark_normalizar_datos(lista_personajes)