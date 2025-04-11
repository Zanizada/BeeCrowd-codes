#include <stdio.h>
int main() {
    double A, B, PA = 3.5, PB = 7.5, soma, media;
    scanf("%lf", &A);
    scanf("%lf", &B);
    soma = (A * PA) + (B * PB);
    media = soma/(PA + PB);
    printf("MEDIA = %.5lf\n", media);
    return 0;
}
