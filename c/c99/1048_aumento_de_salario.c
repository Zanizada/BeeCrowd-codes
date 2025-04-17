#include <stdio.h>

int main() {
    float salario, reajuste, ganho;
    int porcentagem;
    if (0 <= salario && salario <= 400.00) {
        reajuste = salario * 1.15;
        porcentagem = 15;
        ganho = salario - reajuste;
    } else if (400.01 <= salario && salario <= 800.00) {
        reajuste = salario * 1.12;
        porcentagem = 12;
        ganho = salario - reajuste;
    } else if (800.01 <= salario && salario <= 1200.00) {
        reajuste = salario * 1.10;
        porcentagem = 10;
        ganho = salario - reajuste;
    } else if (1200.01 <= salario && salario <= 2000.00) {
        reajuste = salario * 1.07;
        porcentagem = 7;
        ganho = salario - reajuste;
    } else {
        reajuste = salario * 1.04;
        porcentagem = 4;
        ganho = salario - reajuste;
    }
    printf("Novo Salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %\n", reajuste, ganho, porcentagem);

    return 0;
}
