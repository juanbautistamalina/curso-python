""" Crea un programa que pida dos números por teclado. El programa tendrá una función 
llamada “DevuelveMax” encargada de devolver el número más alto de los dos
introducidos. """

def DevuelveMax(n1, n2):
    if n1 > n2:
        print("El primer número (",n1,") es mayor que el segundo (",n2,")")
    elif n2>n1:
        print("El segundo número (",n2,") es mayor que el primero (",n1,")")
    else:
        print( "Los números introducidos son iguales")




numero_1 = int(input("Introduce el primer número: "))
numero_2 = int(input("Introduce el segundo número: "))
DevuelveMax(numero_1, numero_2)

