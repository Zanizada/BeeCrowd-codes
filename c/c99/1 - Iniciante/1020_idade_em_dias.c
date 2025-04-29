#include <stdio.h>

int main() {
    int N, dias, meses, anos;
    scanf("%d", &N);
    anos = N / 365;
    N = N % 365;
    meses = N / 30;
    dias = N % 30;
    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", anos, meses, dias);
    return 0;
}
