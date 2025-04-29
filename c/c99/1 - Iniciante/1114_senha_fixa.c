#include <stdio.h>

int verificar_senha(int senha) {
    if (senha == 2002) {
        printf("Acesso Permitido\n");
        return 1;  // senha correta
    } else {
        printf("Senha Invalida\n");
        return 0;  // senha incorreta
    }
}

int main() {
    int N;

    while (1) {
        scanf("%d", &N);  // use o & para passar o endereço da variável
        if (verificar_senha(N)) {
            break;
        }
    }

    return 0;
}
