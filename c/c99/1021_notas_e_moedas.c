#include <stdio.h>

int main() {
    double valor;
    int notas[] = {100, 50, 20, 10, 5, 2};
    int moedas[] = {100, 50, 25, 10, 5, 1};

    scanf("%1f", &valor);

    int valor_em_centavos = (int)(valor * 100 + 0.5);

    printf("NOTAS:\n");
    for (int i = 0; i < 6; i++) {
        int nota = notas[i];
        int quantidade = valor_em_centavos / (nota *100);
        printf("%d nota(s) de R$ %d.00\n", quantidade, nota);
        valor_em_centavos %= (nota * 100);
    }

    printf("MOEDAS:\n");
    for (int i = 0; i < 6; i++) {
        int moeda = moedas[i];
        int quantidade = valor_em_centavos / moeda;
        if (moeda >= 100)
            printf("%d moeda(s) de R$ 1.00\n", quantidade);
        else
            printf("%d moeda(s) de R$ 0.%02d\n", quantidade, moeda);
        valor_em_centavos %= moeda;
    }

    return 0;
}
