#include <stdio.h>

int main() {
    int h_inicio, m_inicio, h_final, m_final, horas, minutos;
    scanf("%d %d %d %d", &h_inicio, &m_inicio, &h_final, &m_final);

    if ((h_inicio < h_final) || (h_inicio == h_final && m_inicio < m_final)) {
        horas = h_final - h_inicio;
        minutos = m_final - m_inicio;
    } else if (h_inicio == h_final && m_inicio == m_final) {
        horas = 24;
        minutos = 0;
    } else {
        horas = (24 - h_inicio) + h_final;
        minutos = m_final - m_inicio;
    }
    if (minutos < 0) {
        minutos += 60;
        horas--;
    }
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", horas, minutos);

    return 0;
}
