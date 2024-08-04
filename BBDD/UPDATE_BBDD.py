# Importando libreria
import sqlite3

mi_conexion = sqlite3.connect("GestionProductos") # Creando una conexión a la base de datos

mi_cursor = mi_conexion.cursor() # Creando un puntero o cursor

# Haciendo un UPDATE (actualización de datos)
mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO = 50000 WHERE NOMBRE_ARTICULO = 'Zapatillas'")


# Confirmando los cambios
mi_conexion.commit()


mi_conexion.close() # Cerrando conexión
