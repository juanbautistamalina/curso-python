
distancia = int(input("¿A cuántos kilómetros te encuentras de la universidad?: "))
numero_hermanos = int(input("¿Cuántos hermanos posees?: "))
salario_familiar = int(input("Introduce tu salario familiar: "))


if distancia>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("Tienes derecho a beca.")
else:
    print("No tienes derecho a beca. ")