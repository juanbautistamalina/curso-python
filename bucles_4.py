# continue: Se coloca dentro de condicionales y bucles para NO ejecutar lo que sigue y volver al inicio del bucle o 
# condicion. 

frase = input("Introduce una frase: ")
contador = 0

for i in frase: 
    
    if i == ' ':
        continue
    
    contador+=1

print("La frase ingresada tiene ", contador, " letras o caracteres. ")