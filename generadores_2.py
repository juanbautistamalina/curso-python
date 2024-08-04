def devuelve_nombres(*nombres):
    yield nombres

nombres_devueltos = devuelve_nombres("Juan", "Bautista", "Malina")
print(next(nombres_devueltos))
