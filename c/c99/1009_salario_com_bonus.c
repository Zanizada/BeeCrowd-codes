#include <stdio.h>
int main() {
    char nome[100];
    double S, V, C, total;
    scanf("%s", &nome);
    scanf("%lf", &S);
    scanf("%lf", &V);
    C = V * 0.15;
    total = S + C;
    printf("TOTAL = R$ %.2lf\n", total);
    return 0;
}
