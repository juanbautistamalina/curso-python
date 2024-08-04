from io import open 

# Si no existe el archivo, el método open() lo crea. 
archivo_txt = open("archivo.txt", "w") # Abriendo el archivo

frase = """Esto es un texto almacenado 
en un archivo txt. Esto es mas texto. """

archivo_txt.write(frase) # Escribiendo texto 

archivo_txt.close() # Cerrando el archivo