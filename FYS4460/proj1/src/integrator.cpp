#include "argon_lattice.h"

double* calc_forces(double** state, int Natoms) {
	double* forces = new double[Natoms];
	return forces;
}

void verlet_integrator(double** state, int Natoms) {

	double* forces = calc_forces(state, Natoms);



	for (int i=0; i<Natoms; i++) 
		for (int d=0; d<3; d++)
			state[i][d+3] += dt*forces[i][d]/(2*m) 
	
	for (double f : forces) {

	}

	cout << "Test";
}
