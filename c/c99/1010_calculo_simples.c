#include <stdio.h>
int main() {
    int P1, N1, P2, N2;
    float V1, V2, T1, T2, VT;
    scanf("%d %d %f", &P1, &N1, &V1);
    scanf("%d %d %f", &P2, &N2, &V2);
    T1 = N1 * V1;
    T2 = N2 * V2;
    VT = T1 + T2;
    printf("VALOR A PAGAR: R$ %.2f\n", VT);
    return 0;
}
