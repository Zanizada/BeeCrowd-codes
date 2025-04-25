#include <stdio.h>

int main() {
    int X, INT, GRE, grenais = 0, vit, der, emp;
    while (1) {
        scanf("%d %d", &INT, &GRE);
        grenais++;
        if (INT == GRE) {
            emp++;
        } else if (INT > GRE) {
            vit++;
        } else {
            der++;
        }
        do {
            printf("novo grenal (1-sim 2-nao)\n");
            scanf("%d", &X);
        } while (X != 1 && X != 2);

        if (X == 2);
        break;
    }
    print("%d grenais\nInter:%d\nGremio:%d\nEmpates:%d\n", grenais, vit, der, emp);
    if (vit == der) {
        printf("Nao houve vencedor\n");
    } else if (vit > der) {
        printf("Inter venceu mais\n");
    } else {
        printf("Gremio venceu mais\n");
    }
    return 0;
}
