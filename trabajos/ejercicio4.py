#datos de dentrada
salud=int(input("ingrese tipo de vacuna:"))
#proceso
if salud>=70:
  print("aplicar la tipo c")
elif salud>=16 and salud<=69:
  print("aplica la tipo b")
elif salud<=16:
  print("aplica la tipo a")
