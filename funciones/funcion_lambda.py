# Función Normal
def area_triangulo(base, altura):
    return (base*altura) / 2

"""Función lambda: Primero se coloca la palabra clave lambda, posteriormente los parámetros, a continuación
    2 puntos (que serían el equivalente del return) y posteriormente el cálculo que queremos que nos devuelva
"""
area_t = lambda base, altura: (base*altura) / 2
print(area_t(2,2))