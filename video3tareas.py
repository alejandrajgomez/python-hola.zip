# EJERCICIO 1
# Para este ejercicio tenéis que crear en la consola de python variables que representen los siguientes datos de un contacto:
# Nombre
# Apellidos
# Edad
# Email
# Teléfono
# Casado (verdadero o falso)
# Con Hijos (verdadero o falso)
# Lista de amigos
# Películas vistas (diccionario con clave y valor. El valor será el título de la película)
# Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().
# Tienes que subir capturas de pantalla en una carpeta comprimida zip.
print("\n")
print("EJERCICIO 1 - VIDEO 3")
Nombre = "Alejandra"
Apellidos = "Judith"
Edad = 52
Email ="mimail@gmail.com"
Telefono = 1100224488
Casado = False
ConHijos = True
Amigos = ['Juan','Pedro','Maria','Magdalena']
Peliculas ={'clave1':'2012','clave2':'Gladiador','clave3':'Dune'}
print("Mi nombre es "+Nombre+ " y mi apellido es "+Apellidos+ ", tengo "+str(Edad)+" años")
print("Este es mi mail "+Email+" y este mi telefono "+str(Telefono))
print("Casada? "+str(Casado)+" Hijos? "+str(ConHijos))
print("Mis amigos religiosos son "+str(Amigos))
print("He visto estas peliculas "+str(Peliculas))


# EJERCICIO 2
# Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en una carpeta comprimida zip.
print("\n")
import math
print("EJERCICIO 2 - VIDEO 3")
supeso = float(input('Por favor ingrese su peso en kilogramos:  '))
suestatura = float(input('Por favor ingrese su estatura (en metros): '))

imc = round(supeso/suestatura**2,2)
print('Su índice de masa corporal es '+str(imc))