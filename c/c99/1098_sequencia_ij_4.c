#include <stdio.h>
#include <math.h>

int main() {
    double I = 0.0;

    while (I <= 2.0 + 1e-9) {
        double J = 1.0 + I;

        for (int k = 0; k < 3; k++) {

            if (fabs(I - (int)I) < 1e-9) {
                printf("I=%d ", (int)I);
            } else {
                printf("I=%.1f ", I);
            }

            if (fabs(J - (int)J) < 1e-9) {
                printf("J=%d\n", (int)J);
            } else {
                printf("J=%.1f\n", J);
            }

            J++;
        }

        I = round((I+0.2)*10)/10.0;
    }

    return 0;
}
