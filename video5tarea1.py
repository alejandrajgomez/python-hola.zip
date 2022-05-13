import os
import time

#VIDEO 5 TAREA 1
# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

def area():
    def triangulo(altura,base):
        areatr = (altura*base)/2
        print("El area del triangulo es: ",areatr)
    
    def circulo(radio):
        areac = 3.14 * (radio**2)
        print("El area del circulo es: ",areac)
    triangulo(2.5,5)
    circulo(2.8)

area()

time.sleep(5)
os.system("cls")