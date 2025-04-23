#include <stdio.h>

int main() {
    int N, quantia, total = 0, coelhos = 0, ratos = 0, sapos = 0, percentual_c = 0, percentual_r = 0, percentual_s = 0;
    char tipo[50];
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d %s", &quantia, &tipo[50]);
        total += quantia;
        if (tipo[50] == "C") {
            coelhos += quantia;
        } else if (tipo[50] == "R") {
            ratos += quantia;
        } else if (tipo[50] == "S") {
            sapos += quantia;
        }
    }

    return 0;
}
