#include <stdlib.h>
#include <stdio.h>

int main()
{

}

double** smooth(double **v_new, double *v, int m, int n, double c) {
    int i, j;

    for (i=1; i<n-1; i++)
        for (j=1; j<m-1; j++)
            v_new[i][j] = v[i][j] + c*(v[i-1][j]+v[i][j+1]+v[i][j-1]+v[i+1][j]-4*v[i][j]);
}