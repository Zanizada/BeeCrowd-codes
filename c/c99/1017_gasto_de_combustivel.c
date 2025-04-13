#include <stdio.h>
int main() {
    int x, y, distancia;
    float total;
    scanf("%d", &x);
    scanf("%d", &y);
    distancia = x * y;
    total = distancia / 12.0;
    printf("%.3f\n", total);
    return 0;
}
