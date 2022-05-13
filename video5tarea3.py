import time
import os

#VIDEO 5 TAREA 3
#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(año):
    if(año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        print("El año ",año,"es bisiesto")
        return (True)
    print("El año",año,"no es bisiesto")
    return(False)
bisiesto(1998)


time.sleep(5)
os.system("cls")

