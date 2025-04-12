#include <stdio.h>
#include <math.h>
int main() {
    double A, B, C, pi = 3.14159, a, b, c, d, e;
    scanf("%lf %lf %lf", &A, &B, &C);
    a = (A * C) / 2;
    b = pi * pow(C, 2);
    c = ((A + B) * C) / 2;
    d = pow(B, 2);
    e = A * B;
    printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\nQUADRADO: %.3lf\nRETANGULO: %.3lf\n", a, b, c, d, e);
    return 0;
}
