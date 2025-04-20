#include <stdio.h>

int main() {
    int dia_inicio, dia_fim;
    int h1, m1, s1, h2, m2, s2;
    int total_inicio, total_fim, duracao;
    int dias, horas, minutos, segundos;

    scanf("Dia %d", &dia_inicio);
    scanf("%d : %d : %d", &h1, &m1, &s1);

    scanf(" Dia %d", &dia_fim);
    scanf("%d : %d : %d", &h2, &m2, &s2);

    total_inicio = s1 + m1 * 60 + h1 * 3600 + dia_inicio * 86400;
    total_fim = s2 + m2 * 60 + h2 * 3600 + dia_fim * 86400;

    duracao = total_fim - total_inicio;

    dias = duracao / 86400;
    duracao %= 86400;
    horas = duracao / 3600;
    duracao %= 3600;
    minutos = duracao / 60;
    segundos = duracao % 60;

    printf("%d dia(s)\n", dias);
    printf("%d hora(s)\n", horas);
    printf("%d minuto(s)\n", minutos);
    printf("%d segundo(s)\n", segundos);

    return 0;
}
