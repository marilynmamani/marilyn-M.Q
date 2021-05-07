def votoElecciones():
  print("Como saber si puedes votar por tu edad")
  mensaje =""
  edadP=int(input("ingrese la edad que tiene:"))
  if edadP>=18:
    mensaje ="Usted esta apto para votar"
  else:
    mensaje ="Usted no cumple con la edadad minima y no esta apto para votar"
  print(mensaje)
votoElecciones()