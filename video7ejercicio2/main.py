# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.

import time

hactual =  time.strftime("%H")
minutos =  time.strftime("%M")

print("La hora actual es: ",hactual,":",minutos)



if int(hactual) >= 19:
    print("Son las ",hactual,":",minutos,"Hora de ir a casa")
   
else:
    horas = 19-1-int(hactual)
    minuto = 60-int(minutos)
    print("restan ",horas," horas, y ", minuto,"minutos de trabajo") 
