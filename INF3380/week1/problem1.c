#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char* argv[]) {

    int N = 100;
    int i;
    double s = 0;

    for (i=0; i<N; i++) {
        s += pow(-1,i)*pow(0.5,2*i);
    }

    printf("%g \n",s);

    return 0;
}
