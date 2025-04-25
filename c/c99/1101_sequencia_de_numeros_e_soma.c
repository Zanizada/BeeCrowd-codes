#include <stdio.h>

int main() {
    int M, N;

    while (1) {
        scanf("%d %d", &M, &N);

        if (M <= 0 || N <= 0) {
            break;
        }

        int soma = 0;

        if (M > N) {
            int temp = M;
            M = N;
            N = temp;
        }

        for (int i = M; i <= N; i++) {
            printf("%d ", i);
            soma += i;
        }
        printf("Sum=%d\n", soma);
    }

    return 0;
}
