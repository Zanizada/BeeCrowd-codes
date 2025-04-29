#include <stdio.h>
#include <stdlib.h>
int main() {
    int a, b, c, AB, Maior;
    scanf("%d %d %d", &a, &b, &c);
    AB = (a + b + abs(a - b)) / 2;
    Maior = (c + AB + abs(c - AB)) / 2;
    printf("%d eh o maior\n", Maior);
    return 0;
}
