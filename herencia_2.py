class Persona():
    
    def __init__(self, nombre, edad, domicilio):
         self.nombre = nombre 
         self.edad = edad
         self.domicilio = domicilio
         
    def descripcion(self):
        print("Nombre: ", self.nombre, "| Edad: ", self.edad, "| Domicilio: ", self.domicilio)
    
class Empleado(Persona): 
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, domicilio_empleado):
        
        # Este método permite utilizar el método de la clase padre en una clase hija
        # Entonces le paso por parámetros los parámetros del constructor de esta clase al constructor de la clase padre.
        super().__init__(nombre_empleado, edad_empleado, domicilio_empleado)
        
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "| Antiguedad: ", self.antiguedad)
        
        



miEmpleado = Empleado(50000, 5, "Juan", 20, "Estados Unidos")
miEmpleado.descripcion()

