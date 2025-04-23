#include <stdio.h>

int main() {
    int N, quantia, coelhos = 0, ratos = 0, sapos = 0;
    float total = 0.0, percentual_c = 0.0, percentual_r = 0.0, percentual_s = 0.0;
    char tipo;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d %s", &quantia, &tipo);
        total += quantia;
        if (tipo = "C") {
            coelhos += quantia;
        } else if (tipo = "R") {
            ratos += quantia;
        } else if (tipo = "S") {
            sapos += quantia;
        }
    }

    percentual_c = (coelhos*100)/total;
    percentual_r = (ratos*100)/total;
    percentual_s = (sapos*100)/total;

    printf("Total: %d cobaias\nTotal de coelhos: %d\nTotal de ratos: %d\nTotal de sapos: %d\nPercentual de coelhos: %.2f %%\nPercentual de ratos: %.2f %%\nPercentual de sapos: %.2f %%\n", total, coelhos, ratos, sapos, percentual_c, percentual_r, percentual_s);

    return 0;
}
