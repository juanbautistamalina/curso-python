from io import open

archivo_txt = open("archivo.txt", "r") 

print(archivo_txt.read())

archivo_txt.seek(5) # Control del puntero

print(archivo_txt.read())
archivo_txt.close()


