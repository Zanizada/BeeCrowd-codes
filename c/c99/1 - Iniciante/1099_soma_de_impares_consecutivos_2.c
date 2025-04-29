#include <stdio.h>

int main() {
    int N, X, Y;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d %d", &X, &Y);

        int soma = 0;

        if (X > Y) {
            int temp = X;
            X = Y;
            Y = temp;
        }

        for (int j = X + 1; j < Y; j++) {
            if (j % 2 != 0) {
                soma += j;
            }
        }

        printf("%d\n", soma);
    }

    return 0;
}
