from tkinter import * 

raiz = Tk()

mi_frame = Frame(raiz, width=1200, height=600)
mi_frame.pack()


# Variable
minombre = StringVar() # Le decimos que la variable se trata de una cadena



# Instancia de la clase Entry
cuadro_nombre = Entry(mi_frame, textvariable=minombre)
cuadro_nombre.config(fg="red", justify="c")


# Trabajando con filas y columnas
cuadro_nombre.grid(row=0, column=1, pady=10, padx=10)

cuadro_pass = Entry(mi_frame)
cuadro_pass.config(fg="green", show="*") # show="*" para que remplaze las letras por asteriscos
cuadro_pass.grid(row=1, column=1)

cuadro_apellido = Entry(mi_frame)
cuadro_apellido.grid(row=2, column=1, pady=10, padx=10)


cuadro_direccion = Entry(mi_frame)
cuadro_direccion.grid(row=3, column=1, pady=10, padx=10)

# Añadiendo un cuadro de texto más amplio
texto_comentario = Text(mi_frame, width=16, height=5)
texto_comentario.grid(row=4, column=1, pady=10, padx=10)

# Añadiendo una barra de scroll para el texto amplio
barra_scroll = Scrollbar(mi_frame, command=texto_comentario.yview)
barra_scroll.grid(row=4, column=2, sticky="nsew" ) # sticky="nsew" se adapta al largo del texto

texto_comentario.config(yscrollcommand=barra_scroll.set)

# Trabajando con las posiciónes usando grid (filas y columnas empiezan desde 0). 
# sticky: Sirve para especificar el alineamiento (N, S, E, W) -> Puntos cardinales
# pady y padx: Son los espacios horizontales y verticales que hay entre un elemento y otro
label_nombre = Label(mi_frame, text="Nombre:")
label_nombre.grid(row=0, column=0, sticky="w", pady=10, padx=10)

label_direccion = Label(mi_frame, text="Contraseña:")
label_direccion.grid(row=1, column=0, sticky="w", pady=10, padx=10)

label_apellido = Label(mi_frame, text="Appelido:")
label_apellido.grid(row=2, column=0, sticky="w", pady=10, padx=10)

label_direccion = Label(mi_frame, text="Dirección:")
label_direccion.grid(row=3, column=0, sticky="w", pady=10, padx=10)
              
label_comentarios = Label(mi_frame, text="Comentarios:")
label_comentarios.grid(row=4, column=0, sticky="w", pady=10, padx=10)
              


def codigoBoton():
    minombre.set("Juan") 
    
    
    
# Agregando botones
boton_enviar = Button(raiz, text="Enviar", command=codigoBoton) # El parámetro command 
boton_enviar.pack()



raiz.mainloop()