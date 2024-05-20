#CONSIGNA

"""Ejercicio Integrador 01

La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.

Se debe informar lo siguiente:

Del más caro de los barbijos, la cantidad de unidades y el fabricante.
Del ingreso con más unidades, el fabricante. 
Cuántas unidades de jabones hay en total.
"""
#Inicializaciones

acumulador_barbijos = 0
ingreso_mas_cantidad = 0
acumulador_jabones = 0


for i in range(5):


    #Validaciones
    tipo = input('Ingrese el tipo de producto: ')
    while tipo != 'barbijo' and tipo != 'jabón' and tipo != 'alcohol':
        tipo = input('Reingrese el tipo de producto: ')
    
    precio = input('Ingrese el precio: ')
    precio = int(precio)
    while precio < 100 or precio > 300:
        precio = input('Reingrese el preico: ')
        precio = int(precio)
    
    cantidad = input('Ingrese la cantidad: ')
    cantidad = int(cantidad)
    while cantidad < 1 or cantidad > 1000:
        cantidad = input('Reingrese la cantidad: ')

    fabricante = input('Ingrese un fabricante (puede ser cualquiera): ')

    match tipo:
        case "barbijo":
            
            if i == 0 or precio > precio_fabricante_mas_caro:
                fabricante_mas_caro = fabricante
                precio_fabricante_mas_caro = precio
                acumulador_barbijos = acumulador_barbijos + cantidad
        
        case "jabón":
            acumulador_jabones = acumulador_jabones + cantidad

    if i == 0 or cantidad > ingreso_mas_cantidad:
        ingreso_mas_cantidad = cantidad
        fabricante_mas_unidades = fabricante

    # Del más caro de los barbijos, la cantidad de unidades y el fabricante.
print(f'El fabricante de los barbijos más caros es {fabricante_mas_caro} y hay un total de {acumulador_barbijos} unidades')
print(f'El fabricante del ingreso con más unidades es {fabricante_mas_unidades}')
print(f'Hay un total de {acumulador_jabones} unidades de jabón')
    

