from tkinter import *

# Importando biblioteca de las ventanas emergentes
from tkinter import messagebox


raiz = Tk()


def info_adicional():
    messagebox.showinfo("Información del usuario", "Software registrado a nombre de Juan Bautista Malina")


def info_licencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")


def salir_app():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if(valor == "yes"):
        raiz.destroy() # Cierra la ventana



def cerrar_doc():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento Bloqueado") 


barra_menu = Menu(raiz) # Creando objeto
raiz.config(menu=barra_menu, width=300, height=300) # Asignándolo a la raíz

# Estableciendo cuántos elementos tiene


archivo = Menu(barra_menu, tearoff=0) #tearoff = 0 desactiva un separador visual
archivo.add_command(label="Nuevo") # Añadiendo Submenús (opciones de deriven de las opciones principales: Archivo, Edición, Herramientas, Ayuda)
archivo.add_command(label="Guardar")
archivo.add_command(label="Guardar como")

archivo.add_separator() # Añadiendo separador
archivo.add_command(label="Cerrar", command=cerrar_doc)
archivo.add_command(label="Salir", command=salir_app)


edicion = Menu(barra_menu, tearoff=0)
edicion.add_command(label="Copiar")
edicion.add_command(label="Cortar")
edicion.add_command(label="Pegar")



herramientas = Menu(barra_menu)


ayuda = Menu(barra_menu, tearoff=0)
ayuda.add_command(label="Licencia", command=info_licencia)
ayuda.add_command(label="Acerca de", command=info_adicional)


# Añadiendo el texto de Archivo, el primer elemento del menú
barra_menu.add_cascade(label="Archivo", menu=archivo)

# Añadiendo el texto de Edición, el segundo elemento del menú
barra_menu.add_cascade(label="Edición", menu=edicion)

# Añadiendo el texto de Herramientas, el tercer elemento del menú
barra_menu.add_cascade(label="Herramientas", menu=herramientas)

# Añadiendo el texto de Ayuda, el cuarto elemento del menú
barra_menu.add_cascade(label="Ayuda", menu=ayuda)






raiz.mainloop()