import  java.util.Scanner ;

/ **
 * StrRepetitive
 * /
public  class  StrRepetitive {

     escáner estático teclado = nuevo  escáner ( System . in);
    

     saludo público vacío estático  () { 
        Sistema . fuera . println ( " Hola como estas? " );
    }
    public  static  void  name5 () {
        Sistema . fuera . println ( " Probando " );
    }

    public  static  void  suma10NumerosMientras () {
      // definir variables
        int contador = 0 ;
        numeros dobles , sumaNumeros = 0 ;
        // Datos de Entrada y proceso
        while (contador < 10 ) {   // ++ contador contador ++
            ++ contador;
            Sistema . fuera . println ( " Ingrese el valor de la posición " + contador + " : " );
            numeros = teclado . nextDouble ();
            sumaNumeros = sumaNumeros + numeros;            
        }
        // Datos de salida
        Sistema . fuera . println ( " La suma de los 10 números es: " + sumaNumeros);        
    }

    public  static  void  suma10NumerosHacerMientras () {
        // definir variables
          int contador = 0 ;
          numeros dobles , sumaNumeros = 0 ;
          // Datos de Entrada y proceso
         do {   // ++ contador: primero incrementa el valor contador ++: imprime el valor luego incrementa
              ++ contador;
              Sistema . fuera . println ( " Ingrese el valor de la posición " + (contador) + " : " );
              numeros = teclado . nextDouble ();
              sumaNumeros = sumaNumeros + numeros;
              
          } while (contador < 10 );
          // Datos de salida
          Sistema . fuera . println ( " La suma de los 10 números es: " + sumaNumeros);        
      }    
        
      public  static  void  suma10NumerosParaHasta () {
        // definir variables
          numeros dobles , sumaNumeros = 0 ;
          // Datos de Entrada y proceso
          para ( int contador = 1 ; contador <= 10 ; contador ++ ) {
              Sistema . fuera . println ( " Ingrese el valor de la posición " + contador + " : " );
              numeros = teclado . nextDouble ();
              sumaNumeros = sumaNumeros + numeros;              
          }
          // Datos de salida
          Sistema . fuera . println ( " La suma de los 10 números es: " + sumaNumeros);        
      } 

    public  static  void  menuMain () {
        String mensaje = " Seleccion el algoritmo que desea ejecutar: " +
        " \ n 1 = suma10NumerosMientras " +
        " \ n 2 = suma10NumerosHacerMientras " +
        " \ n 3 = suma10NumerosPara " +
        " \ n 4 = numerosParesHasta100 " +
        " \ n 5 = numerosFibonaci " +
        " \ n 0 = Salir del programa " ;

        Sistema . fuera . println (mensaje);
        int opcion = 0 ;
        hacer {
            opcion = teclado . nextInt ();
            cambiar (opcion) {
                caso  1 : suma10NumerosMientras (); romper ;
                caso  2 : suma10NumerosHacerMientras (); romper ;
                caso  3 : suma10NumerosParaHasta (); romper ;
                caso  4 : numerosParesHasta100 (); romper ;
                caso  5 : numeroFibonaci (); romper ;
            }
            si (opcion ! = 0 )
            Sistema . fuera . println ( " \ n Desea seguir probando: " + mensaje);
            
        } while (opcion ! = 0 );        
    }

     numerosParesHasta100 público estático  vacío  () {
      para ( int contador = 0 ; contador < 100 ; contador ++ ) {
        si (contador % 2 == 0 ) {
          Sistema . fuera . println ( " El numero " + contador + " es numero par " );
        }
      }
    }

    public  static  void  numeroFibonaci () {
      int numAnt = 0 ;
      int numNue = 1 ;
      int numTem = 0 ;
      int contador = 1 ;
      Sistema . fuera . println ( " Numero Fibonaci " );
      int numFinal = teclado . nextInt ();
      while (contador < numFinal) {
        numTem = numNue;
        numNue = numAnt + numNue;
        numAnt = numTem;     
        contador ++ ;
        // System.out.println ("El numero Fibonci es:" + numNue);
      }
      Sistema . fuera . println ( " Numero fibonaci de " + numFinal + " es: " + numNue);
    }


    public  static  void  main ( String [] args ) {
    menuMain ();
    }


}

