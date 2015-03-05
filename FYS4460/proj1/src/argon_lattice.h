#ifndef PROJ1_SRC_ARGON_LATTICE_H_
#define PROJ1_SRC_ARGON_LATTICE_H_

#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <random>
#include <cmath>

using namespace std;

#define MAX_NATOMS 200000;

double const k_b = 8.31447e-7; // Boltzmann's constant in Da*Å^2/fs^2/K
double const b = 5.260; // Lattice constant for argon
double const m = 39.948; // Mass of Argon atom in amu
double const dt = 0.01;

/* Initialize */
double**** make_cells(int Nc);
double** empty_state(int Natoms);
void generate_initial_positions(double** state, int Nc);
void generate_initial_velocities(double** state, int Natoms, double T);

/* Integrator */
double* calc_forces(double** state, int Natoms);
void verlet_integrator(double** state, int Natoms);

/* Other */
void write_state(double** state, int N, FILE* outfile);



#endif