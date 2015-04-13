#include <iostream>
#include "system.h"
#include "io.h"
#include "integrator.h"
#include "parameters.h"

using namespace std;

int main()
{
    int Nc = 8;
    char outfile[] = "../../data/centrallimit.xyz";
    char header[] = "Face-centered cubic lattice of argon atoms";

    // Generate and initialize lattice
    System lattice = System(Nc);
    lattice.initialize_FCC_lattice(Nc);
    lattice.initialize_uniform_velocities(100/eps);
    lattice.eliminate_drift();

    // Set up logger
    Logger logger = Logger(&lattice, outfile);
    logger.write_header(header);
    lattice.enforce_periodic();

    Verlet_integrator solver = Verlet_integrator(&lattice);

    for (int i=0; i<1000; i++) {
        solver.velocity_verlet_step(dt);
        logger.write_current_state();
        lattice.update_energies();
        cout << lattice.total_energy << endl;
    }
}


