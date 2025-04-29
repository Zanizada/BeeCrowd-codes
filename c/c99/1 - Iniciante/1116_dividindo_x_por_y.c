#include <stdio.h>

int main() {
    int N, X, Y;
    float div;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d %d", &X, &Y);

        if (Y == 0) {
            printf("divisao impossivel\n");
        } else {
            div = (float)X / Y;
            printf("%.1f\n", div);
        }
    }

    return 0;
}
