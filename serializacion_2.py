import pickle

lista = open("lista_nombres", "rb") # Lectura Binaria
info = pickle.load(lista)
print(info)