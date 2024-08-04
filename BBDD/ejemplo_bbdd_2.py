# Importando libreria
import sqlite3

mi_conexion = sqlite3.connect("GestionProductos") # Creando una conexión a la base de datos

mi_cursor = mi_conexion.cursor() # Creando un puntero o cursor


mi_cursor.execute("""--sql
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE, -- UNIQUE hace que no se pueda repetir la información en un campo
    PRECIO INTEGER,
    CATEGORIA VARCHAR(20))
    """)



# Creando lista de productos
productos = [
    ("Mouse", 10000, "Tecnología"),
    ("Cubo de Rubik", 2000, "Entretenimiento"),
    ("Zapatillas", 45000, "Deporte"),
    ("Mochila", 15000, "Viajes") 
]


# Dejo en el primer espacio NULL para que la base de datos gestione automáticamente el campo clave ID.
mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (null,?,?,?)", productos)


mi_cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL, 'Teclado', 30000, 'Tecnología' )")


# Confirmando los cambios
mi_conexion.commit()


mi_conexion.close() # Cerrando conexión
