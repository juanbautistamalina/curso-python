import pickle
from serializar import *

archivo_apertura = open("losAutos", "rb")
lista_autos = pickle.load(archivo_apertura)
archivo_apertura.close()

for i in lista_autos:
    print(i.estado())
