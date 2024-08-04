cadena1 = "Juan Bautista Juan"
cadena2= "Mi nombre es "
cadena3 = "prueba"
cadena4 = "110"
cadena5 = "abcde"

# Convierte la cadena en MAYÚSUCLAS
print(cadena1.upper())

# Convierte la cadena en minúsculas
print(cadena2.lower())

# Convierte la primera letra en mayúscula
print(cadena3.capitalize())

# Buscar una letra dentro de una cadena (si no hay coincidencias devuelve -1) 
print(cadena1.find(" "))

# Buscar una letra dentro de una cadena (si no hay coincidencias, lanza una excepión)
print(cadena1.index("J"))

# (Se usa en cadenas en donde hay números) Si es numérico, devuelve true
print(cadena4.isnumeric())

# Si es alfanumérico, deuvelve true (no debe haber espacio entre las letras)
print(cadena5.isalpha())

# Contamos coincidencias de una cadena dentro de otra (devuelve la cantidad de veces que concida)
contador = cadena1.count("Juan")
print(contador)

# Contamos cuantos caracteres tiene una cadena 
contar_caracteres = len(cadena1)
print(contar_caracteres)

# Verifica si una cadena empieza con otra cadena dada (si es verdadero devueve true)
empieza_con = cadena1.startswith("J")
print(empieza_con)

# Verifica si una cadena termina con otra cadena dada
termina_con = cadena1.endswith("n")
print(termina_con)

# Remplaza un pedazo de la cadena, por otro
remplaza = cadena1.replace("Juan", "Juanci", 1)
print(remplaza)

# Separar cadena, por la cadena que le pasemos 
separar_cadena = cadena1.split("a")
print(separar_cadena)