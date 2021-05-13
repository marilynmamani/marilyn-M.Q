opcion=0
def Ejercicio5MMQ():
  opc=int(input("Menu principal \n"
  "1.promedio de notas \n"
  "2.bono \n"
  "3.tipos de vacunas \n"
  "4.operaciones de aritmeticas \n"
  "5.finish \n"
  "escoja una opcion: \n"))
  return opc

def Ejercicio1MMQ():
 # datos de entrada
 Nfinal=0.0
 punidad=float(input("Ingrese nota de primera unidad: "))
 sunidad=float(input("Ingrese nota de segunda unidad: "))
 tunidad=float(input("Ingrese nota de tercera unidad: "))
 tfinal=float(input("Ingrese la nota final del trabajo: "))
 # Proceso
 if punidad>0:
   Nfinal=(punidad*0.20)+(sunidad*0.15)+(tunidad*0.15)+(tfinal*0.50)
 # Datos de salida
 print(f"Nota final:{Nfinal:.1f} ")

def Ejercicio2MMQ():
  # Datos de entrada
  sueldo=930
  bono=0
  puntos=int(input("Ingrese la puntuacion y bono optenido: "))
  # Proceso
  if puntos>=50 and puntos<=100:
    bono=sueldo*0.10
  elif puntos>100 and puntos<=150:
    bono=sueldo*0.40
  elif puntos>150:
    bono=sueldo*0.70
  # Datos de salida
  print("le corresponde el bono de:", bono)

def Ejercicio3MMQ():
  # Datos de entrada
  edad=0
  edad=int(input("Ingrese su edad: "))
  sexo=input("Ingrese su sexo correspondiente \n" 
  "h:hombre. \n" 
  "m:mujer. \n")
  # Proceso
  if edad>=70:
   print("aplica la vacuna tipo C.")
  elif edad>=16 and edad<70 and sexo=="m":
   print("aplica la vacuna tipo B.")
  elif edad>=16 and edad<70 and sexo=="h":
   print("aplica la vacuna tipo A.")
  elif edad<16:
   print("aplica la vacuna tipo A.")

def Ejercicio4MMQ():
  print("operaciones aritmeticas.")
  a=0
  b=0
  a=int(input("Ingrese el primer valor: "))
  b=int(input("Ingrese el segundo valor: "))
  # Proceso
  print("Suma:  \n ", a+b)
  print("Resta:\n", a-b)
  print("Division: \n", a/b)
  print("Multiplicacion \n", a*b)
  print("Potenciacion \n", a**b)

while opcion !=5:
  opcion = Ejercicio5MMQ()
  if opcion == 1:
    Ejercicio1MMQ()
  if opcion == 2:
    Ejercicio2MMQ()
  if opcion == 3:
    Ejjercicio3MMQ()
  if opcion == 4:
    Ejercicio4MMQ()
  if opcion == 5:
    print("Programa culminado:")