#include <stdio.h>

int main() {
    double N, soma = 0, media;
    int divisor = 0;

    while (1) {
        scanf("%lf", &N);

        if (0 > N || N > 10) {
            printf("nota invalida\n");
        } else {
            divisor++;
            soma += N;

            if (divisor == 2) {
                media = soma / divisor;
                printf("media = %.2lf\n", media);
            }
            int X;
            scanf("novo calculo (1-sim 2-nao)%d", &X);
            if (X < 1 || X > 2) {
                scanf("novo calculo (1-sim 2-nao)%d", &X);
            } else {
                if (X == 2) {
                    break;
                } else {
                    scanf("%lf", &N);
                    divisor = 0;
                    soma = 0;

                    if (0 > N || N > 10) {
                        printf("nota invalida\n");
                    } else {
                        divisor++;
                        soma += N;

                        if (divisor == 2) {
                            media = soma / divisor;
                            printf("media = %.2lf\n", media);
                }
            }
        }
    }
    return 0;
}
