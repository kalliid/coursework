#include "argon_lattice.h"

Cells::Cells(int Nc) {
    Ncells = Nc*Nc*Nc;

    // Initialize cell origins
    for (int i=1; i<=Nc; i++)
        for (int j=1; j<=Nc; j++)
            for (int k=1; k<=Nc; k++)
                origins.push_back(vec3(b*i, b*j, b*k));
}

Atoms::Atoms(int Nc) {
    Natoms = 4*Nc*Nc*Nc;
    forces.resize(Natoms);
}

void Atoms::initialize_positions(Cells cells) {
    vec3 p0 = vec3(0,   0,   0);
    vec3 p1 = vec3(b/2, b/2, 0);
    vec3 p2 = vec3(b/2, 0,   b/2);
    vec3 p3 = vec3(0,   b/2, b/2);

    for (vec3 cell_origin : cells.origins) {
        positions.push_back(cell_origin + p0);
        positions.push_back(cell_origin + p1);
        positions.push_back(cell_origin + p2);
        positions.push_back(cell_origin + p3);
    }
}

void Atoms::initialize_velocities(float T) {
    // Generates the initial velocities of all atoms in the lattice
    // Each velocity is drawn independantly from a Boltzmann distribution

    // Set up RNG following Boltzmann distribution
    random_device rd;
    mt19937 gen(rd());
    normal_distribution<double> boltzmann_dist(0, sqrt(k_b*T/m));

    vec3 avg_vel = vec3();

    // Draw velocities
    for (int i=0; i<Natoms; i++) {
        vec3 rand_vel = vec3(boltzmann_dist(gen), boltzmann_dist(gen), boltzmann_dist(gen));
        velocities.push_back(rand_vel);
        avg_vel += rand_vel;
    }

    // Remove any net linear momentum
    avg_vel /= Natoms;
    for (vec3 &vel : velocities)
        vel -= avg_vel;
}

