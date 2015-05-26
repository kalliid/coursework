#include <iostream>
#include "system.h"
#include "io.h"
#include "integrator.h"
#include "parameters.h"

using namespace std;

int main()
{
    int Nc = 8;
    char outfile[] = "../../data/energies.xyz";
    char header[] = "Face-centered cubic lattice of argon atoms";

    // Generate and initialize lattice
    System lattice = System(Nc);
    lattice.initialize_FCC_lattice(Nc);
    lattice.initialize_boltzmann_velocities(300/T0);
    lattice.eliminate_drift();

//    // Set up logger
//    Logger logger = Logger(&lattice, outfile);
//    logger.write_header(header);
//    lattice.enforce_periodic();

    Verlet_integrator solver = Verlet_integrator(&lattice);

    // Equilibriate
    for (int i=0; i<40; i++) {
        solver.velocity_verlet_step(dt);
//        logger.write_current_state();
        cout << lattice.temperature << endl;
    }

    // Step temperature up
    for (int i=0; i<200; i++) {
        solver.velocity_verlet_step(dt);
        solver.berendsen_thermostat(100/T0, 15.0);
//        logger.write_current_state();
        cout << lattice.temperature << endl;
    }
}


