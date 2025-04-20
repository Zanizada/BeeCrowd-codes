#include <stdio.h>

int main() {
    int positivos = 0;
    float N;
    for (int i = 1; i <= 6; i++) {
        scanf("%f", &N);
        if (N > 0) {
            positivos++;
        }
    }
    printf("%d valores positivos\n", positivos);
    return 0;
}
