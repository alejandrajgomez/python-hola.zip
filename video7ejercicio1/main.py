from modulin import calculadora


print( "Mi modulo calculadora se ejecutará  a continuacion:")

def main():
  suma = calculadora.suma(5,4)
  print("Esta es mi suma:",suma)

  resta = calculadora.resta(15,4)
  print("Esta es mi resta:",resta)

  multiplicacion = calculadora.multi(5,4)
  print("Esta es mi multiplicacion:",multiplicacion)

  division = calculadora.divi(20,4)
  print("Esta es mi division:",division)




if __name__ == '__main__':
    main()
