from tkinter import * 
from tkinter import messagebox
import sqlite3

# ------------- RAIZ ------------- 
raiz = Tk()
raiz.title("CRUD")

# ------------- FRAME ------------- 
mi_frame = Frame()
mi_frame.pack()

# ------------- FUNCIONES ------------- 

""" conectar_bbdd(): Esta función posee un try que intentará ejecutar todo lo referente a la creación
    de la base de datos. En caso de que arroje una excepción, mostrará un cartel en pantalla advirtiendo
    que la base de datos ya existe. """
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
        
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")



def salir_app():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if(valor == "yes"):
        raiz.destroy() # Cierra la ventana (interfaz gráfica)



def vaciar_datos():
    cuadro_id.delete(0, END)
    cuadro_nombre.delete(0, END)
    cuadro_pass.delete(0, END)
    cuadro_apellido.delete(0, END)
    cuadro_direccion.delete(0, END)
    cuadro_comentario.delete(1.0, END)
    
    
    
""" insertar_datos_bbdd(): Esta función posee inicialmente un try que en caso de ser posible, conectará
    con la base de datos, creará el cursor y creará una lista en la cual se almacenarán los datos escritos
    en los cuadros de la interfaz gráfica. Luego hay un try dentro del try inicial, el cual intentará
    insertar un usuario mediante comandos SQL, y en caso de una excepción arrojará un cartel en la pantalla
    informando de que el nombre de usuario ya existe.
    
    Finalmente está el except del primer try, el cual se ejecutaría en el caso de que el usuario intente
    insertar un usuario sin haber creado la base de datos previamente: En ese caso, se llama primero a la 
    función conectar_bbdd y luego se llama a sí misma, es decis, a la función insertar_datos, para que así
    se cree la base de datos y luego con esa llamada a sí misma se inserten los datos. """
def insertar_datos_bbdd():
    
    try:
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

    except:
        conectar_bbdd()
        insertar_datos_bbdd()


""" leer_datos_bbdd(): Esta función, posee un try que primero realiza la conexión a la base de datos, 
    luego almacena en una variable lo que el usuario haya colocado en el cuadro gráfico ID. 
    Con ese ID que haya introducido el usuario, se ejecuta un comando SQL que realiza una consulta a la
    Base de Datos y guarda en una lista llamada datos_usuarios los datos traídos de la base de
    datos que estén asociados al ID introducido. 
    Posteriormente, se limpian los datos que estén escritos en los cuadros de texto de la interfaz gráfica
    y luego se insertan los datos de la lista datos_usuarios (obtenidos de la base de datos) de forma
    ordenada en los cuadros de texto de la interfaz gráfica. 
    
    En cuanto a los except posee 2 casos: (En ambos casos se muestra un cartel gráfico notificando)
    
    - sqlite3.ProgrammingError: Contempla la posibilidad de que los campos estén vacíos
    
    - IndexError: Contempla la posibilidad de que el ID ingresado no esté asociado a ningún usuario.
    Por lo que el usuario no existe. 
"""
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
        
        # Obteniendo e insertando los datos obtenidos de la bbdd en la interfaz gráfica
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
        
        
"""
FALTA HACER ESTE COMENTARIO. 

"""
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


"""
    FALTA HACER ESTE COMENTARIO
"""
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


# OPCION BORRAR
borrar = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Borrar", menu=borrar) # Añadiendo el texto de Borrar
# submenus BORRAR
borrar.add_command(label="Vaciar Campos", command = vaciar_datos) 


# OPCION CRUD
crud = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="CRUD", menu=crud) # Añadiendo el texto de CRUD
# submenus CRUD
crud.add_command(label="Crear", command = insertar_datos_bbdd) 
crud.add_command(label="Leer", command =  leer_datos_bbdd) 
crud.add_command(label="Actualizar", command = actualizar_datos_bbdd)
crud.add_command(label="Borrar", command = borrar_datos_bbdd)


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
cuadro_pass.config(fg="green", show="*") # show="*" para que reemplaze las letras por asteriscos
cuadro_pass.grid(row=2, column=1, pady=10, padx=10)

cuadro_apellido = Entry(mi_frame)
cuadro_apellido.grid(row=3, column=1, pady=10, padx=10)

cuadro_direccion = Entry(mi_frame)
cuadro_direccion.grid(row=4, column=1, pady=10, padx=10)

cuadro_comentario = Text(mi_frame, width=16, height=5)
cuadro_comentario.grid(row=5, column=1, pady=10, padx=10)
barra_scroll = Scrollbar(mi_frame, command= cuadro_comentario.yview)
barra_scroll.grid(row = 5, column = 2, sticky="nsew")
cuadro_comentario.config(yscrollcommand = barra_scroll.set)

# ------------- BOTONES INFERIORES ------------- 

frame_inferior = Frame(raiz)
frame_inferior.pack()

boton_create = Button(frame_inferior, text="Create", command = insertar_datos_bbdd)
boton_create.grid(row=1, column=0, pady=10, padx=10, sticky="w")

boton_read = Button(frame_inferior, text="Read", command = leer_datos_bbdd)
boton_read.grid(row=1, column=1, pady=10, padx=10, sticky="w")

boton_update = Button(frame_inferior, text="Update", command = actualizar_datos_bbdd)
boton_update.grid(row=1, column=2, pady=10, padx=10, sticky="w")

boton_delete = Button(frame_inferior, text="Delete", command = borrar_datos_bbdd)
boton_delete.grid(row=1, column=3, pady=10, padx=10, sticky="w")


# Mostrando la ventana (interfaz gráfica)
raiz.mainloop()