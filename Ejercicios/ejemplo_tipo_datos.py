# Tuple : Las tuplas son un tipo de lista inmutable.
    #Sintaxis () "Parentesis"

lista = [1,2,3]


#Set : Sus elemnentos son únicos y no tienen elementos duplicados // 
    #No respetan un orden, no están indexados
    #Sintaxis {} "Llaves"
    #No se pueden acceder a sus elementos a traves de sus índices

    #Métodos exclusivos tipo set:
    # add : Agrega un elemento, si el elemento ya estaba no lo agrega.
    # discard : Elimina un elemento si ya está en el set // remove da error el elemento no existe

# Diccionario : Colección de elementos --- Contiene una "Key" única con un "value"
# Se declara con {} "Llaves"
    #Métodos diccionarios:
    # get : Accede a la key si es que existe en el diccionario
    # keys : Lista de keys
    # Values : Lista de values
    # pop : Elimina una key y el value asociado a ella.

diccionario = {'Juan': 21, 
            'Pepe': 39}


print (diccionario.get('Juan'))
