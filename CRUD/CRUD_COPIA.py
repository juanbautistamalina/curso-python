from tkinter import * 
from tkinter import messagebox
import sqlite3

# ------------- RAIZ ------------- 
raiz = Tk()
raiz.title("CRUD")

# ------------- FRAME ------------- 
mi_frame = Frame()
mi_frame.pack()

# ------------- VARIABLE DE CONTROL ------------- 
base_datos = False

# ------------- FUNCIONES ------------- 

def conectar_bbdd():
    try:
        mi_conexion = sqlite3.connect("Usuarios") # Creando conexión a la base de datos
        mi_cursor = mi_conexion.cursor() # Creando un puntero o cursor
    
        mi_cursor.execute("""CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NOMBRE_USUARIO VARCHAR(50) UNIQUE,
            CONTRASENIA VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100)
            )""")
    
        mi_conexion.close() # Cerrando conexión
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
        
        # Interruptor
        global base_datos
        base_datos = True
        

    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")


def salir_app():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if(valor == "yes"):
        raiz.destroy() # Cierra la ventana



def vaciar_datos():
    cuadro_id.delete(0, END)
    cuadro_nombre.delete(0, END)
    cuadro_pass.delete(0, END)
    cuadro_apellido.delete(0, END)
    cuadro_direccion.delete(0, END)
    cuadro_comentario.delete(1.0, END)
    
    
""" Esta función tiene una variable global llamada base_datos. Esta variable por defecto
    está iniciada en False.
    
    Su funcionamiento es el siguiente: 
    - Si el usuario intenta insertar un usuario, sin 
        haber creado previamente la basa de datos, el método irá al else, creará la base
        de datos y posteriormente insertará el registro. 
    
    - Si la base de datos ya existe, inserta el registro
    """

# SOLUCIONAR MENSAJE QUE SALTA A VECES DE QUE YA EXISTE LA BBDD <---
def insertar_datos_bbdd():
    
    global base_datos
    
    if(base_datos == True):
        mi_conexion = sqlite3.connect("Usuarios") # Creando conexión a la base de datos
        mi_cursor = mi_conexion.cursor() # Creando un puntero
        
        
        datos_usuario = [cuadro_nombre.get(), 
                        cuadro_pass.get(), 
                        cuadro_apellido.get(), 
                        cuadro_direccion.get(),
                        cuadro_comentario.get("1.0", "end-1c")] # Toma desde el carácter 0 hasta el final
        
        try:
            # Insertando datos en la tabla
            mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, ?, ?, ?, ?, ?)", datos_usuario)
            
            mi_conexion.commit() # Confirmando los cambios
            mi_conexion.close() # Cerrando conexión
            messagebox.showinfo("BBDD", "Registro insertado con éxito")
        
        except sqlite3.IntegrityError:
            messagebox.showwarning("¡Atención!", "El nombre de usuario ya existe")
        base_datos = True
        
    else:
        conectar_bbdd()
        base_datos = True
        insertar_datos_bbdd()


def leer_datos_bbdd():
    
    try: 
        mi_conexion = sqlite3.connect("Usuarios") # Creando conexión a la base de datos
        mi_cursor = mi_conexion.cursor() # Creando un puntero o cursor
        
        id_usuario = cuadro_id.get()
        
        # Haciendo un READ (lectura)
        mi_cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID = (?)", id_usuario)

        datos_usuario = mi_cursor.fetchall()
        
        # Borrando datos en pantalla actuales
        cuadro_nombre.delete(0, END)
        cuadro_pass.delete(0, END)
        cuadro_apellido.delete(0, END)
        cuadro_direccion.delete(0, END)
        cuadro_comentario.delete(1.0, END)
        
        # Obteniendo e insertando los datos de la bbdd en la interfaz gráfica
        cuadro_nombre.insert(0, datos_usuario[0][1])
        cuadro_pass.insert(0, datos_usuario[0][2])
        cuadro_apellido.insert(0, datos_usuario[0][3])
        cuadro_direccion.insert(0, datos_usuario[0][4])
        cuadro_comentario.insert(1.0, datos_usuario[0][5])
        
        mi_conexion.commit() # Confirmando los cambios
        mi_conexion.close() # Cerrando conexión
        
    except sqlite3.ProgrammingError:
        messagebox.showwarning("BBDD", "Los campos están vacíos")
    
    except IndexError:
        messagebox.showwarning("BBDD", "El usuario ingresado no existe")
        

def actualizar_datos_bbdd():
    mi_conexion = sqlite3.connect("Usuarios") # Creando conexión a la base de datos
    mi_cursor = mi_conexion.cursor() # Creando un puntero o cursor
    
    #id_usuario = cuadro_id.get()
    datos_usuario = [cuadro_nombre.get(), 
                    cuadro_pass.get(), 
                    cuadro_apellido.get(), 
                    cuadro_direccion.get(),
                    cuadro_comentario.get("1.0", "end-1c"),
                    cuadro_id.get()]
    
    mi_cursor.execute("""UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = ?,
                         CONTRASENIA = ?,
                         APELLIDO = ?,
                         DIRECCION = ?,
                         COMENTARIOS = ?
                         WHERE ID = ?""", datos_usuario) 
       
    mi_conexion.commit() # Confirmando los cambios
    mi_conexion.close() # Cerrando conexión
    messagebox.showinfo("BBDD", "Registro modificado con éxito")




