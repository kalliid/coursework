#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

double max(double* v, int n);
double min(double* v, int n);

int main() 
{
    int i;
    int n = 10;
    double *v = (double*) malloc(n*sizeof(double));

    srand(time(NULL));
    for (i=0; i<n; i++) {
        v[i] = rand();
    }

    printf("Min: %.0f   Max: %.0f\n", min(v, n), max(v, n));
}

double max(double* v, int n) {
    int i;
    int cmax = -32000;
    for (i=0; i<n; i++)
        if (v[i] > cmax)
            cmax = v[i];
    return cmax;
}

double min(double* v, int n) {
    int i;
    int cmin = 2147483647;
    for (i=0; i<n; i++)
        if (v[i] < cmin)
            cmin = v[i];
    return cmin;
}

