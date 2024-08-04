class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class Moto():
    
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion():
    
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")



# Polimorfismo: El método vehiculo.desplazamiento
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)

