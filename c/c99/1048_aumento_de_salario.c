#include <stdio.h>

int main() {
    float salario, reajuste, ganho;
    int porcentagem;
    scanf("%f", &salario);
    if (0 <= salario && salario <= 400.00) {
        reajuste = salario * 1.15;
        porcentagem = 15;
        ganho = reajuste - salario;
    } else if (400.01 <= salario && salario <= 800.00) {
        reajuste = salario * 1.12;
        porcentagem = 12;
        ganho = reajuste - salario;
    } else if (800.01 <= salario && salario <= 1200.00) {
        reajuste = salario * 1.10;
        porcentagem = 10;
        ganho = reajuste - salario;
    } else if (1200.01 <= salario && salario <= 2000.00) {
        reajuste = salario * 1.07;
        porcentagem = 7;
        ganho = reajuste - salario;
    } else {
        reajuste = salario * 1.04;
        porcentagem = 4;
        ganho = reajuste - salario;
    }
    printf("Novo salario: %.2f\n", reajuste);
    printf("Reajuste ganho: %.2f\n", ganho);
    printf("Em percentual: %d %%\n", porcentagem);

    return 0;
}
