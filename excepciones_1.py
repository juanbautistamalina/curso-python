def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):	
    # Las excepciones son como una especia de if, que protegen al programa de que no se caiga. 
    try: 	
        return num1/num2
    
    except ZeroDivisionError:
        print("No es posible dividir entre cero. ")
        return "Operación Erronea. "

# Bucle infinito, para que el usuario sí o sí deba ingresar 2 números para que el programa funcione
while True: 
# Tomando en cuenta otra excepción: En este caso, contemplo la posibilidad de que el usuario escriba texto. 
	try: 
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))		
		break

	except ValueError: 
         print("Los valores introducidos no son correctos. Vuelve a intentarlo. ")
    
    
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")