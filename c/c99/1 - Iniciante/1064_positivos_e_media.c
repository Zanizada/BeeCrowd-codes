#include <stdio.h>

int main() {
    float a, b, c, d, e, f;
    float soma = 0, media;
    int contador = 0;

    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);
    scanf("%f", &d);
    scanf("%f", &e);
    scanf("%f", &f);

    float N[6] = {a, b, c, d, e, f};

    for (int i = 0; i < 6; i++) {
        if (N[i] > 0) {
            contador++;
            soma += N[i];
        }
    }

    media = soma/contador;

    printf("%d valores positivos\n", contador);
    printf("%.1f\n", media);

    return 0;
}
