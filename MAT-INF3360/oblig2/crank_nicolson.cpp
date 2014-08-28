#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <fstream>

using namespace std;

void Crank_Nicolson(double **u, double r, int n, int m) {
	// Dynamic-memory allocation of vectors
	double *b, *v, p;
	b = new double[n+1];
	v = new double[n+1];
	double c = 2 - 2*r;
	b[0] = 2 + 2*r;

	for (int j=1; j<=m; j++)
	{
		// Initialize tri-diag vectors
		for (int i=1; i<=n; i++)
		{
			b[i] = b[0];
			v[i] = r*u[i+1][j-1] + c*u[i][j-1] + r*u[i-1][j-1];
		}	

		// Decomposition of matrix A
		for (int i=1; i<=(n-1); i++)
		{
			p = -r/b[i];	
			b[i+1] += p*r;
			v[i+1] -= p*v[i];
		}

		// Forward substitution
		u[n][j] = v[n]/b[n];
		for (int i=n-1; i>=1; i--)
			u[i][j] = (v[i] + r*u[i+1][j])/b[i];
	}
}

void Crank_Nicolson(double **C, double, int, int);

int main(int argc, char* argv[]) {
	if (argc!=2) {
		cout << "Bad usage: " << argv[0] <<
		"Please specify outfile" << endl;
	exit(1);
	}

	// Prepare outfile
	ofstream outfile;
	outfile.open(argv[1], ios::binary);

	int n = 11;
	int m = 250;

	double L = 1; double T = 0.1;
	double x0=0; double t0=0;

	double dx = L/(n+1);
	double dt = T/(m+1);
	double alpha = dt/dx/dx;
	double *x, *t;
	x = new double[n+2];
	t = new double[m+2];
	for (int i=0; i<=n+1; i++)
		x[i] = x0 + i*dx;
	for (int i=0; i<=m+1; i++)
		t[i] = t0 + i*dt;

	// Dynamic-memory allocation of matrix
	double **u;
	u = new double *[n+2];
	for (int i=0; i<=n+1; i++)
		u[i] = new double[m+2];

	// Initial condition
	for (int i=0; i<=n+1; i++) {
		if (x[i] < 0.5)
			u[i][0] = 2*x[i];
		else
			u[i][0] = 2*(1-x[i]);
	}
		
	// Boundry conditions
	for (int j=1; j<=m+1; j++)
		u[0][j] = u[n][j] = 0;

	
	Crank_Nicolson(u, alpha, n, m);

	// Writing results to outfile
	for (int i=0; i<=n+1; i++)
		for (int j=0; j<=m+1; j++)
			outfile.write((char*) &u[i][j], sizeof(double));
	
	outfile.close();
	return 0;
}

