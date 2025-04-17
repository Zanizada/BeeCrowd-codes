#include <stdio.h>

int main() {
    int A, B, C, D, PA, PB, diff;
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);
    scanf("%d", &D);
    PA = A * B;
    PB = C * D;
    diff = PA - PB;
    printf("DIFERENCA = %d\n" diff);
    return 0;
}
