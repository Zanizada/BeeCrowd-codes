#include <stdio.h>

int main() {
    float A, B, C;
    scanf("%f %f %f", &A, &B, &C);
    if (A < B + C && B < A + C && C < A + B) {
        float perimetro;
        perimetro = A + B + C;
        printf("Perimetro = %.1f\n", perimetro);
    } else {
        float area;
        area = ((A + B) * C) / 2;
        printf("Area = %.1f\n", area);
    }
    return 0;
}
