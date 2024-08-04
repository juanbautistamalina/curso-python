""" En este ejemplo, la función decoradora sirve para mostrar un mensaje por consola antes de realizar
    un cálculo y luego, una vez realizado dicho cálculo, mostrar otro mensaje."""

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args): # *args sirve para decirle a la función que puede recibir parámetros
        print("Se va a realizar un cálculo: ")
        funcion_parametro(*args)
        print("Se ha terminado la ejecución")
    return funcion_interior

@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)
    

suma(10,5)
resta(50, 30)