#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[])
{
    int rank, p, offset;
    int N, i, j, k;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&p);

    offset = (rank*N)/p;
    n = ((rank+1)*N))/p - offset;

    u = (double*)malloc((n+2)*sizeof(double));
    u_prev = (double*)malloc((n+2)*sizeof(double));

    for (i=0; i<=size; i++) 
        u_prev[i] = sin(PI*(i+offset)/(N+1));

    t=0.0
    while (t<final_T) {
        for (i=1;i<n;i++)
            u[i] = u_prev[i] + a*u_prev[i-1]-2*u_prev+u_prev[i+1]

        // Send left
        if (my_rank == 0)
            u[0] = 0.0;
        else
            MPI_Sendrecv(u[1], 1, MPI_DOUBLE, rank-1, 111,u[0],1,MPI_DOUBLE, rank-1, 222,MPI_COMM_WORLD, &status);

        // Send right
        if (my_rank == num_procs-1)
            u[n+1] = 0.0;
        else
            MPI_Sendrecv(u[n], 1, MPI_DOUBLE, rank+1, 222,u[n+1],1,MPI_DOUBLE, rank+1,111,MPI_COMM_WORLD, &status);

    }

    MPI_Finalize();
    return 0;
}