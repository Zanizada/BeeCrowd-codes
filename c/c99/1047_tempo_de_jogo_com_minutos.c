#include <stdio.h>

int main() {
    int h_inicio, h_fim, m_inicio, m_fim, duracao;
    scanf("%d %d %d %d", &h_inicio, &m_inicio, &h_fim, &m_fim);
    if (h_inicio < h_fim) {
        duracao = fim - inicio;
    } else {
        duracao = (24 - inicio) + fim;
    }
    printf("O JOGO DUROU %d HORA(S)\n", duracao);

    return 0;
}
