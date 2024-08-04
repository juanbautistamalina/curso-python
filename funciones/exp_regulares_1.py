import re

cadena = "Utilizando expresiones regulares"

if re.search("expresiones", cadena) is not None:
    print("He encontrado el texto")

else: 
    print("No he encontrado el texto")

# search() Devuelve un objeto en caso de encontrarlo y None en caso de no encontrarlo. 


# Otros métodos: 
cadena_1 = "Prueba de búsqueda de texto"
cadena_2 = "búsqueda"
texto_encontrado = re.search(cadena_2, cadena_1)
print(texto_encontrado.start()) # start() deuvelve el número de carácter donde comienza a encontrar el texto.
print(texto_encontrado.end()) # end() deuvelve el número de carácter donde termina el texto.
print(texto_encontrado.span()) # span() es una combinación de start y end (devuelve una tupla con los 2 valores)

cadena_1 = "Python es un lenguaje de programación. Python posee una sintaxis sencilla. Python es fácil de aprender"
cadena_2 = "Python"
print(re.findall(cadena_2, cadena_1)) # findall() devuelve una tupla con la palabra repetida en una cadena