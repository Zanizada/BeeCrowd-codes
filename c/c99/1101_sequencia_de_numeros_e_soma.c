#include <stdio.h>

int main() {
    int M, N, ordem, soma;
    while (M > 0 && N > 0) {
        scanf("%d %d", &M, &N);

        if (M <= 0 || N <= 0) {
            break;
        }

        if (M > N) {
            int temp = M;
            M = N;
            N = temp;
        }

        for (int i = M; i < N + 1; i++) {
            ordem[N] = i;
            soma += i
        }
    }
    return 0;
}
