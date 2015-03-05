#ifndef ARGON_LATTICE_H
#define ARGON_LATTICE_H

//#include <iostream>
//#include <iomanip>
//#include <string>
//#include <map>
//#include <cmath>
#include <random>
#include <vector>
#include "vec3.h"

using namespace std;

#ifndef ATOMIC_UNITS
// Atomic Units uses
float const k_b = 1.0;
float const b = 5.260; // Lattice constant for argon
float const m = 39.948; // Mass of Argon atom in amu
float const dt = 0.01;
#else
// Physical Constants used
float const k_b = 8.31447e-7; // Boltzmann's constant in Da*Å^2/fs^2/K
float const b = 5.260; // Lattice constant for argon
float const m = 39.948; // Mass of Argon atom in amu
float const dt = 0.01;
#endif

class Cells {
public:
    int Ncells;
    vector<vec3> origins;
    Cells(int Nc);
};

class Atoms {
public:
    int Natoms;
    vector<vec3> positions;
    vector<vec3> velocities;
    vector<vec3> forces;

    Atoms(int Nc);
    void initialize_positions(Cells cells);
    void initialize_velocities(float T);
};


// IO methods
void write_header(int Natoms, char msg[], FILE* outfile);
void write_current_state(Atoms atoms, FILE* outfile);

#endif // ARGON_LATTICE_H
