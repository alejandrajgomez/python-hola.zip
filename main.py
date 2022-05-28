# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.


import pickle

class Vehiculo:
    marca = " "
    modelo = 0
    color = " "

    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f'La marca es {self.marca} el modelo es {self.modelo} y es de color {self.color}'

v1 = Vehiculo("Volvo",1970,"rojo")

print(str(v1))


f = open('vehiculo.bin','wb')
pickle.dump(v1,f)
f.close()

f = open('vehiculo.bin', 'rb')# con esto lo leo
vehiculo = pickle.load(f)
f.close()
print(type(vehiculo))
print("Marca: ",vehiculo.marca, "Modelo: ",vehiculo.modelo, "Color: ",vehiculo.color)