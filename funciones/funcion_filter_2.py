class Empleado:
    
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario



    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)


lista_empleados = [
    Empleado("Juan", "Director", 100000),
    Empleado("Simon", "Presidente", 90000),
    Empleado("Mateo", "Administrativo", 15000),
    Empleado("Kevin", "Secretario", 30000)
]


salarios_altos = list(filter(lambda empleado: empleado.salario > 50000, lista_empleados ))

for e in salarios_altos:
    print(e)
