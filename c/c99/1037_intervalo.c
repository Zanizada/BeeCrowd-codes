#include <stdio.h>

int main() {
    double N;
    scanf("%lf", &N);
    if (N >= 0 && N <= 25.0000) {
        printf("Intervalo [0,25]\n");
    }
    else if (N > 25.00001 && N <= 50.0000) {
        printf("Intervalo (25,50]\n");
    }
    else if (N > 50.00001 && N <= 75.0000) {
        printf("Intervalo (50,75]\n");
    }
    else if (N > 75.00001 && N <= 100.0000) {
        printf("Intervalo (75,100]\n");
    }
    else {
        printf("Fora de intervalo\n");
    }
    return 0;
}
