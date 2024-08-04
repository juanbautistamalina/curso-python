def calculos(): 
    
    try: 
        num_1 = float(input("Introduce el primer número: "))
        num_2 = float(input("Introduce el segundo número: "))
        
        resultado = num_1/num_2
        print("La división es: ", resultado)
        
        print("Fin de la función...")
    
    except ZeroDivisionError: 
        print("No se puede dividir entre cero")
    
    except ValueError:
        print("El valor introducido es erroneo")

calculos()
