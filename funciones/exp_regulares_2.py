import re 

lista_nombres = ["Juan Bautista Malina", "Simón Malina", "Kevin Romero", "Ulises Pellegrini"]


# Buscando en la lista todas las coincidencias que empiecen con "Juan"
for nombre in lista_nombres:
    if re.findall('^Juan', nombre):
        print(nombre)      


# Buscando en la lista todas las coincidencias que terminen con "Malina"
for nombre in lista_nombres:
    if re.findall('Malina$', nombre):
        print(nombre)      
