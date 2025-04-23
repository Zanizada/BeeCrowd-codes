#include <stdio.h>

int main() {
    int X, Y, soma = 0;

    scanf("%d", &X);
    scanf("%d", &Y);

    if (X > Y) {
        int temp = X;
        X = Y;
        Y = temp;
    }

    for (int i = X + 1; i < Y; i++) {
        if (i % 2 != 0) {
            soma += i;
        }
    }

    printf("%d\n", soma);

    return 0;
}
