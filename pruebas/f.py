from tkinter import Entry


nota = int(input("Ingresa una nota: "))

if(nota == 10):
    print("Excelente")

elif(nota >=7 and nota <=9):
    print("muy bien")

elif(nota >= 4 and nota <=6):
    print("bien")

else:
    print("mal")
