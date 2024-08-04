from tkinter import * 

raiz = Tk()
mi_frame = Frame(raiz, width=600, height=450)

mi_frame.pack()

mi_label = Label(mi_frame, text="Logo Python: : ", fg="blue", font=(50))

# Coloco el texto en un lugar concreto
mi_label.place(x=10, y=0)

# Coloco una imágen
mi_imagen = PhotoImage(file="python.png")
a = Label(mi_frame, image = mi_imagen).place(x=20, y=20)


raiz.mainloop()