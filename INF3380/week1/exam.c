#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <omp.h>

double trapezoidal(int n) {
    double result = 0.0;
    double h = 1.0/n;
    double x;
    int i;

    x = 0.0;
    for (i=1; i<n; i++) {
        x += h;
        result += exp(5.0*x)+sin(x)-x*x
    }

    x = 0.;
    result += 0.5*exp(5.0*x)+sin(x)-x*x;

    x = 1.0;
    result += 0.5*exp(5.0*x)+sin(x)-x*x;

    return (h*result);
}

double trapezoidal(int n) {
    double result = 0.0;
    double h = 1.0/n;
    double x;
    int i;

    #pragma omp parallel for private(x) reduction(+: result)
    for (i=1; i<n; i++) {
        x = i*h;
        result += exp(5.0*x)+sin(x)-x*x
    }

    x = 0.0;
    for (i=1; i<n; i++) {
        x += h;
        result += exp(5.0*x)+sin(x)-x*x
    }

    x = 0.;
    result += 0.5*exp(5.0*x)+sin(x)-x*x;

    x = 1.0;
    result += 0.5*exp(5.0*x)+sin(x)-x*x;

    return (h*result);
}


double trapezoidal(int n) {
    double my_result = 0.0;
    double h = 1.0/n;
    double x;
    int i;
    int my_rank, num_procs

    MPI_Comm_rank(&my_rank, MPI_COMM_WORLD);
    MPI_Comm_size(&num_procs, MPI_COMM_WORLD);

    start = (my_rank*n)/num_procs
    stop = ((my_rank+1)*n)/num_procs

    for (i=start; i<stop; i++) {
        double x = i*h
        my_result += exp(5.0*x)+sin(x)-x*x
    }

    MPI_Reduce(&my_result, &result, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD)
  
    if (my_rank==0) {
        x = 0.0;
        result += exp(5.0*x)+sin(x)-x*x
        x = 1.0;
        result += 0.5*exp(5.0*x)+sin(x)-x*x;
        return (h*result);
    }


}




void main(int argc, char* argv[]) {

    double* a = (double*)malloc(4*sizeof(double));

    a[0] = 1;
    a[1] = 2;
    a[2] = 3;
    a[3] = 4;

    double sum;
    int n = 4;

    sum = Euclidean_norm_MPI(a, n);

    printf("%g\n", sum);

}
