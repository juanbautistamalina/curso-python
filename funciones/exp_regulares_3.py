import re

lista_nombres = ["Juan", 
                 "Simón", 
                 "Kevin",
                 "Ulises",
                 "Mateo",
                 "Abraham"]

for i in lista_nombres:
    if re.findall('[a-b]', i):
        print(i)