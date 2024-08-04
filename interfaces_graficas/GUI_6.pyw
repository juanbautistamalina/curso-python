from tkinter import * 
from tkinter import filedialog

raiz = Tk()

# initialdir sirve para seleccionar una ruta 
# filetypes sirve para especificar el tipo de archivo a examinar
def abre_archivo():
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="c:/", filetypes=(("Archivos PDF", "*.pdf"), 
    ("Archivos de texto", "*txt"), ("Todos los archivos", "*.*")))
    print(archivo) # Imprime la ruta del archivo seleccionado

boton = Button(raiz, text="Abir Archivo", command=abre_archivo).pack()



raiz.mainloop()