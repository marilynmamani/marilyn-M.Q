def nombre_y_edad():
  print("nombre y edad de la persona menor")
  #datos de entrada
  julio=int(input("ingrese la edad que tiene julio: "))
  arturo=int(input("ingrese la edad que tiene arturo: "))
  pamela=int(input("ingrese la edad que tiene pamela: "))
  #proceso y fin
  if 0<julio<150 and 0<arturo<150 and 0<pamela<150:
    print("\neres genial lo resolviste que")
    if julio<arturo and julio<pamela:
      print(f"el menor es jose y tiene {julio} año(s)")
   
    elif arturo<julio and arturo<pamela:
      print(f"el menor es arturo y tiene {arturo} año(s)")
    elif pamela<julio and pamela<arturo:
      print(f"el menor es pamela y tiene {pamela} año(s)")
    elif julio==arturo and julio==pamela and arturo==pamela:
      print("los tres son de la misma edad")
  else:
     print("\nehhh ingresa bien todos sus datos deve de ser verdaderas")
nombre_y_edad()