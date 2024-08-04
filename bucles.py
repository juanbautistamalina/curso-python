
correo = input("Introduce tu correo electrónico: ")
punto = 0
arroba = 0
espacio = False

for i in correo:
    
    if i == '@':
        arroba+=1

    if i=='.':
        punto+=1
    
    if i==' ':
        espacio=True

#Chequeo
if arroba == 1 and punto>=1 and espacio== False:
    print("El email es correcto")
else:
    print("El email es incorrecto")
