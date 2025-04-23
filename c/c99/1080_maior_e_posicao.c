#include <stdio.h>

int main() {
    int i, numeros[100];
    for (i = 0; i < 100; i++) {
        scanf("%d", &numeros[i]);
    }
    int maior = numeros[0], menor = numeros[0];

    for (i = 1; i < 100; i++) {
        if (numeros[i] > maior) {
            maior = numeros[i];
        }
        if (numeros[i] < menor) {
            menor = numeros[i];
        }
    }

    printf("%d\n", maior);
    printf("%d\n", menor);

    return 0;
}
