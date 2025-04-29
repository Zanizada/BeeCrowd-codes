#include <stdio.h>

int main() {
    int N, horas, minutos, segundos;
    scanf("%d", &N);
    horas = N / 3600;
    N = N % 3600;
    minutos = N / 60;
    segundos = N % 60;
    printf("%d:%d:%d\n", horas, minutos, segundos);
    return 0;
}
