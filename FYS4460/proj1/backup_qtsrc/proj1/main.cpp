#include <iostream>
#include "argon_lattice.h"
#include "integrator.h"
#include "system.h"
#include "io.h"

using namespace std;

int main()
{
//    #define ATOMIC_UNITS
    int Nc = 8;
    char outfile[] = "../../data/testfile.xyz";
    char header[] = "Face-centered cubic lattice of argon atoms";

    // Generate and initialize lattice
    System argon_lattice;
    argon_lattice.initialize_FCC_lattice(Nc);
    argon_lattice.initialize_velocities(100);
    argon_lattice.eliminate_drift();

    // Set up logger
    Logger logger = Logger(&argon_lattice, outfile);
    logger.write_header(header);
    logger.write_current_state();


//    Cells cells = Cells(Nc);
//    Atoms atoms = Atoms(Nc);
//    atoms.initialize_positions(cells);
//    atoms.initialize_velocities(100);

//    FILE* outfile = fopen("../../data/testfile.txt", "w");

//    write_header(atoms.Natoms, header, outfile);
//    write_current_state(atoms,outfile);
//    fclose(outfile);

//    Verlet_integrator solver = Verlet_integrator(&atoms, &cells);/**/

}
