#include <stdio.h>

int main() {
    int X, INT, GRE, grenais = 0, vit = 0, der = 0, emp = 0;
    while (1) {
        scanf("%d %d", &INT, &GRE);
        grenais++;
        if (INT == GRE) {
            emp++;
        } else if (INT > GRE) {
            vit++;
        } else if (INT < GRE) {
            der++;
        }

        do {
            printf("novo grenal (1-sim 2-nao)\n");
            scanf("%d", &X);
        } while (X != 1 && X != 2);

        if (X == 2) {
        break;
        }
    }
    printf("%d grenais\n", grenais);
    printf("Inter:%d\n", vit);
    printf("Gremio:%d\n", der);
    printf("Empates:%d\n", emp);

    if (vit == der) {
        printf("Nao houve vencedor\n");
    } else if (vit > der) {
        printf("Inter venceu mais\n");
    } else if (vit < der) {
        printf("Gremio venceu mais\n");
    }
    return 0;
}
