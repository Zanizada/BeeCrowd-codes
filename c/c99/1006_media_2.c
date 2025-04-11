#include <stdio.h>
int main() {
    double A, B, C, PA = 2, PB = 3, PC = 5, soma, media;
    scanf("%lf", &A);
    scanf("%lf", &B);
    scanf("%lf", &C);
    soma = (A * PA) + (B * PB) + (C * PC);
    media = soma/(PA + PB + PC);
    printf("MEDIA = %.1lf\n", media);
    return 0;
}
