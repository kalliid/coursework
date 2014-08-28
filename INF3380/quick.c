#include <mpi.h>
#include <stdlib.h>
#include <stdio.h>



int main(int argc, char  *argv[]) {
    int i, j, k;
    int start, stop, size;
    int my_rank, num_procs;
    int* a;
    int pivot;
 
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
    MPI_Comm_size(MPI_COMM_WORLD,&num_procs);
 
    int n=10;
    a = (int*)malloc(n*sizeof(int));
    for (i=0;i<n;i++)
        a[i] = rand()%100;

    pivot = a[0];

    start = (my_rank*n)/num_procs;
    stop = ((my_rank+1)*n)/num_procs - 1;
    size = stop-start;

    int *S, *L, Scnt=0, Lcnt=0;
    S = (int*)malloc(size*sizeof(int));
    L = (int*)malloc(size*sizeof(int));

    for (i=start; i<=stop; i++) {
        if (a[i] <= pivot) {
            S[Scnt] = a[i];
            Scnt++;
        } else {
            L[Lcnt] = a[i];
            Lcnt++;
        }
    }

    // printf("My rank: %d\t", my_rank);
    // for (i=0;i<Lcnt;i++)
    //     printf("%4d  ", L[i]);
    // printf("\n");

    // if (my_rank==0) {
    //     for (i=0; i<n; i++) 
    //         printf("%4d  ", a[i]);
    //     printf("\n");
    // }

    int Soffset, Loffset, totSoffset;
    
    MPI_Scan(&Scnt, &Soffset, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
    Soffset -= Scnt;
    MPI_Scan(&Lcnt, &Loffset, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
    Loffset -= Lcnt;
    MPI_Allreduce(&Scnt, &totSoffset, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);

    // printf("My rank: %d, Soffset: %d\n", my_rank, Soffset);

    for (i=0; i<Scnt; i++) {
        printf("Global index: %d, S[i]=%d\n", Soffset+i, S[i]);

        a[Soffset+i] = S[i];
    }
    for (i=0; i<Lcnt; i++) {   
        printf("L: %d\n", totSoffset+Loffset+i);
        a[totSoffset+Loffset+i] = L[i];
    }

    MPI_Barrier(MPI_COMM_WORLD);
    if (my_rank==0) {
        for (i=0; i<n; i++) 
            printf("%4d  ", a[i]);
        printf("\n");
    }

    MPI_Finalize();
    return 0;
}
