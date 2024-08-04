# CheckButtons: Botones de selección para preguntas de respuesta múltiple
from tkinter import *

raiz = Tk()
raiz.title("Libros")

habitos_a = IntVar()
deep_work = IntVar()
club_5am = IntVar()

def opciones_libros():
    
    opcion = ""
    
    if(habitos_a.get() == 1):
        opcion+=" Hábitos Atómicos"
    
    if(deep_work.get()==1):
        opcion+=" Deep Work"

    if(club_5am.get()==1):
         opcion+=" Club de las 5 de la mañana"


    texto_final.config(text= opcion)

# Imágen
imagen = PhotoImage(file="books.png")
Label(raiz, image=imagen).pack()

frame = Frame(raiz)
frame.pack()

Label(frame, text="Selecciona libros de desarrollo personal: ", width=50).pack()


# CheckButtons: 
boton_check = Checkbutton(frame, text=" Hábitos Atómicos", variable=habitos_a, onvalue=1, offvalue=0, command=opciones_libros).pack()
boton_check = Checkbutton(frame, text="Deep Work", variable=deep_work, onvalue=1, offvalue=0, command = opciones_libros).pack()
boton_check = Checkbutton(frame, text=" El club de las 5 de la mañana", variable=club_5am, onvalue=1, offvalue=0, command = opciones_libros).pack()


texto_final = Label(frame)
texto_final.pack()



raiz.mainloop()