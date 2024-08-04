import re 

nombre_1 = "Juan Bautista Malina"
nombre_2 = "Simon Malina"
nombre_3 = "Kevin Romero"


# Función match: Busca si hay coincidencias en un patrón de búsqueda al comienzo de una cadena de texto
if re.match("Juan", nombre_1):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")
    

# Función search: Busca en toda la cadena para ver si el patrón de búsqueda se encuentra o no. 
cadena_1 = "0934jt9j34rgnl,aesngliñrn71wimneñfna,on{zdv{i}}"
cadena_2 = "r,x dvmd sjjjkfksñasñdkc,dkndfbsdbf99999971dsekmvose"
cadena_3 = "dfkblkxdbfbsxfxbdsvq34q34734574354722217"


if re.search("71", cadena_1):
    print("Hemos encontrado el numero")
else:
    print("No lo hemos encontrado")
    