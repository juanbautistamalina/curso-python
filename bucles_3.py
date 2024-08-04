#Importación de clases
import math

numero = int(input("Introduce un número: "))
intentos = 0

while numero<0 and intentos!=2: 
    print("No se puede calcular la raíz de un numero negativo. ")
    
    if numero<0: 
        numero = int(input("Intorduce un número: "))
        intentos+= 1
    
    if intentos==2 and numero<0:
        print("Has excedido el número de intentos. ")
        break
    
    

    

if intentos<=2 and numero>0: 
    resultado = math.sqrt(numero)
    print("La raíz cuadrada de "+ str(numero)+ " es: "+ str(resultado))