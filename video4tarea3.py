import os
import time
os.system("cls")

#VIDEO 4 - TAREA 3
#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
time.sleep(2)   
os.system("cls")

lista = list(range(1,101))
print("Lista normal\n ",lista)
print()
print("Lista en reverse")
for i in reversed(lista):
    print(f"{i}")
time.sleep(20)   
os.system("cls")