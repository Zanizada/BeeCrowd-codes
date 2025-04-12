import java.util.Scanner;

public class media_2_1006 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double A = sc.nextDouble();
        double B = sc.nextDouble();
        double C = sc.nextDouble();
        double PA = 2;
        double PB = 3;
        double PC = 5;
        double soma = (A * PA) + (B * PB) + (C * PC);
        double media = soma / (PA + PB + PC);
        
        System.out.printf("MEDIA = %.1f%n", media);

        sc.close();
    }
}