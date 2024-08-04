# Importando libreria
import sqlite3

mi_conexion = sqlite3.connect("GestionProductos") # Creando una conexión a la base de datos

mi_cursor = mi_conexion.cursor() # Creando un puntero o cursor

# Haciendo un READ (lectura)
mi_cursor.execute("SELECT * FROM PRODUCTOS WHERE CATEGORIA ='Tecnología'")

categoria = mi_cursor.fetchall()
print(categoria)


# Confirmando los cambios
mi_conexion.commit()


mi_conexion.close() # Cerrando conexión
