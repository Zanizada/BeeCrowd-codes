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
                media = soma/(float)divisor;
                printf("media = %.2lf\n");
                break;
            }
        }
    }

    return 0;
}
