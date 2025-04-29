import java.util.Scanner;

public class produto_simples_1004 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        
        int PROD = A * B;

        System.out.printf("PROD = %d%n", PROD);

        sc.close();
    }
}