import java.util.Scanner;

public class soma_simples_1003 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        
        int SOMA = A + B;

        System.out.printf("SOMA = %d%n", SOMA);

        sc.close();
    }
}