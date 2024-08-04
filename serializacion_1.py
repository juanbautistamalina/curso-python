import pickle

lista = ["Juan", "Bautista", "Malina"] # 1) Creo una lista con nombres

archivo_binario = open("lista_nombres", "wb") # 2) Apertura del archivo en modo escritura binaria (WB)

pickle.dump(lista, archivo_binario) 
# 3) Toma la lista de nombres del paso 1, y lo almacena en la variable archivo_binario en código binario

archivo_binario.close() # Cierro el archivo

del(archivo_binario) 