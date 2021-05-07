#datos de entrada
edad=int(input("ingrese su edad: "))
nota=float(input("ingrese su promedio: "))
#proceso
if edad>18 and nota>=9:
  print("usted es acreedor de 2000")
elif edad>=18 and nota>=7.5:
  print("usted es acreedor de 1000")

elif edad>18 and nota<7.5 and nota>=6.0:
  print("usted es acreedor de 500")
elif nota<6.0:
  print("se le invita a participar al proximo ciclo escolar y seguir estudiando")
elif edad<=18 and nota>=9:
  print("usted es acreedor de 3000")
elif edad<=18 and nota<9 and nota>=8:
  print("usted es acreedor de 2000")
elif edad<=18 and nota<8 and nota>=6:
  print("usted es acreedor de 100")
