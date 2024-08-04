diccionario = {
    "nombre" : "Juan Bautista",
    "apellido" : 'Malina',
    "edad" : 20
}

# Devuelve las claves
claves = diccionario.keys()
print(claves)

# Devuelve el valor
claves = diccionario.get("nombre")
print(claves)

# Elimina un elemento del diccionario 
diccionario.pop("nombre")
print(diccionario)

# Accediendo a un elemento iterable del diccionario
dic_item = diccionario.items()
print(dic_item)


# Elimina los elementos de la lista
diccionario.clear()

