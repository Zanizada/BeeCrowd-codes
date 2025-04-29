#include <stdio.h>

void quadrante(int A, int B) {
    if (A > 0 && B > 0) {
        printf("primeiro\n");
    } else if (A < 0 && B > 0) {
        printf("segundo\n");
    } else if (A < 0 && B < 0) {
        printf("terceiro\n");
    } else {
        printf("quarto\n");
    }
}

int main() {
    int X, Y;

    while (1) {
        scanf("%d %d", &X, &Y);

        if (X == 0 || Y == 0) {
            break;
        } else {
            quadrante(X, Y);
        }
    }

    return 0;
}
