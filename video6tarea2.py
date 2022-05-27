#Ejercicio 2
class Alumno():
    
    def inicio(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        
    def impresion(self):
        print("Nombre alumno:" ,self.nombre)
        print("Su nota: ",self.nota)
        
    def resultado(self):
        if (self.nota>=6):
            print("El alumno está aprobado")
        else:
            print("El alumno está desaprobado")
            
a1 = Alumno()
a1.inicio("Ian",9.2)
a1.impresion()
a1.resultado()

a2 = Alumno()
a2.inicio("Alejandra",5.2)
a2.impresion()
a2.resultado()
