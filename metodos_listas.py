# Creando una lista normal
lista = ["Juan", 20, "Desarrollo Personal", True]
print(lista)

# Creando una lista con list
lista2 = list(["Juan", 20, "Malina", 100])
print(lista2)

# Devuelve la cantidad de elementos de la lista
cant_elementos = len(lista)
print(cant_elementos)

# Agregar elementos a las listas (los añade a la última posición)
lista.append(7)
print(lista)

# Agregar elementos a la lista con un índice específico
lista.insert(2,"Malina")
print(lista)

# Agregar varios elementos a una lista
lista.extend(["Bautista", 2023, False, 65])
print(lista)

# Eliminando un elemento de la lista (por índice) | -1 para eliminar el último elemento 
lista.pop(0)
print(lista)

# Eliminando un elemento de la lista (especificando tal cual, lo que queremos eliminar)
lista.remove("Bautista")
print(lista)

# Ordena los elementos de forma ascendente
lista_ = [45,7,2,98,23,0,1,5,9]
lista_.sort()
print(lista_)

# Ordena los elementos de forma descendente
lista_.sort(reverse=True)
print(lista_)

# Revertir (dar vuelta) una lista
new_lista = ["Hola", True, 100, 29, False]
new_lista.reverse()
print(new_lista)


# Elimina todos los elementos de la lista
lista.clear()
print(lista)
