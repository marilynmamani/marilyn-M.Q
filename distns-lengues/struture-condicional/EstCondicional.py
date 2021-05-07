def estCondicional01():
 #Definir variables
 print("Ejemplo estructura Condicional en Python")
 montoP=0
 #Datos de entrada
 cantidadX=int(input("Ingrese la cantidad de lapices:"))
 #Proceso
 if cantidadX>=1000:
 montoP=cantidadX*0.80
 else:
 montoP=cantidadX*0.90
 #Datos de salida
 print("El monto a pagar es:", montoP)
estCondicional01()
def  postulanteCarreraEstMultiple ():
  #Definir Variables
  notaFinal = 0.0
  #Datos de Entrada
  areaCarreraNcomp = input ( "Ingrese el area a la que pertenece su carrera \ n B = Biomedicas \ n I = Ingenieria \ n S = Sociales:" )
  notaEP = float ( input ( "Ingrese la nota de EP:" ))
  notaRM = float ( input ( "Ingrese la nota de RM:" ))
  notaRV = float ( input ( "Ingrese la nota de RV:" ))
  notaAB = float ( input ( "Ingrese la nota de AB:" ))
  #Proceso
  si  areaCarreraNcomp == "B" :
    notaFinal = ( notaEP * 0.40 ) + ( notaRM * 0.10 ) + ( notaRV * 0.20 ) + ( notaAB * 0.30 )
    areaCarreraNcomp = "Biomedicas"
  elif  areaCarreraNcomp == "I" :
    notaFinal = ( notaEP * 0.40 ) + ( notaRM * 0.30 ) + ( notaRV * 0.15 ) + ( notaAB * 0.15 )
    areaCarreraNcomp = "Ingenierias"  
  elif  areaCarreraNcomp == "S" :
    notaFinal = ( notaEP * 0.40 ) + ( notaRM * 0.10 ) + ( notaRV * 0.30 ) + ( notaAB * 0.20 );
    areaCarreraNcomp = "Sociales" ;
  otra cosa :
    print ( "La opcion que ingreso no existe! intente nuevamente ...." )
  #Datos de Salida
  print ( "La persona obtuvo una nota de:" , notaFinal , "y su carrera es del area:" , areaCarreraNcomp)