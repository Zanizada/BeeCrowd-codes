#include <stdio.h>
#include <math.h>
int main() {
    double R, pi = 3.14159, V;
    scanf("%lf", &R);
    V = (4.0/3) * pi * pow(R, 3);
    printf("VOLUME = %.3lf", V);
    return 0;
}
