""" Aplica una función a cada elemento de una lista iterable
    (listas, tuplas, etc) devolviendo una lista con los resultados"""
    
class Empleado:
    
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario



    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)


lista_empleados = [
    Empleado("Juan", "Director", 10000),
    Empleado("Simon", "Presidente", 7500),
    Empleado("Mateo", "Administrativo", 6000),
    Empleado("Kevin", "Secretario", 4500)
]

def calculo_comision(empleado):
    empleado.salario = empleado.salario*1.03
    return empleado


lista = map(calculo_comision, lista_empleados)

for i in lista:
    print(i)