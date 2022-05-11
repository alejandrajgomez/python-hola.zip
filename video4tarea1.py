#VIDEO 4 - TAREA 1
# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

import os
import time
os.system("cls")
edad= int(input("Ingrese su edad\n"))

if edad >= 21:
    print("Usted es mayor de edad")
else:
    print("Eres menor de edad, ve a estudiar")
time.sleep(2)   
os.system("cls")