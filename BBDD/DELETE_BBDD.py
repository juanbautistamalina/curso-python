# Importando libreria
import sqlite3

mi_conexion = sqlite3.connect("GestionProductos") # Creando una conexión a la base de datos

mi_cursor = mi_conexion.cursor() # Creando un puntero o cursor

# Haciendo un DELETE (eliminación de datos)
mi_cursor.execute("DELETE FROM PRODUCTOS WHERE ID = 2")


# Confirmando los cambios
mi_conexion.commit()


mi_conexion.close() # Cerrando conexión
