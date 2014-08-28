#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <mpi.h>
#include <omp.h>

typedef struct
{
    double** elements; // elements of the matrix
    double* storage;   // used for contiguous storage
    int m;             // number of rows
    int n;             // number of columns
} mat;

void allocate_matrix(mat* M, int m, int);
void deallocate_matrix(mat* M);
void multiply(mat A, mat B, mat* C);
void print_matrix(mat M);
void read_matrix_binaryformat(char* filename, mat* M, int* m, int* n);
void write_matrix_binaryformat(char* filename, mat M);

int main(int argc, char *argv[])
{
    /* 
    Program to multiply matrices A and B, given as binary files, 
    in parallell using Cannon's algorithm. Result is writen to a binary file 
    */
    int i, j, k;
    int m, l, n;
    int my_rank, num_procs, p, Pi, Pj;
    mat A, B, C;

    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank (MPI_COMM_WORLD, &my_rank);
    MPI_Comm_size (MPI_COMM_WORLD, &num_procs);
    p = sqrt(num_procs - 1);
  
    /* MASTER THREAD */
    if (my_rank == 0) {
        int w;
        int m_A, n_A, m_B, n_B, m_C, n_C, lmax;
        int icntA, jcntA, icntB, jcntB, icntC, jcntC;
        char *infile_A, *infile_B, *outfile;
        mat subA, subB, subC;

        if (p*p != num_procs - 1) {
            printf("Number of processes must be a perfect square + 1, e.g. 10 (3*3+1). \n");
            return 1;
        }

        if (argc != 4) {
            printf("Error: Please specify infiles A and B, and outfile C.\n");
            return 1;
        }

        infile_A = argv[1];
        infile_B = argv[2];
        outfile = argv[3];

        // /* GET MATRICES A AND B FROM FILES */
        read_matrix_binaryformat(infile_A, &A, &m, &l);
        read_matrix_binaryformat(infile_B, &B, &l, &n);
        allocate_matrix(&C, m, n);

        /* DIVIDE MATRICES INTO SUBMATRICES AND SEND TO WORKERS */
        icntA = 0;
        jcntA = 0;
        icntB = 0;
        jcntB = 0;
        for (w=1; w<num_procs; w++) {
            // Find process-coordinates
            Pi = (w-1)/p;
            Pj = (w-1)%p;

            // Find dimensions of submatrices
            m_A = Pi<m%p ? m/p+1 : m/p;
            n_A = Pj<l%p ? l/p+1 : l/p;
            lmax = 0<l%p ? l/p+1 : l/p;
            m_B = Pi<l%p ? l/p+1 : l/p;
            n_B = Pj<n%p ? n/p+1 : n/p;

            // Extract submatrices
            allocate_matrix(&subA, m_A, lmax);
            allocate_matrix(&subB, lmax, n_B);

            for (i=0; i<m_A; i++) {   
                for (j=0; j<n_A; j++)
                    subA.elements[i][j] = A.elements[i+icntA][j+jcntA];           
            }

            for (i=0; i<m_B; i++)
                for (j=0; j<n_B; j++)
                    subB.elements[i][j] = B.elements[i+icntB][j+jcntB];

            jcntA += n_A;
            jcntB += n_B;
            if (w%p == 0) {
                icntA += m_A;
                icntB += m_B;
                jcntA = 0;
                jcntB = 0;
            }

            // Send submatrices
            MPI_Send(&m_A, 1, MPI_INT, w, 1, MPI_COMM_WORLD);
            MPI_Send(&lmax, 1, MPI_INT, w, 1, MPI_COMM_WORLD);
            MPI_Send(&n_B, 1, MPI_INT, w, 1, MPI_COMM_WORLD);

            MPI_Send(&subA.elements[0][0], m_A*lmax, MPI_DOUBLE, w, 1, MPI_COMM_WORLD);
            MPI_Send(&subB.elements[0][0], lmax*n_B, MPI_DOUBLE, w, 1, MPI_COMM_WORLD);

            deallocate_matrix(&subA);
            deallocate_matrix(&subB);
        }

        deallocate_matrix(&A);
        deallocate_matrix(&B);

        /* RECIEVE RESULTS FROM WORKERS AND COMBINE */
        icntC = 0;
        jcntC = 0;
        for (w=1; w<num_procs; w++) {
            MPI_Recv(&m_C, 1, MPI_INT, w, 1, MPI_COMM_WORLD, &status);
            MPI_Recv(&n_C, 1, MPI_INT, w, 1, MPI_COMM_WORLD, &status);

            allocate_matrix(&subC, m_C, n_C);

            MPI_Recv(&subC.elements[0][0], m_C*n_C, MPI_DOUBLE, w, 1, MPI_COMM_WORLD, &status);

            for (i=0; i<m_C; i++)
                for (j=0; j<n_C; j++)
                    C.elements[i+icntC][j+jcntC] = subC.elements[i][j];

            jcntC += n_C;
            if (w%p == 0) {
                icntC += m_C;
                jcntC = 0;
            }

            deallocate_matrix(&subC);
        }

        /* WRITE FINAL RESULT TO FILE */
        write_matrix_binaryformat(outfile, C);
        deallocate_matrix(&C);

        /* MASTER THREAD DONE */

    /* WORKER THREAD */
    } else {
        int i;
        int left, right, up, down;
        int to_A, from_A, to_B, from_B;

        Pi = (my_rank-1)/p;
        Pj = (my_rank-1)%p;

        // /* RECIEVE INITAL DATA */
        MPI_Recv(&m, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
        MPI_Recv(&l, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
        MPI_Recv(&n, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
        
        allocate_matrix(&A, m, l);
        allocate_matrix(&B, l, n);
        allocate_matrix(&C, m, n);

        MPI_Recv(&A.elements[0][0], m*l, MPI_DOUBLE, 0, 1, MPI_COMM_WORLD, &status);
        MPI_Recv(&B.elements[0][0], l*n, MPI_DOUBLE, 0, 1, MPI_COMM_WORLD, &status);

        /* ALIGN INITAL SUBMATRICES */
        // Find process coordinates for dest and source
        left = (Pj - Pi + p) % p;
        right = (Pj + Pi) % p;
        up = (Pi - Pj + p) % p;
        down = (Pi + Pj) % p;

        // Find worker numbers
        to_A = Pi*p + left + 1;
        from_A = Pi*p + right + 1;
        to_B = up*p + Pj + 1;
        from_B = down*p + Pj + 1;

        // Shift submatrices
        if (to_A != my_rank)
            MPI_Sendrecv_replace(&A.elements[0][0], m*l, MPI_DOUBLE, to_A, 1, from_A, 1, MPI_COMM_WORLD, &status);
        if (to_B != my_rank)
            MPI_Sendrecv_replace(&B.elements[0][0], l*n, MPI_DOUBLE, to_B, 1, from_B, 1, MPI_COMM_WORLD, &status);

        /* MULTIPLY SUB-MATRICES AND SHIFT */
        left = (Pj - 1 + p) % p;
        right = (Pj + 1) % p;
        up = (Pi - 1 + p) % p;
        down = (Pi + 1) % p;

        to_A = Pi*p + left + 1;
        from_A = Pi*p + right + 1;
        to_B = up*p + Pj + 1;
        from_B = down*p + Pj + 1;

        for (i=0; i<p; i++) {
            multiply(A, B, &C);

            MPI_Sendrecv_replace(&A.elements[0][0], m*l, MPI_DOUBLE, to_A, 1, from_A, 1, MPI_COMM_WORLD, &status);
            MPI_Sendrecv_replace(&B.elements[0][0], l*n, MPI_DOUBLE, to_B, 1, from_B, 1, MPI_COMM_WORLD, &status);
        }

        /* RETURN RESULTS TO MASTER THREAD */
        MPI_Send(&m, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
        MPI_Send(&n, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
        MPI_Send(&C.elements[0][0], m*n, MPI_DOUBLE, 0, 1, MPI_COMM_WORLD);
        
        /* WORKER THREAD DONE*/
        deallocate_matrix(&A);       
        deallocate_matrix(&B);       
        deallocate_matrix(&C);       
    }

    /* END OF MAIN */
    MPI_Finalize ();
    return 0;
}

void allocate_matrix(mat* M, int m, int n) {
    /* Allocates memory to a matrix struct */
    int i, j;
    M->m = m;
    M->n = n;
    M->storage  = (double*)malloc(m*n*sizeof(double));
    M->elements = (double**)malloc(m*sizeof(double*));
    for (i=0; i<m; i++) {
        M->elements[i] = &(M->storage[i*n]);
        for (j=0; j<n; j++) {
            M->elements[i][j] = 0;
        }
    }
}

void deallocate_matrix(mat* M) {
    /* Deallocates memory used by a matrix struct */
    free(M->storage);
    free(M->elements);
}

void multiply(mat A, mat B, mat* C){
    /* Multiplies matrices A and B and adds (appends) result to C */
    int i, j, k, m, l, n;
    m = A.m;
    l = A.n;
    n = B.n;
    
    #pragma omp parallel for private(j,k)
    for (i=0; i<m; i++)
        for (j=0; j<n; j++)
            for (k=0; k<l; k++)
                C->elements[i][j] += A.elements[i][k]*B.elements[k][j];
}

void print_matrix(mat M) {
    /* Prints a matrix struct */
    int i, j;
    for (i=0; i<M.m; i++) {   
        for (j=0; j<M.n; j++) {
            printf("%8g", M.elements[i][j]);
        }
        printf("\n");
    }
}

void read_matrix_binaryformat(char* filename, mat* M, int* m, int* n) {
    /* Reads a matrix from binary file and stores it in a matrix struct*/ 
    FILE* fp = fopen(filename, "rb");
    fread(m, sizeof(int), 1, fp);
    fread(n, sizeof(int), 1, fp);

    allocate_matrix(M, *m, *n);

    fread((*M).elements[0], sizeof(double), (*m)*(*n), fp);
    fclose(fp);
}

void write_matrix_binaryformat(char* filename, mat M) {
    /* Writes a matrix struct to a binary file */
    FILE *fp = fopen(filename, "wb");
    fwrite(&(M.m), sizeof(int), 1, fp);
    fwrite(&(M.n), sizeof(int), 1, fp);
    fwrite(M.elements[0], sizeof(double), M.m*M.n, fp);
    fclose(fp);
}