from tkinter import *


""" Si cambio la extensión del archivo de .py a .pyw al hacer doble click sobre el archivo, se va a abrir
    la ventana, sin la consola detrás. """

# TRABAJANDO CON LA RAÍZ DE LA VENTANA
raiz = Tk()

# Le doy un título a la ventana
raiz.title("Ventana de Prueba")

# Evitar que se modifique el tamaño de la ventana (0 y 0)
raiz.resizable(1,1) # Ancho (width) y Alto (height)

# Cambiando el ícono de la ventana
raiz.iconbitmap("images.ico")

# Modificando la resolución de la ventana
#raiz.geometry("650x350")

# Cambiando el color de fondo
raiz.config(bg = "red")
"------------------------------------------------------"

# TRABAJANDO CON EL FRAME DE LA VENTANA
mi_frame = Frame()

# Empaquetando el frame (relacionándolo con la raíz)
mi_frame.pack()

# Dándole el tamaño al frame
mi_frame.config(width=650, height=350)

# Haciendo que el frame se expanda en todas las direcciones al agrandar o arhicar la ventana
#mi_frame.pack(fill = "both", expand= "True")

# Dándole color al frame
mi_frame.config(bg="blue")

# Cambiando el borde
mi_frame.config(bd=50)
mi_frame.config(relief = "groove")


# Cambiando el cursor dentro de la ventana
mi_frame.config(cursor="hand2")


# Se muestra la ventana 
raiz.mainloop()