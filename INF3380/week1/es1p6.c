#include <stdlib.h>
#include <stdio.h>

double** smooth(double **v_new, double **v, int m, int n, double c);
double** m2D_alloc(int n, int m);


int main()
{
    double **u = m2D_alloc(4,4);
    double **u_new = m2D_alloc(4,4);

    int i,j;
    for (i=0; i<4; i++)
        for (j=0; j<4; j++)
            u[i][j] = 5;
    u[1][1] = 2.5;

    smooth(u_new, u, 4, 4, 0.5);

    for (i=0; i<4; i++) {   
        for (j=0; j<4; j++)
            printf("%.0f\t", u[i][j]);
        printf("\n");
    }

    printf("\n");

    for (i=0; i<4; i++) {   
        for (j=0; j<4; j++)
            printf("%.2f\t", u_new[i][j]);
        printf("\n");
    }
}

double** smooth(double **v_new, double **v, int n, int m, double c) {
    int i, j;

    v_new[0][0] = v[0][0];
    v_new[n-1][0] = v[n-1][0];
    v_new[0][m-1] = v[0][m-1];
    v_new[n-1][m-1] = v[n-1][m-1];

    for (i=1; i<n-1; i++) {  
        v_new[i][0] = v[i][0] + c*(v[i-1][0] + v[i+1][0] - 2*v[i][0]);
        v_new[i][m-1] = v[i][m-1] + c*(v[i-1][m-1] + v[i+1][m-1] - 2*v[i][m-1]);
        for (j=1; j<m-1; j++)
            v_new[i][j] = v[i][j] + c*(v[i-1][j]+v[i][j+1]+v[i][j-1]+v[i+1][j]-4*v[i][j]);
    }
    for (j=1; j<m-1; j++) {   
        v_new[0][j] = v[0][j] + c*(v[0][j-1] + v[0][j+1] - 2*v[0][j]);
        v_new[n-1][j] = v[n-1][j] + c*(v[n-1][j-1] + v[n-1][j+1] - 2*v[n-1][j]);
    }
}

double** m2D_alloc(int n, int m) {
    int i;
    double* A_storage = (double*) malloc (n*m*sizeof(double));
    double** A = (double**) malloc (n*sizeof(double*));
    for (i=0; i<n; i++)
        A[i] = &(A_storage[i*m]);
    return A;
}
