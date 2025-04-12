import java.util.Scanner;

public class media_1_1005 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double A = sc.nextDouble();
        double B = sc.nextDouble();
        double PA = 3.5;
        double PB = 7.5;
        double soma = (A * PA) + (B * PB);
        double media = soma / (PA + PB);
        
        System.out.printf("MEDIA = %.5f%n", media);

        sc.close();
    }
}