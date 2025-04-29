#include <stdio.h>
#include <math.h>

int main() {
    int N, multi;
    scanf("%d", &N);

    for (int i = 1; i <= N; i++) {
        if (i % 2 == 0) {
            multi = i * i;
            printf("%d^2 = %d\n", i, multi);
        }
    }
}
