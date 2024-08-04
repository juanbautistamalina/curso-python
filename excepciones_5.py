import math
def calcular_raiz(num):
    if num<0: 
       raise ValueError("El número introducido, no puede ser negativo. ")
    
    else:
        return math.sqrt(num)
    
    

numero = int(input("Introduce un número: "))

try: 
    print(calcular_raiz(numero))

# Le doy un alias o nombre propio a la excepción/error. 
except ValueError as NumeroNegativo: 
    print(NumeroNegativo)
    
    