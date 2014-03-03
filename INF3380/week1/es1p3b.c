#include <stdlib.h>

int main() {
    int i, j;
    int m = 10000;
    int n = 10000;

    double **A = (double **) malloc(m*sizeof(double *));
    for (i=0; i<m; i++)
        A[i] = (double*) malloc(n*sizeof(double));

    for (j=0; j<m; j++)   
        for (i=0; i<n; i++)
            A[i][j] = i+j;
}