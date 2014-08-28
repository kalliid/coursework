
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct
{
	double** elements; /* a 2D array of doubles */
	double* storage;
	int m; /* number of columns */
	int n; /* number of rows */
}
matrix;

void allocate_matrix(matrix *A, int m, int n)
{
	int i,j;
	A->storage = (double*)malloc(n*m*sizeof(double)); // underlying contiguous array
	A->elements = (double**)malloc(m*sizeof(double*));
	for(i=0;i<m;i++){
		A->elements[i] = &(A->storage[i*n]);
		for(j=0;j<n;j++){
			A->elements[i][j] = 0;
		}
	}
	A->m = m;
	A->n = n;
}

void deallocate_matrix(matrix *A)
{
	free(A->storage);
	free(A->elements);
}

void print_matrix(matrix A){
	int i,j,m,n;
	m=A.m;
	n=A.n;

	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			printf("%6.2f \t", A.elements[i][j]);
		}
		printf("\n");
	}
}
int multiply_matrices(matrix A, matrix B, matrix *C){
	int i,j,k,m,l,n;
	m = A.m;
	l = A.n;
	n = B.n;

	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			for(k=0;k<l;k++){
				C->elements[i][j] += A.elements[i][k]*B.elements[k][j];
			}
		}
	}

	return 0;
}


void read_matrix_binaryformat(char* filename, matrix* M,int* num_rows, int* num_cols)
{
	int i;
	FILE* fp = fopen (filename,"rb");
	fread(num_rows, sizeof(int), 1, fp);
	fread(num_cols, sizeof(int), 1, fp);
	/* storage allocation of the matrix */
	allocate_matrix(M, *num_rows, *num_cols);

	// *matrix = (double**)malloc((*num_rows)*sizeof(double*));
	// (*matrix)[0] = (double*)malloc((*num_rows)*(*num_cols)*sizeof(double));
	// for (i=1; i<(*num_rows); i++)
	// 	(*matrix)[i] = (*matrix)[i-1]+(*num_cols);
	/* read in the entire matrix */
	fread((*M).elements[0], sizeof(double), (*num_rows)*(*num_cols), fp);
	fclose(fp);
}

void write_matrix_binaryformat (char* filename, matrix M)
{
	FILE *fp = fopen (filename,"wb");
	fwrite(&(M.m), sizeof(int), 1, fp);
	fwrite(&(M.n), sizeof(int), 1, fp);
	fwrite(M.elements[0], sizeof(double), M.m*M.n, fp);
	fclose(fp);
}



int main(int argc, char *argv[])
{
	int m,n,l;
	matrix A,B,C, test;
	char *A_filename, *B_filename, *C_filename, *test_filename;

	A_filename = "A_liten.bin";
	B_filename = "B_liten.bin";
	C_filename = "C_liten.bin";

	test_filename = "AB_liten.bin";

	m = 9;
	l = 7;
	n = 5;

	allocate_matrix(&A,m,l);
	allocate_matrix(&B,l,n);
	allocate_matrix(&C,m,n);



	A.elements[0][0] = 2;
	A.elements[1][0] = 3;
	A.elements[2][0] = -5;
	A.elements[3][0] = 6;
	A.elements[4][0] = 0;
	A.elements[5][0] = -2;
	A.elements[6][0] = 7;
	A.elements[7][0] = -8;
	A.elements[8][0] = 2;
	A.elements[0][1] = 2;
	A.elements[1][1] = 6;
	A.elements[2][1] = 7;
	A.elements[3][1] = 9;
	A.elements[4][1] = -3;
	A.elements[5][1] = -6;
	A.elements[6][1] = -7;
	A.elements[7][1] = -2;
	A.elements[8][1] = 1;
	A.elements[0][2] = 2;
	A.elements[1][2] = 3;
	A.elements[2][2] = 7;
	A.elements[3][2] = 8;
	A.elements[4][2] = -5;
	A.elements[5][2] = 3;
	A.elements[6][2] = 1;
	A.elements[7][2] = 0;
	A.elements[8][2] = 0;
	A.elements[0][3] = 1;
	A.elements[1][3] = -2;
	A.elements[2][3] = 5;
	A.elements[3][3] = 7;
	A.elements[4][3] = 2.4;
	A.elements[5][3] = -1.3;
	A.elements[6][3] = 5;
	A.elements[7][3] = 2;
	A.elements[8][3] = 0;
	A.elements[0][4] = 2;
	A.elements[1][4] = -3;
	A.elements[2][4] = -4;
	A.elements[3][4] = 0;
	A.elements[4][4] = 4;
	A.elements[5][4] = 1;
	A.elements[6][4] = 0;
	A.elements[7][4] = 2;
	A.elements[8][4] = -4;
	A.elements[0][5] = 5;
	A.elements[1][5] = 3;
	A.elements[2][5] = -3;
	A.elements[3][5] = 1;
	A.elements[4][5] = -1;
	A.elements[5][5] = -1;
	A.elements[6][5] = 9;
	A.elements[7][5] = 4;
	A.elements[8][5] = 3;
	A.elements[0][6] = 4;
	A.elements[1][6] = 2;
	A.elements[2][6] = 1;
	A.elements[3][6] = -3;
	A.elements[4][6] = 2;
	A.elements[5][6] = 6;
	A.elements[6][6] = 3;
	A.elements[7][6] = 0;
	A.elements[8][6] = -2;

	
	B.elements[0][0] = 0;
	B.elements[1][0] = 2;
	B.elements[2][0] = 3;
	B.elements[3][0] = -4;
	B.elements[4][0] = 2;
	B.elements[5][0] = -1;
	B.elements[6][0] = 0;
	B.elements[0][1] = -6;
	B.elements[1][1] = 3.3;
	B.elements[2][1] = -2;
	B.elements[3][1] = 0;
	B.elements[4][1] = 1;
	B.elements[5][1] = -1;
	B.elements[6][1] = 4;
	B.elements[0][2] = 5.5;
	B.elements[1][2] = -7;
	B.elements[2][2] = 2;
	B.elements[3][2] = 3;
	B.elements[4][2] = 0;
	B.elements[5][2] = 5;
	B.elements[6][2] = 0;
	B.elements[0][3] = 2;
	B.elements[1][3] = 1;
	B.elements[2][3] = 1;
	B.elements[3][3] = 1;
	B.elements[4][3] = -3;
	B.elements[5][3] = 2.7;
	B.elements[6][3] = 11;
	B.elements[0][4] = 3;
	B.elements[1][4] = 0;
	B.elements[2][4] = -1;
	B.elements[3][4] = 4;
	B.elements[4][4] = 2;
	B.elements[5][4] = 7;
	B.elements[6][4] = -4;
	
	multiply_matrices(A,B,&C);

	write_matrix_binaryformat(A_filename,A);
	write_matrix_binaryformat(B_filename,B);
	write_matrix_binaryformat(C_filename,C);

	read_matrix_binaryformat(test_filename, &test, &m, &n);

	print_matrix(C);
	printf("\n \n");
	print_matrix(test);

}