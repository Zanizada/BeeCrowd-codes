#include <stdio.h>
#include <stdlib.h>

int compare(const void *x, const void *y) {
    return (*(int*)x - *(int*)y);
}

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int numeros[3] = {a, b, c};
    qsort(numeros, 3, sizeof(int), compare);
    for (int i = 0; i < 3; i++) {
        printf("%d\n", numeros[i]);
    }
    printf("\n%d\n%d\n%d\n", a, b, c);
    return 0;
}
