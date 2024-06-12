#Ejemplo de carga de números en listas
#Carga secuencial
lista = [0] * 5

for i in range(len(lista)):
    numero = input(f"Ingrese un número en el índice {i+1}: ")
    lista[i] = numero
    lista[i] = int(lista[i])

for i in range (len(lista)):
    print(lista[i])

#Carga aleatoria
"""mi_lista = [0] * 5

respuesta = 'Si'
largo_lista = len(mi_lista)

while respuesta == 'Si':
    
    posicion = input('Ingrese la posición de la lista en la que quiera agregar un número: ')
    posicion = int(posicion)
    while posicion < 1 or posicion > largo_lista:
        posicion = input('Posición inválida. Reingrese la posición de la lista en la que quiera agregar un número: ')
        posicion = int(posicion)
    
    numero = input('Ingrese el número: ')
    numero = int(numero)
    mi_lista[posicion-1] = numero


    respuesta = input('Desea continuar? Si/No: ')
    while respuesta != 'Si' and respuesta != 'No':
        respuesta = input('Desea continuar? Si/No: ')
    

for i in range(len(mi_lista)):
    print(mi_lista[i])"""
    


#Función : Calcular_Promedio_enteros 
# Tiene que reciir una lista de enteros / calcular / devolver el promedio

def calcular_promedio(list:list):
    suma = 0
    cantidad_promedio = 0 

    for i in range(len(lista)):
        suma += lista[i]
        if lista[i] > 0:
            cantidad_promedio += 1
    realizar_promedio = suma / cantidad_promedio
    
    return realizar_promedio

# print("---------------------------------------------")
# print(calcular_promedio(lista))

#Función: Calcular_producto
#Calcular & retornar producto(resultado de la multiplicación)

def calcular_producto(lista:list):
    multiplicacion = 1
    producto = 0
    for i in range(len(lista)):
        if lista[i] != 0:
            multiplicacion *= lista[i]
            producto = multiplicacion
    
    return producto

# print("---------------------------------------------")
# print(calcular_producto(lista))

#Función: encontrar_valor_maximo
#recibe lista enteros / retorna posicion y/o posiciones del valor máximo

def encontrar_valor_maximo(lista:list):
    posicion_mayor = -1
    for i in range(len(lista)):
        if lista[i] > posicion_mayor:
            posicion_mayor = i 

    return posicion_mayor
print("---------------------------------------------")
resultado = encontrar_valor_maximo(lista)
print(f"El índice con donde se encuentra el número mayor es: {resultado}")

#Función: reemplazar_nombres
#recibe una lista de nombres / nombre a reemplazar / reemplazo correspondiente
#Retornar la cantidad total de reemplazos realizados

lista_txt = ["Hola","Juan","Hellow", "Juan"]

def reemplazar_nombres(lista:list, nombre:str, reemplazo:str):
    contador_reemplazo = 0
    for i in range(len(lista)):
        if lista[i] == nombre:
            lista[i] = reemplazo
            contador_reemplazo += 1
        
    return contador_reemplazo


"""print(lista_txt)
reemplazo = reemplazar_nombres(lista_txt,"Juan","Pepe")
print("---------------------------------------------")
print(lista_txt)
print(reemplazo)"""