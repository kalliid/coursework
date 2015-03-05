#include "system.h"

Atom::Atom (float x, float y, float z) {
    r = vec3(x, y, z);
    v = vec3();
    F = vec3();
}

void Atom::reset_force() {
    F.set(0,0,0);
}

System::System(int Nc) {
    sys_size = vec3(Nc*b, Nc*b, Nc*b);
}

void System::initialize_FCC_lattice(int Nc) {
   // Generates the positions of all the atoms in a
   // NcxNcxNc face-centered cubic lattic
   for (int i=0; i<Nc; i++) {
       for (int j=0; j<Nc; j++) {
           for (int k=0; k<Nc; k++) {
               atoms.push_back(Atom(b*i,     b*j,     b*k));
               atoms.push_back(Atom(b*i+b/2, b*j+b/2, b*k));
               atoms.push_back(Atom(b*i+b/2, b*j,     b*k+b/2));
               atoms.push_back(Atom(b*i,     b*j+b/2, b*k+b/2));
           }
       }
   }
//   calculate_forces();
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

void System::enforce_periodic() {
    for (Atom &atom : atoms)
        atom.r = (atom.r + sys_size) % sys_size;
}

void System::reset_all_forces() {
    for (Atom &atom : atoms)
        atom.reset_force();
}

void System::calc_forces_between_pair(int i, int j) {
//    // Force on atom i from atom j and vice versa
//    // Uses the minimum image convention
//    vec3 dr = atoms[j].r - atoms[i].r;
//    dr = dr - (dr/sys_size).round()*sys_size;
//    float r = dr.length();

//    vec3 F = dr*(24*(2*pow(r,-14) - pow(r,-8)));
//    F = vec3();

//    atoms[i].F += F;
//    atoms[j].F -= F;
}

void System::calculate_forces() {
    /*
    reset_all_forces();

    for (size_t i=0, N=atoms.size(); i<N; i++)
        for (size_t j=i+1; j<N; j++)
            calc_forces_between_pair(i,j);
    */
}


