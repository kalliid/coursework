#include "argon_lattice.h"
    
int main() {
    int Nc = 8;
    int Natoms = 4*Nc*Nc*Nc;
    double T = 100; // Initial temperature, K

    double** state = empty_state(Natoms);
    generate_initial_positions(state, Nc);
    generate_initial_velocities(state, Natoms, T);

    verlet_integrator(state, Natoms);

    delete[] (state);
}

