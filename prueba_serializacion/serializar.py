import pickle


class Vehiculos():
    
    def __init__(self, marca, modelo):
         self.marca = marca 
         self.modelo = modelo
         self.enmarcha = False
         self.acelerar = False
         self.frenar = False
         
    def arrancar(self): 
        self.enmarcha = True
    
    def acelerando(self):
        self.acelerar = True
        
    def frenando(self):
        self.frenar = True
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEncendido: ", self.enmarcha,
              "\nAcelerando: ", self.acelerar, "\nFrenando: ", self.frenar)
        

coche1 = Vehiculos("Mazda", "MX5")
coche2 = Vehiculos("Seatr", "Leon")
coche3 = Vehiculos("Renault", "Megane")

coches = [coche1, coche2, coche3]

archivo = open("losAutos", "wb")
pickle.dump(coches, archivo)
archivo.close()
del(archivo)