def borrar_datos_bbdd():
    mi_conexion = sqlite3.connect("Usuarios") # Creando conexión a la base de datos
    mi_cursor = mi_conexion.cursor() # Creando un puntero o cursor
    
    id_usuario = cuadro_id.get()
    mi_cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID = (?)", id_usuario)
    
    mi_conexion.commit() # Confirmando los cambios
    mi_conexion.close() # Cerrando conexión
    messagebox.showinfo("BBDD", "Registro borrado con éxito")



def info_licencia():
    messagebox.showinfo("Licencia", "Este programa está protegido por derechos de autor. Todos los derechos reservados.")


def info_acerca_de():
    messagebox.showinfo("Acerca de", "Versión del Software 1.0 - CRUD (Desarrollado en Python)")



# ------------- BARRA DE OPCIONES SUPERIOR ------------- 
barra_menu = Menu(raiz) # Creando objeto
raiz.config(menu=barra_menu, width=300, height=300) # Asignándolo a la raíz (mostrandolo en la interfaz)


# OPCION BBDD
bbdd = Menu(barra_menu, tearoff=0) #tearoff = 0 desactiva un separador visual
barra_menu.add_cascade(label="BBDD", menu=bbdd) # Añadiendo el texto de BBDD

# submenus BBDD
bbdd.add_command(label="Conectar", command = conectar_bbdd) 
bbdd.add_command(label="Salir", command=salir_app)

#...........................................................

# OPCION BORRAR
borrar = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Borrar", menu=borrar) # Añadiendo el texto de Borrar

# submenus BORRAR
borrar.add_command(label="Vaciar Campos", command = vaciar_datos) 

#...........................................................

# OPCION CRUD
crud = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="CRUD", menu=crud) # Añadiendo el texto de CRUD

# submenus CRUD
crud.add_command(label="Crear", command = insertar_datos_bbdd) 
crud.add_command(label="Leer", command =  leer_datos_bbdd) 
crud.add_command(label="Actualizar", command = actualizar_datos_bbdd)
crud.add_command(label="Borrar", command = borrar_datos_bbdd)

#...........................................................

# OPCION AYUDA
ayuda = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=ayuda) # Añadiendo el texto de Ayuda

# submenus AYUDA
ayuda.add_command(label="Licencia", command = info_licencia) 
ayuda.add_command(label="Acerca de...", command = info_acerca_de) 



# ------------- TÍTULOS DE LOS CUADROS ------------- 
titulo_id = Label(mi_frame, text="ID:")
titulo_id.grid(row=0, column=0, sticky="w", pady=10, padx=10)

titulo_nombre = Label(mi_frame, text="Nombre:")
titulo_nombre.grid(row=1, column=0, sticky="w", pady=10, padx=10)

titulo_pass = Label(mi_frame, text="Contraseña:")
titulo_pass.grid(row=2, column=0, sticky="w", pady=10, padx=10)

titulo_apellido = Label(mi_frame, text="Apellido:")
titulo_apellido.grid(row=3, column=0, sticky="w", pady=10, padx=10)

titulo_direccion = Label(mi_frame, text="Dirección:")
titulo_direccion.grid(row=4, column=0, sticky="w", pady=10, padx=10)

titulo_comentario = Label(mi_frame, text="Comentario:")
titulo_comentario.grid(row=5, column=0, sticky="w", pady=10, padx=10)


# ------------- FILAS Y COLUMNAS (CUADROS) ------------- 
cuadro_id = Entry(mi_frame)
cuadro_id.grid(row=0, column=1, pady=10, padx=10)

cuadro_nombre = Entry(mi_frame)
cuadro_nombre.grid(row=1, column=1, pady=10, padx=10)

cuadro_pass = Entry(mi_frame)
cuadro_pass.config(fg="green", show="*") # show="*" para que remplaze las letras por asteriscos
cuadro_pass.grid(row=2, column=1, pady=10, padx=10)


cuadro_apellido = Entry(mi_frame)
cuadro_apellido.grid(row=3, column=1, pady=10, padx=10)


cuadro_direccion = Entry(mi_frame)
cuadro_direccion.grid(row=4, column=1, pady=10, padx=10)


cuadro_comentario = Text(mi_frame, width=16, height=5)
cuadro_comentario.grid(row=5, column=1, pady=10, padx=10)


# ------------- BOTONES INFERIORES ------------- 
boton_create = Button(mi_frame, text="Create", command = insertar_datos_bbdd)# El parámetro command 
boton_create.grid(row=6, column=0, pady=10, padx=10, sticky="w")

boton_read = Button(mi_frame, text="Read", command = leer_datos_bbdd) # El parámetro command 
boton_read.grid(row=6, column=1, pady=10, padx=10, sticky="w")

boton_update = Button(mi_frame, text="Update", command = actualizar_datos_bbdd) # El parámetro command 
boton_update.grid(row=6, column=2, pady=10, padx=10, sticky="w")

boton_delete = Button(mi_frame, text="Delete", command = borrar_datos_bbdd) # El parámetro command 
boton_delete.grid(row=6, column=3, pady=10, padx=10, sticky="w")






# Mostrando la ventana
raiz.mainloop()