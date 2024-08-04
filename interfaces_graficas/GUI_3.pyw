# Trabajando con Botones de Radio (Selección uno u otro)

from tkinter import *

raiz = Tk()

""" Esta función evalúa el valor de la variable opción, y guarda un texto u otro a la variable etiqueta
    dependiendo del valor de la variable opción entes mencionado (1 o 2). En este caso, sería lo que el usuario
    pulse (no escribe nada)"""
def imprimir(): 
    
    if opcion.get()==1:
        etiqueta.config(text="Has elegido Masculino")

    else:
        etiqueta.config(text="Has elegido Femenino")

Label(raiz, text="Género").pack()

opcion = IntVar() # Le digo a la variable que va a almacenar valores de tipo entero

# Creo los botones, con el texto correspondiente, y las uno a la variable opción. Devuelven un valor numérico
# Les asigno el comando, en este caso una función.
Radiobutton(raiz, text="Masculino", variable=opcion, value=1, command=lambda:imprimir()).pack()
Radiobutton(raiz, text = "Femenino", variable=opcion, value=2, command= lambda:imprimir()).pack()


etiqueta = Label(raiz)
etiqueta.pack()



raiz.mainloop() 