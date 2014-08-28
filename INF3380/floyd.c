#include <stdlib.h>
#include <stdio.h>
#include <mpi.h>

#define INF 100000;

int BLOCK_LOW(int i, int p, int n) {
    return (i*n)/p;
}

int BLOCK_HIGH(int i, int p, int n) {
    return ((i+1)*n)/p;
}

int BLOCK_SIZE(int i, int p, int n) {
    return BLOCK_HIGH(i,p,n) - BLOCK_LOW(i,p,n);
}

int BLOCK_OWNER(int k, int p, int n) {
    return (p*(k+1)-1)/n;
}

int main(int argc, char *argv[])
{
    int i, j, k;
    int my_rank, num_procs, size, offset;
    int **A, **myA;
    int n = 4;

    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
    
    offset = BLOCK_LOW(my_rank, num_procs, n);
    size = BLOCK_SIZE(my_rank, num_procs, n);

    int* myA_storage = (int*)malloc(n*n*sizeof(int));
    myA = (int**)malloc(size*sizeof(int*));
    for (i=0; i<size; i++) {   
        myA[i] = &myA_storage[i*n];
        for (j=0; j<n; j++)
            myA[i][j] = 0;
    }

    int* cnts = malloc(num_procs*sizeof(int));
    int* displs = malloc(num_procs*sizeof(int));
    for (i=0;i<num_procs;i++) {
        cnts[i] = BLOCK_SIZE(i, num_procs, n)*n;
        displs[i] = BLOCK_LOW(i, num_procs, n)*n;
    }

    if (my_rank==0) {
        int *A_storage = (int*)malloc(n*n*sizeof(int));
        A = (int**)malloc(n*sizeof(int*));
        for (i=0;i<n;i++)
            A[i] = &A_storage[i*n];

        A[0][0] = 0;
        A[0][1] = 4;
        A[0][2] = INF;
        A[0][3] = INF;
        A[1][0] = 2;
        A[1][1] = 0;
        A[1][2] = 3;
        A[1][3] = 3;
        A[2][0] = INF;
        A[2][1] = 4;
        A[2][2] = 0;
        A[2][3] = 3;
        A[3][0] = INF;
        A[3][1] = 2;
        A[3][2] = 4;
        A[3][3] = 0;

        for (i=0; i<n*size; i++)
            myA[0][i] = A[0][i];

        for (i=1; i<num_procs; i++) {
            MPI_Send(&A[0][displs[i]], cnts[i], MPI_INT, i, 111, MPI_COMM_WORLD);
        }
    }
      
    if (my_rank != 0)
        MPI_Recv(&myA[0][0], size*n, MPI_INT, 0, 111, MPI_COMM_WORLD, &status);
    
    free(cnts);
    free(displs);

    
    int kowner = 0;
    int *krow = (int*)malloc(n*sizeof(int));

    for (k=0; k<n; k++) {
        kowner = BLOCK_OWNER(k, num_procs, n);

        if (my_rank==kowner)
            for (i=0; i<n; i++)
                krow[i] = myA[k-offset][i];

        MPI_Bcast(&krow[0], n, MPI_INT, kowner, MPI_COMM_WORLD);
        printf("My rank: %d, krow: %d")
        // for (i=0; i<size; i++)
        //     for (j=0;j<n;j++)
        //         if (A[i][j] > A[i][k] + krow[j])
        //             A[i][j] = A[i][k] + krow[j];
    }

    // MPI_Gatherv(&myA, size, MPI_INT, &A[0][0], cnts, displs, MPI_INT, 0, MPI_COMM_WORLD);

    // if (my_rank==0) {
    //     for (i=0; i<n; i++) {
    //         for(j=0;j<n;j++)    
    //             printf("%d  ", A[i][j]);
    //         printf("\n");
    //     }
    //     printf("\n");
    // }

    MPI_Finalize();

    return 0;
}