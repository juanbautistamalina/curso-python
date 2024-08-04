from io import open

archivo_txt = open("archivo.txt", "r") # Modo Lectura

lineas_texto = archivo_txt.readlines()

archivo_txt.close 

print(lineas_texto)