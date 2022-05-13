import os
import time

#VIDEO 5 TAREA 2
# "Escribe una función que pueda decirte si un número (número entero) es primo o no." 

def primo(num):
    if num==1:
        print("El numero ",num,"no se consiera numero primo")
    else:
        for n in range(2,num):
            if num % n == 0:
                print("El numero ",num," no es numero primo")
                return (False)
        print("El numero ",num, "es numero primo")
        return(False)
primo(17)

time.sleep(5)
os.system("cls")