import pickle

class Persona: 
    
    # Constructor que inicializa propiedades y avisa por consola que se ha creado una nueva persona
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de: ", self.nombre )
    
    
    # Reemplaza las llaves por las propiedades nombre, género y edad. Siguiendo ese orden. 
    def __str__(self):
        return f"{self.nombre} {self.genero} {self.edad}"
    

class ListaPersonas:
    
    # Lista que va a ser usada para grabar y leer la información
    personas = []
    
    
    # Constructor que crea una variable encargada de crear/abrir el archivo externo en modo apertura binaria
    def __init__(self):
        lista_de_personas = open("nombrePersonas", "ab+")
        lista_de_personas.seek(0) # Desplazo el cursor a la posición 0, al comienzo
        
        
        try:
            self.personas = pickle.load(lista_de_personas) # Cargo lo que ya tenía la lista de personas 
                                                           #en el archivo externo
            print(f"Se cargaron {len(self.personas)} personas del fichero externo: ")
            
        except:
            print("El archivo está vacío")
        
        finally:
            lista_de_personas.close() # Cierro el archivo para que no consuma memoria
            del(lista_de_personas) # Borro la variable
        
        
    def agregar_personas(self, p):
        self.personas.append(p) # Se añade a la lista a la persona que se le pase por parámetros al método
        self.guardar_personas_en_archivo_externo()
        
    def guardar_personas_en_archivo_externo(self):
        lista_de_personas = open("nombrePersonas", "wb") # Abro nuevamente el archivo externo en modo escritura binaria
        pickle.dump(self.personas, lista_de_personas) # Toma la lista de personas y las guarda o vuelca en el archivo externo
        lista_de_personas.close() # Cierro el archivo externo
        del(lista_de_personas) # Borro la variable
        
    
    # Este método recorre la lista personas (creada al inicio de la clase) con un bucle, mostrando el nombre, género y la edad
    def mostrar_info_archivo_externo(self):
        print("La información del archivo externo es la siguiente: ")
        for i in self.personas: 
            print(i)
    
    """ El método __str__() no se llama explícitamente, pero es utilizado implícitamente por la función print() 
        cuando se imprime un objeto de la clase Persona."""
    

mi_lista = ListaPersonas()
persona = Persona("Kevin", "Masculino", 22)
mi_lista.agregar_personas(persona)   
mi_lista.mostrar_info_archivo_externo()




"""
En primer lugar se crea un objeto de tipo ListaPersonas, esto va directo al constructor lo que crea una variable encargada
a su vez de crear un archivo externo llamado nombrePersonas con el modo apertura binaria. Luego se posiciona el 
cursor en la posición 0, es decir, al inicio.
Posteriormente al ser la primera vez que se ejecuta el programa (es decir que el archivo está completamente vacío)
lo que va a pasar es que el try no se va a ejecutar, ya que la lista está vacía, entonces el flujo del programa
va a dirigirse al except y va a imprimir por consola "El archivo está vacío".
Luego de eso, ejecutará lo que hay en el finnaly que sería cerrar el archivo y borrar la variable. 

En segundo lugar, se crea una variable llamada persona que es un objeto o instancia de la clase Persona, y se le pasan
por parámetros el nombre ("Juan"), el género ("Masculino") y la edad (21). Esto va directo al constructor de la clase
Persona lo que inicializa las variables e imprime por pantalla "Se ha creado una persona nueva con el nombre de Juan".

En tercer lugar, se utiliza al objeto mi_lista de la clase ListaPersonas, y se hace uso sel método agregar personas
pasándole por parámetros la persona antes creada (en este caso: Juan Masculino 21) 
Al dirigirse a ese método se añade a la persona a la lista haciendo uso del método append y luego
se llama al método guardar_personas_en_archivo_externo. 
Este método primero abre el archivo en modo escritura binaria, luego pasa lo que hay en la lista personas y lo 
vuelca o lo guarda en el archivo externo, luego cierra el archivo externo y borra la variable que lo contenía.

Finalmente se hace uso del método mostrar_info_archivo_externo, el cual primero muestra por consola el siguiente
mensaje "La información del archivo externo es la siguiente: ", y finalmente recorre la lista personas con un bucle
for y a cada vuelta imprime lo que contiene la lista. En caso de que sólo se haya añadido a 1 sola persona aparecería:
Por ejemplo: Juan Masculino 21. 
------------------------------------------------------------------

- Archivo externo: Se crea archivo externo llamado nombrePersonas

- En consola: Al ser la primera ejecución, primero se muestra 
    "El archivo está vacío"
    "Se ha creado una persona nueva con el nombre de Juan"
    "La información del archivo externo es la siguiente: "
    "Juan Masculino 21"
"""