import os
import time
os.system("cls")

#VIDEO 4 - TAREA 2
# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numero = 1
for numero in range(1,10):
        if numero % 2 != 0:
            print("Numero impar", numero)
print()
time.sleep(2)   
os.system("cls")