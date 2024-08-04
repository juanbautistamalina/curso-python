# Creando clase padre o superclase 
class Vehiculos():
    
    # Constructor 
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
        

class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        
        if self.cargado == True:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
    
    
    
    
# Clase Moto que hereda de la clase Vehículos
class Moto(Vehiculos):
    willy = ""
    
    def tirar_willy(self):
        self.willy = "Estoy tirando willy!"
      
     # Sobreescribiendo un método perteneciente a otra clase
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEncendido: ", self.enmarcha,
              "\nAcelerando: ", self.acelerar, "\nFrenando: ", self.frenar, "\n", self.willy)


class Vehiculos_Electricos(Vehiculos): 
    
    def __init__(self, marca, modelo):
        
        
        super().__init__(marca, modelo)
        self.autonomia = 100
        
        def cargar_energia(self):
            self.cargando = True
            
# Herencia Múltiple:  La clase BiciElectrica hereda de 2 clases
class BiciElectrica(Vehiculos_Electricos, Vehiculos):
    pass
    
#----------------------------------------------------------------------------------------------------------------------
miMoto = Moto("Honda", "CBR")
miMoto.tirar_willy()

# En esta línea se llama al método perteneciente a la clase Moto, ya que sobreescribe al método de la clase Veíhulos
miMoto.estado()

print()

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

print()

miBici = BiciElectrica("MUI", "S1")
miBici.estado()