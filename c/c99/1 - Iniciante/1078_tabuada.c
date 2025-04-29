#include <stdio.h>

int main() {
    int N, multiplo = 1, tabuada;
    scanf("%d", &N);

    for (int i = 0; i < 10; i++) {
        tabuada = multiplo * N;
        printf("%d x %d = %d\n", multiplo, N, tabuada);
        multiplo++;
    }

    return 0;
}
