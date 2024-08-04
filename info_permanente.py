import pickle

"""
    Explicación del código: 
    
    Clase Personas:
    
        - __init__: Es el constructor, recibe 3 parámetros y se los asigna a 3 variables. También imprime por pantalla 
        un texto avisando que se ha creado una nueva persona y muestra el nombre de la persona. 
    
        - __str__: Este método devuelve una cadena de formato en la que se reemplazarán las llaves {} 
        con los valores correspondientes
    
    
    Clase ListaPersonas:
        Primero se crea una lista vacía
        

"""

class Persona: 
    
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de: ", self.nombre )
    
    
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    

class ListaPersonas:
    personas = []
    
    def __init__(self):
        lista_de_personas = open("archivoExterno", "ab+")
        lista_de_personas.seek(0) # Desplazo el cursor a la posición 0, al comienzo
        
        try:
            self.personas = pickle.load(lista_de_personas) # Cargo la lista de personas en la variable personas
            print("Se cargaron {} personas del fichero externo: ".format(len(self.personas)))
        except:
            print("El archivo está vacío")
        
        finally:
            lista_de_personas.close()
            del(lista_de_personas)
        
    def agregar_personas(self, p):
        self.personas.append(p) # Se añade a la lista a la persona
        self.guardar_personas_en_archivo_externo()
        
    def mostrar_personas(self):
        for p in self.personas:
            print(p)
    
    def guardar_personas_en_archivo_externo(self):
        lista_de_personas = open("archivoExterno", "wb")
        pickle.dump(self.personas, lista_de_personas)
        lista_de_personas.close()
        del(lista_de_personas)
        
    
    def mostrar_info_archivo_externo(self):
        print("La información del archivo externo es la siguiente: ")
        for i in self.personas: 
            print(i)
    
mi_lista = ListaPersonas()
persona_1 = Persona("Juan", "Masculino", 21)
mi_lista.agregar_personas(persona_1)   
mi_lista.mostrar_info_archivo_externo()

