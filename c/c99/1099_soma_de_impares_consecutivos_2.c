#include <stdio.h>

int main() {
    int temp, soma, N, X, Y, i;
    scanf("%d", &N);
    for (i == 0; i < N; i++) {
        scanf("%d %d", &X, &Y);

        if (X > Y) {
            temp = X;
            X = Y;
            Y = temp;

            for (i = X + 1; i < Y; i++) {
                if (i % 2 != 0) {
                    soma += i
                }
            }
        }
        printf("%d\n", soma);
    }

    return 0;
}
