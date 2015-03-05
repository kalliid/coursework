#include "argon_lattice.h"

void write_state(atom* state, int Natoms, FILE* outfile) {
    // Write a given state to a .xyz file

    // Write header
    fprintf(outfile, "%d \n", Natoms);
    fprintf(outfile, "Face-centered cubic lattice of argon atoms \n");

    // Write state data
    for (atom* atom : state) {
        fprintf(outfile, "Ar ");
        for (int d=0; d<3; d++) {
            fprintf(outfile, "%f ", atom.r[d]);
            fprintf(outfile, "%f ", atom.v[d]);
        }
        fprintf(outfile, "\n");
    }
}
