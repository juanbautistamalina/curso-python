from io import open

archivo_txt = open("archivo.txt", "r+") 

nombre = input("Introduce tu nombre: ")

archivo_txt.write("Hola Master, tu nombre es "+nombre+" y sos un maquina!")

