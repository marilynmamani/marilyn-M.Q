import pe.edu.upeu.OperacionesMat;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        OperacionesMat OM=new OperacionesMat ();
        OM.operacionesBasicas();
        

    }

    long ti=System.currentTimeMillis();
    System.out.println("Fibonacci iterativo:"+objSP.fibonacci(numero));
    long tf=System.currentTimeMillis();
    System.out.println("Tiempo ejecucion:"+(tf-ti));
    ti=System.currentTimeMillis();
    System.out.println("Fibonacci recursivo:"+objSP.fibonacciRecur(numero));
    tf=System.currentTimeMillis();
    System.out.println("Tiempo ejecucion:"+(tf-ti));
 }


