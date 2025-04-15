#include <stdio.h>

int main() {
    int N, Q;
    float preco;
    scanf("%d", &N);
    scanf("%d", &Q);
    if N == 1 {
        preco = Q * 4.00;
        printf("Total: R$%.2f\n", preco);
    }
    else if N == 2 {
        preco = Q * 4.50;
        printf("Total: R$%.2f\n", preco);
    }
    else if N == 3 {
        preco = Q * 5.00;
        printf("Total: R$%.2f\n", preco);
    }
    else if N == 4 {
        preco = Q * 2.00;
        printf("Total: R$%.2f\n", preco);
    }
    else if N == 5 {
        preco = Q * 1.50;
        printf("Total: R$%.2f\n", preco);
    }
    return 0;
}
