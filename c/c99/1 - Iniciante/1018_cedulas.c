#include <stdio.h>

int main() {
    int valor, nota;
    int notas[] = {100, 50, 20, 10, 5, 2, 1};
    scanf("%d", &valor);
    printf("%d\n", valor);  // valor original
    for (int i = 0; i < 7; i++) {
        nota = valor / notas[i];
        printf("%d nota(s) de R$ %d,00\n", nota, notas[i]);
        valor = valor % notas[i];
    }
    return 0;
}
