# VIDEO 9 EJERCICIO 2

# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

numeros = [21,30,15,22,45,57,48]

resultado = list(filter(lambda x: x % 2 != 0, numeros))

print(resultado)
print(type(resultado))

def suma(a,b):
      return a + b

print(reduce(suma,resultado))
