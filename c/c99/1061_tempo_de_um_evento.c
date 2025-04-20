#include <stdio.h>

int main() {
    int diaInicio, h1, m1, s1;
    int diaFim, h2, m2, s2;

    scanf("Dia %d", &diaInicio);
    scanf("%d : %d : %d", &h1, &m1, &s1);
    scanf("Dia %d", &diaFim);
    scanf("%d : %d : %d", &h2, &m2, &s2);

    int inicioSeg = s1 + m1 * 60 + h1 * 3600 + diaInicio * 86400;
    int fimSeg = s2 + m2 * 60 + h2 * 3600 + diaFim * 86400;

    int duracao = fimSeg - inicioSeg;

    int dias = duracao / 86400;
    duracao %= 86400;
    int horas = duracao / 3600;
    duracao %= 3600;
    int minutos = duracao / 60;
    int segundos = duracao % 60;

    printf("%d dia(s)\n", dias);
    printf("%d hora(s)\n", horas);
    printf("%d minuto(s)\n", minutos);
    printf("%d segundo(s)\n", segundos);

    return 0;
}
