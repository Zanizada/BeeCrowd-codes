#include <stdio.h>

int main() {
    double N, soma, media;
    int divisor, X;

    while (1) {
        soma = 0;
        divisor = 0;

        while (divisor < 2) {
            scanf("%lf", &N);

            if (N < 0 || N > 10) {
                printf("nota invalida\n");
            } else {
                soma += N;
                divisor++;
            }
        }

        media = soma / divisor;
        printf("media = %.2lf\n", media);

        do {
            printf("novo calculo (1-sim 2-nao)\n");
            scanf("%d", &X);
        } while (X != 1 && X != 2);

        if (X == 2) {
            break;
        }
    }

    return 0;
}
