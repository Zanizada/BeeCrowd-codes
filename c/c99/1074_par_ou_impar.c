#include <stdio.h>

int main() {
    int N, A;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &A);
        if (A == 0) {
            printf("NULL\n");
        }
        if (A % 2 == 0) {
            if (A > 0) printf("EVEN POSITIVE\n");
            else if (A < 0) printf("EVEN NEGATIVE\n");

        } else {
            if (A > 0) printf("ODD POSITIVE\n");
            else if (A < 0) printf("ODD NEGATIVE\n");
        }
    }

    return 0;
}
