# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

f = open('nombresfemeninos.txt','w')

lista = ['Peponia\n',
         'Manila\n',
         'Roselda\n'
       ]

f.writelines(lista)
f.close()
print(lista)


f = open('nombresfemeninos.txt','a')
f.write('Esta es la segunda apertura del archivo, y le agrego nombres:\n')
f.write('Rosa\n')
f.write('Juana\n')
f.write('Mercedes\n')
f.close()

f = open('nombresfemeninos.txt')
print(f.read())
