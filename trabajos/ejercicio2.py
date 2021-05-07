#datos de dentrada
dinero=float(input("ingrese la cantidad:"))
#proceso
if dinero<=10.00:
  print("puedes regalar una tarjeta")
elif dinero>=11.00 and dinero<=100.00:
  print("puedes comprar unos chocolates")
elif dinero>=101.00 and dinero<=250.00:
  print("puedes comprar una flor")
elif dinero>=251.00:
  print("puedes comprar un anillo")
