#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    const char* meses[12] = {
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    };

    if (N >= 1 && N <= 12) {
        printf("%s\n", meses[N - 1]);
    }

    return 0;
}
