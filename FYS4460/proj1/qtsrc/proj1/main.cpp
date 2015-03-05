#include <iostream>
#include "system.h"
#include "io.h"
#include "integrator.h"
#include "parameters.h"

using namespace std;

int main()
{
    int Nc = 2;
    char outfile[] = "../../data/testfile.xyz";
    char header[] = "Face-centered cubic lattice of argon atoms";

    // Generate and initialize lattice
    System lattice = System(Nc);
    lattice.initialize_FCC_lattice(Nc);
    lattice.initialize_velocities(100);
    lattice.eliminate_drift();

    // Set up logger
    Logger logger = Logger(&lattice, outfile);

    logger.write_header(header);
    logger.write_current_state();
    lattice.enforce_periodic();
    logger.write_current_state();

    Verlet_integrator solver = Verlet_integrator(&lattice);

    for (int i=0; i<100; i++) {
       cout << i << endl;
       solver.velocity_verlet_step(dt);
       logger.write_current_state();
    }
}

