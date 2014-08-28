#include <stdlib.h>
#include <stdio.h>
#include <mpi.h>

#define ndims 2;

void allocate_matrix(double** A, int m, int n) {
    int i;
    double *A_storage = (double*)malloc(m*n*sizeof(double));
    A = (double**)malloc(m*sizeof(double*));
    for (i=0; i<m; i++) 
        A[i] = &(A_storage[i*n]);
}

void allocate_vector(double* x, int n) {
    int i;
    x = malloc(n*sizeof(double));
    for (i=0; i<n; i++)
        x[i] = 0.0;
}

void allocate_ivector(int* x, int n) {
    int i;
    x = malloc(n*sizeof(int));
    for (i=0; i<n; i++)
        x[i] = 0.0;
}

int BLOCK_LOW(int id, int p, int n) {
    return (id*n)/p;
}

int BLOCK_HIGH(int id, int p, int n) {
    return BLOCK_LOW(id+1, p, n);
}

int BLOCK_SIZE(int id, int p, int n) {
    return BLOCK_HIGH(id, p, n) - BLOCK_LOW(id, p, n);
}

int main(int argc, char *argv[])
{
    int i, j;
    int m=4;
    int n=4;
    int my_rank, num_procs, pi, pj;
    double **A, **my_A, *x, *my_x, *y, *my_y;
    int disp_m, disp_n, my_m, my_n;

    MPI_Comm mpi_comm_cart;
    MPI_Comm mpi_comm_cols;
    MPI_Comm mpi_comm_rows;

    int dims[ndims] = {0};
    int coords[ndims] = {0};
    
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
    
    MPI_Dims_create(num_procs, ndims, dims);

    MPI_Cart_create(MPI_COMM_WORLD, ndims, dims, (int[ndims]){0}, false, &mpi_comm_cart);

    MPI_Cart_coords(mpi_comm_cart, my_rank, ndims, &coords);

    MPI_Comm_split(MPI_COMM_WORLD, coords[0], coords[1], &mpi_comm_cols);
    MPI_Comm_split(MPI_COMM_WORLD, coords[1], coords[0], &mpi_comm_rows);

    disp_m = BLOCK_LOW(coords[1],dims[1],m);
    my_m = BLOCK_SIZE(coords[1],dims[1],m);
    disp_n = BLOCK_LOW(coords[0],dims[0],m);
    my_n = BLOCK_SIZE(coords[0],dims[0],m);

    allocate_matrix(my_A, my_m, my_n);
    allocate_vector(my_x, my_n);
    allocate_vector(my_y, my_m);

    for (i = 0; i < my_m; i++)
        for (j = 0; j < my_n; j++)
            my_A[i][j] =  (i + disp_m)*n + (j+disp_n)/(m*n-1);

    if (my_rank==0) {
        *x, *y;
        allocate_vector(x,n);
        allocate_vector(y,n);

        x[0] = 4;
        x[1] = 2;
        x[2] = 1;
        x[3] = 3;
    }

    // Scatter x to first row
    if (coords[0] == 0) {
        int *counts, *displs;
        counts = malloc(dims[0]*sizeof(int));
        displs = malloc(dims[0]*sizeof(int));
        for (i=0; i<dims[0]: i++) {
            counts[i] = BLOCK_SIZE(i, dims[0], n);
            displs[i] = BLOCK_LOW(i, dims[0], n);
        }
        MPI_Scatterv(&x, counts, displs, MPI_DOUBLE, my_x, my_n, 0, mpi_comm_rows);        

        free(displs);
        free(counts);
    }

    // First row broadcasts x to their cols
    MPI_Bcast(x, my_n, MPI_DOUBLE, 0, mpi_comm_cols);

    for (i=0; i<my_m; i++)
        for (j=0; j<my_n; i++)
            my_y[i] += my_A[i][j]*my_x[j];

    MPI_Reduce(coords[0]==0 ? MPI_IN_PLACE:my_y, my_y, my_m, MPI_DOUBLE, MPI_SUM, 0, mpi_comm_rows);

    if (coords[0] == 0) {
        int *counts, *displs;
        counts = malloc(dims[0]*sizeof(int));
        displs = malloc(dims[0]*sizeof(int));
        for (i=0; i<dims[0]: i++) {
            counts[i] = BLOCK_SIZE(i, dims[0], n);
            displs[i] = BLOCK_LOW(i, dims[0], n);
        }
        MPI_Gatherv(&my_y, my_m, MPI_DOUBLE, y, counts, displs, MPI_DOUBLE, 0, mpi_comm_cols);        
        
        free(displs);
        free(counts);
    }

    if (my_rank==0) {
        for (i=0;i<m; i++) {
            printf("%d: %f\n", i, y[i]);
        }
    }

    MPI_Comm_free(&mpi_comm_rows);
    MPI_Comm_free(&mpi_comm_cols);
    MPI_Comm_free(&mpi_comm_cart);

    MPI_Finalize();

    return 0;
}
