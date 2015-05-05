#include <iostream>
#include "system.h"
#include "io.h"
#include "integrator.h"
#include "parameters.h"

using namespace std;

int main()
{
    int Nc = 20;
    char outfile[] = "../../data/energies.xyz";
    char header[] = "Face-centered cubic lattice of argon atoms";

    // Generate and initialize lattice
    System lattice = System(Nc);
    lattice.initialize_FCC_lattice(Nc);
    lattice.initialize_boltzmann_velocities(250/T0);
    lattice.eliminate_drift();

    // Set up logger
    Logger logger = Logger(&lattice, outfile);
    logger.write_header(header);
    lattice.enforce_periodic();

    Verlet_integrator solver = Verlet_integrator(&lattice);

    // Equilibriate
    for (int i=0; i<10; i++) {
        solver.velocity_verlet_step(dt);
        cout << lattice.temperature << endl;
    }
    for (int i=0; i<10; i++) {
        solver.velocity_verlet_step(dt);
        solver.berendsen_thermostat(0.851, 15.0);
        cout << lattice.temperature << endl;
    }


}


