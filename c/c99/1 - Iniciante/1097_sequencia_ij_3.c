#include <stdio.h>

int main() {
    int I = 1, J = 7, contador = 0;

    while (I <= 9) {
        printf("I=%d J=%d\n", I, J);
        J -= 1;
        contador += 1;

        if (contador == 3) {
            I += 2;
            J += 5;
            contador = 0;
        }
    }
    return 0;
}
