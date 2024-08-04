from tkinter import *


# Creación de la raiz 
raiz = Tk()

mi_frame = Frame(raiz)
mi_frame.config(background="#FFE4B5")
mi_frame.pack()



operacion = "" # Variable para el borrado de pantalla al hacer una operación
resultado = 0  # Variable para el almacenado de los resultados de las operaciones
reset_pantalla = False




# -------------------------------- PANTALLA --------------------------------

numero_pantalla = StringVar() # Variable para que aparezcan los números por pantalla



pantalla = Entry(mi_frame, textvariable=numero_pantalla) # Configurando la pantalla 
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) # Configurando la posición
pantalla.config(background="#DB9286", fg="black", justify="right") # Colores fondo y letra, escritura a la derecha

""" La propiedad columnspan=4 permite expandir la capacidad de la ventana a 4 columnas para que así
    los botones queden alineados."""


# -------------------------------- PULSACIONES TECLADO --------------------------------

""" Este método toma el número que se le pasa por parámetros, a continuación utilizo la palabra reservada global
    par así poder utilizar la variable dentro de la función. 
    
    Luego hay un if, que compara si la variable operación no está vacía; En este caso, se eliminan los números
    de la pantalla, haciendo uso del método set (esto cuando se pulse sobre un nuevo numero).
    
    En caso contrario, es decir, en caso de que la variable operación esté vacía, se van a seguir añadiendo números
    a los que se van pulsando. """

def numero_pulsado(num):
    
    """Permite acceder y modificar la variable dentro de la función, 
        incluso si operacion se define fuera de la función."""
    global operacion 
    
    if operacion != "":
        numero_pantalla.set(num) # Desaparecen los números que había antes, y hay que volver a añadir un valor
        operacion = "" # Le vuelvo a asignar vacío para que vaya al else, y se añadan los números
    
    else:
        numero_pantalla.set(numero_pantalla.get()+num) 


# -------------------------------- FUNCION SUMA --------------------------------

""" Al llamar a la función suma, se le pasa por parámetros lo que hay en la variable numero_pantalla
    haciendo uso del método get. A continuación, se acumula en resultado lo que se le haya pasado por
    parámetros pero convertido a entero (ya que inicialmente será texto). 
    Posteriormente se almacena el texto suma en la variable operación, y finalmente se muestra por la 
    pantalla de la calculadora lo que hay almacenado en resultado. """

def suma(num):
    global operacion
    global resultado
    
    resultado+=int(num) # Se acumula el resultado
    
    operacion = "suma"

    numero_pantalla.set(resultado)



# -------------------------------- FUNCION RESTA --------------------------------

def resta(num):
    global operacion
    global resultado
    
    resultado-=int(num) # Se acumula el resultado
    
    operacion = "resta"

    numero_pantalla.set(resultado)




# -------------------------------- FUNCION RESULTADO FINAL --------------------------------

""" Este método es llamado al pulsar el botón IGUAL: Lo que hace es mostrar el resultado final por pantalla
    entendiendo por eso a lo que ya haya sido sumado, es decir, lo que ya esté almacenado en resultado más 
    el último valor introducido que aún no ha sido sumado. """
def resultado_final():
    
    global resultado

    numero_pantalla.set(resultado+int(numero_pantalla.get()))

    resultado = 0

# -------------------------------- FILA 1 --------------------------------

boton_7 = Button(mi_frame, text="7", width=3, command=lambda:numero_pulsado("7")) 
boton_7.grid(row=2, column=1)

boton_8 = Button(mi_frame, text="8", width=3, command=lambda:numero_pulsado("8")) 
boton_8.grid(row=2, column=2)

boton_9 = Button(mi_frame, text="9", width=3, command=lambda:numero_pulsado("9")) 
boton_9.grid(row=2, column=3)

boton_div = Button(mi_frame, text="÷", width=3) 
boton_div.config(background="#DB9286")
boton_div.grid(row=2, column=4)


# -------------------------------- FILA 2 --------------------------------

boton_4 = Button(mi_frame, text="4", width=3, command=lambda:numero_pulsado("4"))  # Con command muestro el 4 por pantalla
boton_4.grid(row=3, column=1)

boton_5 = Button(mi_frame, text="5", width=3, command=lambda:numero_pulsado("5")) 
boton_5.grid(row=3, column=2)

boton_6 = Button(mi_frame, text="6", width=3, command=lambda:numero_pulsado("6")) 
boton_6.grid(row=3, column=3)

boton_mult = Button(mi_frame, text="x", width=3) 
boton_mult.config(background="#DB9286")
boton_mult.grid(row=3, column=4)


# -------------------------------- FILA 3 --------------------------------

boton_1 = Button(mi_frame, text="1", width=3, command=lambda:numero_pulsado("1")) 
boton_1.grid(row=4, column=1)

boton_2 = Button(mi_frame, text="2", width=3, command=lambda:numero_pulsado("2")) 
boton_2.grid(row=4, column=2)

boton_3 = Button(mi_frame, text="3", width=3, command=lambda:numero_pulsado("3")) 
boton_3.grid(row=4, column=3)

boton_rest = Button(mi_frame, text="-", width=3, command=lambda:resta(numero_pantalla.get())) 
boton_rest.config(background="#DB9286")
boton_rest.grid(row=4, column=4)


# -------------------------------- FILA 4 --------------------------------

boton_0 = Button(mi_frame, text="0", width=3, command=lambda:numero_pulsado("0")) 
boton_0.grid(row=5, column=1)

boton_coma = Button(mi_frame, text=",", width=3, command=lambda:numero_pulsado(".")) 
boton_coma.grid(row=5, column=2)

boton_suma = Button(mi_frame, text="+", width=3, command=lambda:suma(numero_pantalla.get())) 
boton_suma.config(background="#DB9286")
boton_suma.grid(row=5, column=3)

boton_igual = Button(mi_frame, text="=", width=3, command=lambda: resultado_final()) 
boton_igual.config(background= "#8B0000")
boton_igual.grid(row=5, column=4)












# Mostrar la interfaz gráfica
raiz.mainloop()