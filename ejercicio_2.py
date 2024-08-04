""" Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos 
deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos 
personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por 
teclado). """

Nombre = input("Introduce tu nombre: ")
Direccion = input("Introduce tu dirección: ")
Telefono = int(input("Introduce tu teléfono: "))

mi_lista = [Nombre, Direccion, Telefono]

print("Los datos personales son:")
print("- Nombre: ", Nombre)
print("- Dirección: ", Direccion)
print("- Teléfono: ", Telefono)