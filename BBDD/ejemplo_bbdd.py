# Importando libreria
import sqlite3

mi_conexion = sqlite3.connect("PrimeraBase") # Creando una conexión a la base de datos

mi_cursor = mi_conexion.cursor() # Creando un puntero o cursor

# Creando una tabla en una base de datos (se ejecuta una sola vez)
#mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# Insertando un solo dato en la tabla
#mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('Ajedrez', 15000, 'Juego de Mesa' )")


# Insertando un lote de registros en la tabla
"""
varios_productos = [
    ("Remeras", 10000, "Deportes"),
    ("Zapatillas", 30000, "Deportes"),
    ("Computadoras", 200000, "Tecnología")
]

mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", varios_productos)
"""

# Visualizando los registros de la tabla por consola
mi_cursor.execute("SELECT * FROM PRODUCTOS")
lista_registros = mi_cursor.fetchall() # fetchall devuelve una lista con todos los registros que devuelve sql.

for producto in lista_registros:
    print(producto)

# Confirmando los cambios
mi_conexion.commit()


mi_conexion.close() # Cerrando conexión
