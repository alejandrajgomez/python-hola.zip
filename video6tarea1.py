# Ejercicio 1
class Vehiculo():
    color = ()
    ruedas = ()
    puertas = ()
    
    
class Coche(Vehiculo):
    velocidad = ()
    cilindrada = ()
    
c = Coche()
c.color = "Dorado"   
c.ruedas = 4
c.puertas = 2
c.velocidad = 350
c.cilindrada = 1400


print("Mi auto es ",c.color)
print("Tiene ",c.ruedas," ruedas")
print("tambien ",c.puertas," puertas")
print("puede llegar a la velocidad de ",c.velocidad)
print("y ",c.cilindrada," es su cilindrada")
        
