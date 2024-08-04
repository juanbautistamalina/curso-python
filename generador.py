# Función Tradicional 
def generaPares(limite):
    num=1 
    miLista = []
    
    while num<limite:
        miLista.append(num*2)
        num = num+1
    
    return miLista

# Generador
def generador_Pares(limite):
    num=1 
   
    while num<limite:
        yield num*2
        num = num+1





print("Función Normal: ", generaPares(10))

print("Generador: ")
devuelve_pares = generador_Pares(11)
for i in devuelve_pares: 
    print(i)