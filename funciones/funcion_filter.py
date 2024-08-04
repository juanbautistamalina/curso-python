""" La función filter verifica que los elementos de una secuencia cumplen 
    una condición, devolviendo un iterador (objeto recorrible) con los elementos
    que cumplen dicha condición. """
num_par = lambda num: num%2 == 0

numeros = [12, 6, 87, 2, 10, 102, 54, 309, 16]

print(list(filter(num_par, numeros)))