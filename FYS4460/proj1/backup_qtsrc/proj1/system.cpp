#include "system.h"

Atom::Atom (float x, float y, float z) {
    r = vec3(x, y, z);
}

void System::initialize_FCC_lattice(int Nc) {
   // Generates the positions of all the atoms in a
   // NcxNcxNc face-centered cubic lattic
   for (int i=0; i<Nc; i++) {
       for (int j=0; j<Nc; j++) {
           for (int k=0; k<Nc; k++) {
               atoms.push_back(Atom(b*i,     b*j,     b*k));
               atoms.push_back(Atom(b*i+b/2, b*j+b/2, b*k));
               atoms.push_back(Atom(b*i+b/2, b*j,     b*k));
               atoms.push_back(Atom(b*i,     b*j+b/2, b*k));
           }
       }
   }
}

void System::initialize_velocities(float T) {
    // Generates the initial velocities of all atoms in the system
    // Each velocity is drawn independantly from a Boltzmann distribution

    // Set up RNG following Boltzmann distribution
    random_device rd;
    mt19937 gen(rd());
    normal_distribution<double> boltzmann_dist(0, sqrt(k_b*T/m));

    for (Atom &atom : atoms)
        atom.v.set(boltzmann_dist(gen), boltzmann_dist(gen), boltzmann_dist(gen));
}

void System::eliminate_drift() {
    // Removes any drift of the system by subtracting
    // the average velocity from all atoms
    vec3 avg_vel = vec3();
    for (Atom atom : atoms)
        avg_vel += atom.v;
    avg_vel /= atoms.size();
    for (Atom &atom : atoms)
        atom.v -= avg_vel;
}
