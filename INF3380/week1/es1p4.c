#include <stdlib.h>
#include <stdio.h>

double*** m3D_alloc(int n, int m, int p);

int main()
{
    int i, j, k;
    int n = 4;
    int m = 3;
    int p = 2;

    double ***A = m3D_alloc(n,m,p);

    for (i=0; i<n*m*p; i++)
        A[0][0][i] = i;

    for (i=0; i<n; i++)
        for (j=0; j<m; j++)
            for (k=0; k<p; k++)
                printf("%.0f\n", A[i][j][k]);
}

double*** m3D_alloc(int n, int m, int p) {
    int i, j, k;
    double* A_storage = (double*) malloc (n*m*p*sizeof(double));
    double*** A = (double***) malloc (n*sizeof(double**));

    for (i=0; i<n; i++) { 
        double **A_tmp = (double **)malloc(m*sizeof(double*));
        for (j=0; j<m; j++)
            A_tmp[j] = &(A_storage[i*m*p + j*p]);

        A[i] = A_tmp;
    }

    return A;
}
