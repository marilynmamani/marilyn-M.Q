#datos de dentrada
puntuacion=int(input("ingrese puntos"))
#proceso
if puntuacion>=0 and puntuacion<=100:
  print("tiene mas un salario")
elif puntuacion>=101 and puntuacion<=150:
  print("tiene mas dos salarios")
elif puntuacion>=151:
  print("tiene mas tres salarios")