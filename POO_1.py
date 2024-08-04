class Coche():
    
    # Método Constructor
    def __init__(self):
        
        # Propiedades 
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__encendido = False
        
        # Encapsulando o privatizando una variable o propiedad con el doble barra baja (self.__propiedad)
        self.__ruedas = 4
        
    
    # Métodos
    def encencer(self, arrancamos):
        
        self.__encendido = arrancamos
        
        # Este condicional realiza el chequeo interno en caso de que lo pasado por parámetros sea True
        if(self.__encendido == True):
            chequeo = self.__chequeo_interno()

        # Esta sentencia comprueba que el coche esté encendido y que el chequeo haya ido bien
        if self.__encendido == True and chequeo == True:
            return "El coche está en marcha"
        
        # Esta sentencia comprueba que el coche esté encendido pero que el chequeo haya ido mal
        elif(self.__encendido == True and chequeo == False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        
        # Esta sentencia contempla el caso de que no se haya encendido el coche
        else:
            return "El coche está apagado"
    
    def informacion(self):
        print("El coche tiene ", self.__ruedas," ruedas. Un ancho de ", self.__anchoChasis," y un largo de ", 
              self.__largoChasis)
    
    
    def __chequeo_interno(self):
        print("== Realizando chequeo interno ==")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        
        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas": 
            return True
        else:
            return False
        

# Instancia de clase / Objeto de clase
print("Creando un primer objeto de tipo Coche")
miCoche = Coche()

print(miCoche.encencer(True))
miCoche.informacion()


print("------------Creando un segundo objeto de tipo Coche----------------")
miCoche2 = Coche()

print(miCoche2.encencer(False))
miCoche2.informacion()

