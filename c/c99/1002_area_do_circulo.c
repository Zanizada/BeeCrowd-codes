#include <stdio.h>
#include <math.h>

int main() {
    float raio, area, n = 3.14159;

    scanf("%f", &raio);
    area = n * pow(raio, 2);

    printf("A=%.4f\n", area);

    return 0;
}
