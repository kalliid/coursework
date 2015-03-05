#include "argon_lattice.h"

double**** make_cells(int Nc) {
    // Generates the cell positions in a NxNxN lattice

    double**** cells = new double***[Nc];
    for (int i=0; i<Nc; i++) {
        cells[i] = new double**[Nc];
        for (int j=0; j<Nc; j++) {
            cells[i][j] = new double*[Nc];
            for (int k=0; k<Nc; k++) {
                cells[i][j][k] = new double[Nc];
                cells[i][j][k][0] = b*i;
                cells[i][j][k][1] = b*j;
                cells[i][j][k][2] = b*k;
            }
        }
    }
    return cells;
}   

double** empty_state(int Natoms) {
    // Dynamically allocates an array for all particles in a 
    // face-centered cubic lattice of argon atoms with NxNxN cells.
    
    double** state = new double*[Natoms];
    for (int i=0; i<Natoms; i++)
        state[i] = new double[6];
    return state;
}

void generate_initial_positions(double** state, int Nc) {
    // Generate the initial position of all particles in the lattice
    
    double**** cells = make_cells(Nc);

    // Define mapping from cell origin to particles
    double** cell2atom = new double*[4];
    cell2atom[0] = new double[3]{0  , 0  , 0  };
    cell2atom[1] = new double[3]{b/2, b/2, 0  };
    cell2atom[2] = new double[3]{b/2, 0  , b/2};
    cell2atom[3] = new double[3]{0  , b/2, b/2};

    // Generate 4 particles per cell
    for (int i=0; i<Nc; i++)
        for (int j=0; j<Nc; j++)
            for (int k=0; k<Nc; k++)          
                for (int p=0; p<4; p++)
                    for (int d=0; d<3; d++)
                        state[4*(i*Nc*Nc+Nc*j+k)+p][d] = cells[i][j][k][d] + cell2atom[p][d];
}

void generate_initial_velocities(double** state, int Natoms, double T) {
    // Generates the initial velocities of all particles in the lattice
    // Each velocity is drawn independantly from a Boltzmann distribution

    // Set up RNG following Boltzmann distribution
    random_device rd;
    mt19937 gen(rd());
    normal_distribution<double> boltzmann_dist(0, sqrt(k_b*T/m));

    double* avg_vel = new double[3];

    // Draw Boltzman
    for (int i=0; i<Natoms; i++) {
        for (int d=0; d<3; d++) {   
                state[i][d+3] = boltzmann_dist(gen);    
                avg_vel[d] += state[i][d+3];
        }
    }

    // Remove any net linear momentum of lattice
    avg_vel[0] /= Natoms;
    avg_vel[1] /= Natoms;
    avg_vel[2] /= Natoms;

    for (int i=0; i<Natoms; i++) 
        for (int d=0; d<3; d++)    
            state[i][d+3] -= avg_vel[d];
}  
