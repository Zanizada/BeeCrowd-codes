#include <stdio.h>

int main() {
    int N;
    float a, b, c, media;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%f %f %f", &a, &b, &c);
        media = ((a*2)+(b*3)+(c*5))/(2+3+5);
        printf("%.1f\n", media);
    }
    return 0;
}
