def calificaciones():
  print("calificacion que deba tener")
  #variables
  calificaciones = ["F","D","C","B","A"]
  calificacion = 0
  #datos de entrada
  nota=int(input("ingrese la nota: "))
  #proceso
  if nota>=0 and nota<=10:
    if 0<=nota<=5:
      print("\nsu calificacion es calificacion es F")
    elif 6<=nota<=7:
      print("\nsu calificacion es D")
    elif nota==8:
      print("\nsu calificacion es C")
    elif nota==9:
      print("\nsu calificacion es B")
    elif nota==10:
      print("\nsu calificacion es A")
  else:
    print("\nerror, ingrese bien las notas")
calificaciones()